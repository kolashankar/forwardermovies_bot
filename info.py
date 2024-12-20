import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_USERNAME = os.getenv('BOT_USERNAME')

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'forwarder_bot')

# Channel Configuration
SOURCE_CHANNELS = os.getenv('SOURCE_CHANNELS', '').split(',')
DESTINATION_CHANNELS = os.getenv('DESTINATION_CHANNELS', '').split(',')
MAX_SOURCE_CHANNELS = int(os.getenv('MAX_SOURCE_CHANNELS', '5'))
MAX_DESTINATION_CHANNELS = int(os.getenv('MAX_DESTINATION_CHANNELS', '5'))

# Forwarding Configuration
FORWARD_DELAY = int(os.getenv('FORWARD_DELAY', '0'))
FORWARD_FILTERS = os.getenv('FORWARD_FILTERS', '').split(',')
MAX_FORWARDS_PER_DAY = int(os.getenv('MAX_FORWARDS_PER_DAY', '1000'))
FORWARD_MEDIA = os.getenv('FORWARD_MEDIA', 'True').lower() == 'true'
FORWARD_STICKERS = os.getenv('FORWARD_STICKERS', 'False').lower() == 'true'
FORWARD_VOICE_MESSAGES = os.getenv('FORWARD_VOICE_MESSAGES', 'False').lower() == 'true'

# Premium Features
PREMIUM_ENABLED = os.getenv('PREMIUM_ENABLED', 'False').lower() == 'true'
PREMIUM_PRICE = float(os.getenv('PREMIUM_PRICE', '0'))
PREMIUM_FEATURES = os.getenv('PREMIUM_FEATURES', '').split(',')
PREMIUM_MAX_FORWARDS_PER_DAY = int(os.getenv('PREMIUM_MAX_FORWARDS_PER_DAY', '5000'))
PREMIUM_MAX_SOURCE_CHANNELS = int(os.getenv('PREMIUM_MAX_SOURCE_CHANNELS', '20'))
PREMIUM_MAX_DESTINATION_CHANNELS = int(os.getenv('PREMIUM_MAX_DESTINATION_CHANNELS', '20'))

# Shortlink Configuration
SHORTLINK_API = os.getenv('SHORTLINK_API')
SHORTLINK_URL = os.getenv('SHORTLINK_URL')
SHORTLINK_DOMAINS = os.getenv('SHORTLINK_DOMAINS', '').split(',')
SHORTLINK_TIMEOUT = int(os.getenv('SHORTLINK_TIMEOUT', '10'))

# Admin Configuration
ADMIN_USER_IDS = list(map(int, os.getenv('ADMIN_USER_IDS', '').split(',')))
OWNER_ID = int(os.getenv('OWNER_ID', '0'))
ADMIN_COMMANDS = os.getenv('ADMIN_COMMANDS', '').split(',')

# Logging Configuration
LOG_CHANNEL_ID = int(os.getenv('LOG_CHANNEL_ID', '0'))
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = os.getenv('LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Additional Features
ENABLE_WATERMARK = os.getenv('ENABLE_WATERMARK', 'False').lower() == 'true'
WATERMARK_TEXT = os.getenv('WATERMARK_TEXT', '')
WATERMARK_COLOR = os.getenv('WATERMARK_COLOR', 'white')
WATERMARK_POSITION = os.getenv('WATERMARK_POSITION', 'bottom-right')
ENABLE_CAPTION_EDITING = os.getenv('ENABLE_CAPTION_EDITING', 'False').lower() == 'true'
CAPTION_TEMPLATE = os.getenv('CAPTION_TEMPLATE', '{original_caption}')
ENABLE_FILE_RENAMING = os.getenv('ENABLE_FILE_RENAMING', 'False').lower() == 'true'
FILE_RENAME_TEMPLATE = os.getenv('FILE_RENAME_TEMPLATE', '{original_filename}')

# Performance Settings
MAX_CONCURRENT_TASKS = int(os.getenv('MAX_CONCURRENT_TASKS', '5'))
RATE_LIMIT = int(os.getenv('RATE_LIMIT', '60'))  # messages per minute
CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', '10'))  # number of messages to process in one batch
SLEEP_TIME = int(os.getenv('SLEEP_TIME', '5'))  # seconds to sleep between batches

# Error Handling
ERROR_LOG_CHANNEL_ID = int(os.getenv('ERROR_LOG_CHANNEL_ID', '0'))
MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))
RETRY_DELAY = int(os.getenv('RETRY_DELAY', '60'))  # seconds

