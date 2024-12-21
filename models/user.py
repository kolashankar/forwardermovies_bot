from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    is_premium = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.utcnow)

    forwarding_tasks = relationship("ForwardingTask", back_populates="user")



# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# from sqlalchemy.orm import relationship
# from .base import Base
# from .subscription_plan import SubscriptionPlan

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     telegram_id = Column(Integer, unique=True)
#     username = Column(String)
#     is_premium = Column(Boolean, default=False)
#     subscription_plan_id = Column(Integer, ForeignKey('subscription_plans.id'))

#     subscription_plan = relationship("SubscriptionPlan")
#     forwarding_tasks = relationship("ForwardingTask", back_populates="user")
#     forwarding_stats = relationship("ForwardingStats", back_populates="user")

#     def upgrade_to_premium(self, premium_plan):
#         self.is_premium = True
#         self.subscription_plan = premium_plan

#     def downgrade_to_free(self, free_plan):
#         self.is_premium = False
#         self.subscription_plan = free_plan

#     def can_add_incoming_channel(self):
#         return len(self.get_incoming_channels()) < self.subscription_plan.max_incoming_channels

#     def can_add_outgoing_channel(self):
#         return len(self.get_outgoing_channels()) < self.subscription_plan.max_outgoing_channels

#     def get_incoming_channels(self):
#         return [task.source_channel for task in self.forwarding_tasks]

#     def get_outgoing_channels(self):
#         return [task.destination_channel for task in self.forwarding_tasks]

#     def add_forwarding_task(self, source_channel, destination_channel):
#         if self.can_add_incoming_channel() and self.can_add_outgoing_channel():
#             task = ForwardingTask(user=self, source_channel=source_channel, destination_channel=destination_channel)
#             self.forwarding_tasks.append(task)
#             return True
#         return False

#     def remove_forwarding_task(self, task_id):
#         task = next((task for task in self.forwarding_tasks if task.id == task_id), None)
#         if task:
#             self.forwarding_tasks.remove(task)
#             return True
#         return False

#     @classmethod
#     def get_by_telegram_id(cls, session, telegram_id):
#         return session.query(cls).filter_by(telegram_id=telegram_id).first()

#     @classmethod
#     def create_user(cls, session, telegram_id, username):
#         user = cls(telegram_id=telegram_id, username=username)
#         free_plan = SubscriptionPlan.get_free_plan()
#         user.subscription_plan = free_plan
#         session.add(user)
#         session.commit()
#         return user

