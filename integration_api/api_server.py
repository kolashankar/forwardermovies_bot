from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
import jwt
from datetime import datetime, timedelta
from models.user import User
from models.forwarding_task import ForwardingTask

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class UserInDB(BaseModel):
    username: str
    hashed_password: str

class ForwardingTaskCreate(BaseModel):
    source_channel: str
    destination_channel: str
    filter_keywords: str = None
    replace_keywords: str = None

class ForwardingTaskResponse(BaseModel):
    id: int
    source_channel: str
    destination_channel: str
    filter_keywords: str = None
    replace_keywords: str = None
    is_active: bool

def authenticate_user(username: str, password: str):
    user = User.get_by_username(username)
    if not user or not user.verify_password(password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = User.get_by_username(username)
    if user is None:
        raise credentials_exception
    return user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/tasks", response_model=ForwardingTaskResponse)
async def create_task(task: ForwardingTaskCreate, current_user: User = Depends(get_current_user)):
    new_task = ForwardingTask(
        user=current_user,
        source_channel=task.source_channel,
        destination_channel=task.destination_channel,
        filter_keywords=task.filter_keywords,
        replace_keywords=task.replace_keywords
    )
    new_task.save()
    return ForwardingTaskResponse(**new_task.to_dict())

@app.get("/tasks", response_model=List[ForwardingTaskResponse])
async def get_tasks(current_user: User = Depends(get_current_user)):
    tasks = ForwardingTask.get_by_user(current_user)
    return [ForwardingTaskResponse(**task.to_dict()) for task in tasks]

@app.put("/tasks/{task_id}", response_model=ForwardingTaskResponse)
async def update_task(task_id: int, task: ForwardingTaskCreate, current_user: User = Depends(get_current_user)):
    existing_task = ForwardingTask.get_by_id(task_id)
    if not existing_task or existing_task.user != current_user:
        raise HTTPException(status_code=404, detail="Task not found")
    
    existing_task.source_channel = task.source_channel
    existing_task.destination_channel = task.destination_channel
    existing_task.filter_keywords = task.filter_keywords
    existing_task.replace_keywords = task.replace_keywords
    existing_task.save()
    
    return ForwardingTaskResponse(**existing_task.to_dict())

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    existing_task = ForwardingTask.get_by_id(task_id)
    if not existing_task or existing_task.user != current_user:
        raise HTTPException(status_code=404, detail="Task not found")
    
    existing_task.delete()
    return {"detail": "Task deleted successfully"}

