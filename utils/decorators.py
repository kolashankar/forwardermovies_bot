from functools import wraps
from telegram import Update
from telegram.ext import CallbackContext
from models.user import User

def premium_required(func):
    @wraps(func)
    async def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
        user = User.get_by_telegram_id(update.effective_user.id)
        if user and user.is_premium:
            return await func(update, context, *args, **kwargs)
        else:
            await update.message.reply_text("This feature is only available for premium users. Upgrade your plan to access it.")
    return wrapper

