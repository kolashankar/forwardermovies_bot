from config.settings import Settings
from config.constants import Constants
from bot.handlers import setup_handlers
from bot.middleware.user_activity import UserActivityMiddleware
from bot.middleware.rate_limiter import RateLimiterMiddleware
from telegram.ext import Application

class TelegramForwarderBot:
    def __init__(self):
        self.settings = Settings()
        self.constants = Constants()
        self.application = Application.builder().token(self.settings.BOT_TOKEN).build()

    def setup(self):
        # Set up handlers
        setup_handlers(self.application)

        # Set up middlewares
        self.application.add_handler(UserActivityMiddleware())
        self.application.add_handler(RateLimiterMiddleware(self.constants.RATE_LIMIT))

    async def run(self):
        self.setup()
        await self.application.initialize()
        await self.application.start()
        await self.application.run_polling()

    async def stop(self):
        await self.application.stop()

