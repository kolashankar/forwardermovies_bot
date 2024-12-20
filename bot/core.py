from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config.settings import Settings
from config.constants import Constants
from bot.handlers import setup_handlers
from bot.middleware.user_activity import UserActivityMiddleware
from bot.middleware.rate_limiter import RateLimiterMiddleware

class TelegramForwarderBot:
    def __init__(self):
        self.settings = Settings()
        self.constants = Constants()
        self.updater = Updater(token=self.settings.BOT_TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def setup(self):
        # Set up handlers
        setup_handlers(self.dispatcher)

        # Set up middlewares
        self.dispatcher.add_handler(UserActivityMiddleware())
        self.dispatcher.add_handler(RateLimiterMiddleware(self.constants.RATE_LIMIT))

    def run(self):
        self.setup()
        self.updater.start_polling()
        self.updater.idle()

    def stop(self):
        self.updater.stop()