# Custom Commands
CUSTOM_START_MESSAGE = os.getenv('CUSTOM_START_MESSAGE', 'Welcome to the Telegram Auto Forwarder Bot!')
CUSTOM_HELP_MESSAGE = os.getenv('CUSTOM_HELP_MESSAGE', 'Here are the available commands...')
CUSTOM_COMMANDS = os.getenv('CUSTOM_COMMANDS', '').split(',')

# Scheduler Settings
SCHEDULER_ENABLED = os.getenv('SCHEDULER_ENABLED', 'False').lower() == 'true'
SCHEDULER_INTERVAL = int(os.getenv('SCHEDULER_INTERVAL', '3600'))  # Default to 1 hour
SCHEDULER_TIMEZONE = os.getenv('SCHEDULER_TIMEZONE', 'UTC')

# User Management
MAX_USERS = int(os.getenv('MAX_USERS', '1000'))
USER_EXPIRY_DAYS = int(os.getenv('USER_EXPIRY_DAYS', '30'))
USER_COOLDOWN = int(os.getenv('USER_COOLDOWN', '60'))  # seconds

# Content Filtering
BANNED_WORDS = os.getenv('BANNED_WORDS', '').split(',')
ALLOWED_CONTENT_TYPES = os.getenv('ALLOWED_CONTENT_TYPES', 'text,photo,video,document').split(',')
CONTENT_FILTER_ACTION = os.getenv('CONTENT_FILTER_ACTION', 'delete')  # 'delete' or 'replace'
CONTENT_REPLACEMENT_TEXT = os.getenv('CONTENT_REPLACEMENT_TEXT', '[Content removed]')

# Notification Settings
ENABLE_START_NOTIFICATION = os.getenv('ENABLE_START_NOTIFICATION', 'True').lower() == 'true'
ENABLE_STOP_NOTIFICATION = os.getenv('ENABLE_STOP_NOTIFICATION', 'True').lower() == 'true'
NOTIFICATION_CHAT_ID = int(os.getenv('NOTIFICATION_CHAT_ID', '0'))

# Language Settings
DEFAULT_LANGUAGE = os.getenv('DEFAULT_LANGUAGE', 'en')
SUPPORTED_LANGUAGES = os.getenv('SUPPORTED_LANGUAGES', 'en,es,fr,de').split(',')
TRANSLATION_SERVICE = os.getenv('TRANSLATION_SERVICE', 'google')

# Backup Settings
ENABLE_AUTO_BACKUP = os.getenv('ENABLE_AUTO_BACKUP', 'False').lower() == 'true'
BACKUP_INTERVAL = int(os.getenv('BACKUP_INTERVAL', '86400'))  # Default to daily
BACKUP_CHANNEL_ID = int(os.getenv('BACKUP_CHANNEL_ID', '0'))
MAX_BACKUPS = int(os.getenv('MAX_BACKUPS', '7'))

# Analytics
ENABLE_ANALYTICS = os.getenv('ENABLE_ANALYTICS', 'False').lower() == 'true'
ANALYTICS_TOKEN = os.getenv('ANALYTICS_TOKEN', '')
ANALYTICS_PLATFORM = os.getenv('ANALYTICS_PLATFORM', 'google')

# Security
ENABLE_2FA = os.getenv('ENABLE_2FA', 'False').lower() == 'true'
API_RATE_LIMIT = int(os.getenv('API_RATE_LIMIT', '100'))  # requests per minute
ALLOWED_IPS = os.getenv('ALLOWED_IPS', '').split(',')

# Monitoring
ENABLE_HEALTH_CHECK = os.getenv('ENABLE_HEALTH_CHECK', 'False').lower() == 'true'
HEALTH_CHECK_INTERVAL = int(os.getenv('HEALTH_CHECK_INTERVAL', '300'))  # seconds
ALERT_EMAIL = os.getenv('ALERT_EMAIL', '')

# Caching
ENABLE_CACHING = os.getenv('ENABLE_CACHING', 'False').lower() == 'true'
CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')
CACHE_EXPIRATION = int(os.getenv('CACHE_EXPIRATION', '3600'))  # seconds

# Version Information
BOT_VERSION = '1.2.0'

