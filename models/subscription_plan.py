from sqlalchemy import Column, Integer, String, Float
from .base import Base

class SubscriptionPlan(Base):
    __tablename__ = 'subscription_plans'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(Float)
    max_incoming_channels = Column(Integer)
    max_outgoing_channels = Column(Integer)
    max_messages_per_day = Column(Integer)

    @classmethod
    def get_free_plan(cls):
        return cls.query.filter_by(name='Free').first()

    @classmethod
    def get_premium_plan(cls):
        return cls.query.filter_by(name='Premium').first()

    @staticmethod
    def create_default_plans():
        free_plan = SubscriptionPlan(
            name='Free',
            price=0,
            max_incoming_channels=1,
            max_outgoing_channels=1,
            max_messages_per_day=100
        )
        premium_plan = SubscriptionPlan(
            name='Premium',
            price=100,
            max_incoming_channels=5,
            max_outgoing_channels=5,
            max_messages_per_day=-1  # Unlimited
        )
        return [free_plan, premium_plan]

