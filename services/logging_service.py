import logging
from logging.handlers import RotatingFileHandler
import os

class LoggingService:
    def __init__(self, log_file='bot.log', max_size=1024*1024, backup_count=5):
        self.logger = logging.getLogger('TelegramForwarderBot')
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # File handler
        file_handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

    def debug(self, message):
        self.logger.debug(message)

logging_service = LoggingService()

