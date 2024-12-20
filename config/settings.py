import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Bot settings
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    BOT_USERNAME = os.getenv('BOT_USERNAME')

    # API settings
    API_ID = os.getenv('API_ID')
    API_HASH = os.getenv('API_HASH')

    # Database settings
    DATABASE_URL = os.getenv('DATABASE_URL')

    # Redis settings (for caching and rate limiting)
    REDIS_URL = os.getenv('REDIS_URL')

    # Admin settings
    ADMIN_USER_IDS = list(map(int, os.getenv('ADMIN_USER_IDS', '').split(',')))

    # Logging settings
    LOG_CHANNEL_ID = int(os.getenv('LOG_CHANNEL_ID', 0))
    ERROR_LOG_CHANNEL_ID = int(os.getenv('ERROR_LOG_CHANNEL_ID', 0))

    # Premium settings
    PREMIUM_CHANNEL_ID = int(os.getenv('PREMIUM_CHANNEL_ID', 0))

    # Analytics settings
    ENABLE_ANALYTICS = os.getenv('ENABLE_ANALYTICS', 'False').lower() == 'true'
    ANALYTICS_TOKEN = os.getenv('ANALYTICS_TOKEN')

    # Shortlink settings
    SHORTLINK_API = os.getenv('SHORTLINK_API')
    SHORTLINK_URL = os.getenv('SHORTLINK_URL')

    # Webhook settings (for production)
    WEBHOOK_URL = os.getenv('WEBHOOK_URL')
    WEBHOOK_PORT = int(os.getenv('WEBHOOK_PORT', 8443))

    # Performance settings
    MAX_CONCURRENT_TASKS = int(os.getenv('MAX_CONCURRENT_TASKS', 5))

    # Stripe settings
    STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')
    STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')

    # Feature flags
    ENABLE_PREMIUM_FEATURES = os.getenv('ENABLE_PREMIUM_FEATURES', 'True').lower() == 'true'
    ENABLE_ANALYTICS = os.getenv('ENABLE_ANALYTICS', 'True').lower() == 'true'
    ENABLE_SHORTLINKS = os.getenv('ENABLE_SHORTLINKS', 'True').lower() == 'true'

