import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL")
    STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
    STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_TRANSLATE_API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    CONTENT_MODERATOR_API_KEY = os.getenv("CONTENT_MODERATOR_API_KEY")
    CONTENT_MODERATOR_ENDPOINT = os.getenv("CONTENT_MODERATOR_ENDPOINT")
    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

config = Config()

