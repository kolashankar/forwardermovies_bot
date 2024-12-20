from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, ForwardingTask
from services.content_optimization import content_optimization_service
from services.advanced_analytics import advanced_analytics_service

router = APIRouter()

@router.post("/optimize_content")
async def optimize_content(text: str):
    optimized_text, sentiment = content_optimization_service.optimize_content(text)
    return {"optimized_text": optimized_text, "sentiment": sentiment}

@router.get("/user/{user_id}/tasks")
async def get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    tasks = db.query(ForwardingTask).filter(ForwardingTask.user_id == user_id).all()
    return tasks

@router.post("/generate_engagement_report")
async def generate_engagement_report(data: list):
    report = advanced_analytics_service.generate_engagement_report(data)
    return {"report": report}

@router.post("/predict_content_performance")
async def predict_content_performance(historical_data: list, new_content: str):
    prediction = advanced_analytics_service.predict_content_performance(historical_data, new_content)
    return {"predicted_performance": prediction}

