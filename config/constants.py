class Constants:
    # Forwarding limits
    MAX_FORWARDS_PER_DAY = 1000
    PREMIUM_MAX_FORWARDS_PER_DAY = 10000

    # Channel limits
    MAX_SOURCE_CHANNELS = 10
    MAX_DESTINATION_CHANNELS = 10
    PREMIUM_MAX_SOURCE_CHANNELS = 50
    PREMIUM_MAX_DESTINATION_CHANNELS = 50

    # Rate limiting
    RATE_LIMIT = 60  # messages per minute

    # Content types
    ALLOWED_CONTENT_TYPES = ['text', 'photo', 'video', 'document', 'audio']

    # Languages
    SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de', 'it']
    DEFAULT_LANGUAGE = 'en'

    # Subscription
    PREMIUM_SUBSCRIPTION_PRICE = 9.99  # USD per month

    # Backup
    BACKUP_INTERVAL = 86400  # 24 hours in seconds

    # Analytics
    ANALYTICS_UPDATE_INTERVAL = 3600  # 1 hour in seconds

