from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    username = Column(String, index=True)
    phone_number = Column(String)
    email = Column(String)
    is_authenticated = Column(Boolean, default=False)
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    forwarding_tasks = relationship("ForwardingTask", back_populates="user")

class ForwardingTask(Base):
    __tablename__ = "forwarding_tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    source_channel = Column(String)
    destination_channel = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="forwarding_tasks")

class ShortlinkProvider(Base):
    __tablename__ = "shortlink_providers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    provider_name = Column(String)
    api_key = Column(String)
    api_url = Column(String)

    user = relationship("User")

