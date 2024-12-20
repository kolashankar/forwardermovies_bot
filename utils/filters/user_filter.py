from telegram.ext import MessageFilter
from models.user import User

class UserFilter(MessageFilter):
    def __init__(self, user_type):
        self.user_type = user_type

    def filter(self, message):
        user = User.objects(user_id=message.from_user.id).first()
        if user:
            if self.user_type == 'premium':
                return user.is_premium
            elif self.user_type == 'admin':
                return user.is_admin
            elif self.user_type == 'active':
                return user.is_active
        return False

