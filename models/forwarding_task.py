from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class ForwardingTask(Base):
    __tablename__ = 'forwarding_tasks'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source_channel = Column(String)
    destination_channel = Column(String)
    is_active = Column(Boolean, default=True)
    filter_keywords = Column(String)
    replace_keywords = Column(String)
    begin_text = Column(String)
    end_text = Column(String)

    user = relationship("User", back_populates="forwarding_tasks")

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def update_filters(self, filter_keywords, replace_keywords):
        self.filter_keywords = filter_keywords
        self.replace_keywords = replace_keywords

    def update_text_modifications(self, begin_text, end_text):
        self.begin_text = begin_text
        self.end_text = end_text

