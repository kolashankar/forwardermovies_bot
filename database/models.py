from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import DATABASE_URL
from datetime import datetime, date

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    is_premium = Column(Boolean, default=False)
    incoming_channels = Column(String)  # Comma-separated list of channel IDs
    outgoing_channels = Column(String)  # Comma-separated list of channel IDs
    messages_forwarded_today = Column(Integer, default=0)
    last_forward_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    total_forwarded = Column(Integer, default=0)

Base.metadata.create_all(engine)

