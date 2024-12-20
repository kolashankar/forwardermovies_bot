from telegram.ext import BaseMiddleware
from cachetools import TTLCache
from datetime import datetime, timedelta

class RateLimiterMiddleware(BaseMiddleware):
    def __init__(self, rate_limit):
        super().__init__()
        self.rate_limit = rate_limit
        self.cache = TTLCache(maxsize=10000, ttl=60)

    def on_process_update(self, update, context):
        if update.effective_user:
            user_id = update.effective_user.id
            current_time = datetime.now()
            
            if user_id in self.cache:
                last_time, count = self.cache[user_id]
                if (current_time - last_time) < timedelta(minutes=1):
                    if count >= self.rate_limit:
                        context.bot.send_message(
                            chat_id=update.effective_chat.id,
                            text="You've reached the rate limit. Please try again later."
                        )
                        return False
                    else:
                        self.cache[user_id] = (last_time, count + 1)
                else:
                    self.cache[user_id] = (current_time, 1)
            else:
                self.cache[user_id] = (current_time, 1)

