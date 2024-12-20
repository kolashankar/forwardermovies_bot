from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class ForwardingStats(Base):
    __tablename__ = 'forwarding_stats'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    messages_forwarded = Column(Integer, default=0)
    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="forwarding_stats")

    def increment_forwarded_count(self, count=1):
        self.messages_forwarded += count

    @classmethod
    def get_or_create(cls, session, user_id):
        stats = session.query(cls).filter_by(user_id=user_id, date=datetime.utcnow().date()).first()
        if not stats:
            stats = cls(user_id=user_id)
            session.add(stats)
            session.commit()
        return stats

