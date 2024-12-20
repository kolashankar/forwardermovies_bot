from telegram.ext import BaseMiddleware
from models.user import User
from datetime import datetime

class UserActivityMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    def on_process_update(self, update, context):
        if update.effective_user:
            user_id = update.effective_user.id
            user = User.objects(user_id=user_id).first()
            if user:
                user.last_activity = datetime.utcnow()
                user.save()
            else:
                User(
                    user_id=user_id,
                    username=update.effective_user.username,
                    first_name=update.effective_user.first_name,
                    last_name=update.effective_user.last_name,
                    last_activity=datetime.utcnow()
                ).save()

