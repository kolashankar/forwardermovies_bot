import os
from dotenv import load_dotenv

load_dotenv()

class BotConfig:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL")
    STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
    STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
    GOOGLE_TRANSLATE_API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    CONTENT_MODERATOR_API_KEY = os.getenv("CONTENT_MODERATOR_API_KEY")
    CONTENT_MODERATOR_ENDPOINT = os.getenv("CONTENT_MODERATOR_ENDPOINT")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Bot settings
    MAX_FORWARDING_RATE = 30  # messages per minute
    DEFAULT_LANGUAGE = "en"
    
    # Advanced filtering settings
    MIN_SENTIMENT_SCORE = -0.2
    ALLOWED_LANGUAGES = ["en", "es", "fr", "de", "it", "pt", "ru", "zh", "ja", "ko"]
    MAX_CONTENT_CATEGORY_CONFIDENCE = 0.8
    
    # Media processing settings
    MAX_VIDEO_DURATION = 600  # seconds
    MAX_AUDIO_SIZE = 50 * 1024 * 1024  # 50 MB
    IMAGE_ENHANCEMENT_QUALITY = 85
    
    # Channel management settings
    MAX_SCHEDULED_MESSAGES = 100
    MODERATION_THRESHOLD = 0.8
    AUTO_TAG_LIMIT = 10
    
    # User engagement settings
    MAX_QUIZ_QUESTIONS = 20
    POINTS_PER_ACTION = {
        "forward_message": 1,
        "create_poll": 5,
        "complete_quiz": 10,
        "invite_user": 20,
        "daily_login": 5
    }
    
    # Analytics settings
    DASHBOARD_UPDATE_INTERVAL = 30  # seconds
    RETENTION_ANALYSIS_DAYS = 30
    
    # Integration settings
    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
    MAX_EXTERNAL_SERVICES = 10
    
    # NLP and Machine Learning settings
    NLP_MODEL = "gpt-3.5-turbo"
    ML_MODEL_UPDATE_INTERVAL = 7 * 24 * 60 * 60  # 7 days
    
    # Premium features
    PREMIUM_FEATURES = [
        "advanced_filters",
        "media_processing",
        "content_scheduling",
        "advanced_analytics",
        "custom_integrations",
        "ai_assistance",
        "advanced_user_engagement",
        "content_optimization",
        "advanced_automation",
        "security_features",
        "multi_channel_management",
        "advanced_content_creation",
        "audience_insights",
        "advanced_notification_system",
        "content_monetization",
        "collaboration_tools",
        "advanced_search_and_archiving",
        "compliance_and_governance",
        "crisis_management",
        "advanced_localization",
        "smart_content_distribution",
        "advanced_a_b_testing",
        "predictive_analytics",
        "content_performance_optimization",
        "advanced_user_segmentation",
        "dynamic_content_personalization",
        "advanced_sentiment_analysis",
        "content_trend_forecasting",
        "advanced_competitor_analysis",
        "ai_powered_content_recommendations"
    ]

    # Subscription plans
    FREE_PLAN = {
        "name": "Free",
        "price": 0,
        "max_incoming_channels": 2,
        "max_outgoing_channels": 2,
        "max_messages_per_day": 200,
        "features": []
    }
    
    PREMIUM_PLAN = {
        "name": "Premium",
        "price": 100,  # in INR
        "max_incoming_channels": 10,
        "max_outgoing_channels": 10,
        "max_messages_per_day": -1,  # Unlimited
        "features": PREMIUM_FEATURES
    }
    
    ENTERPRISE_PLAN = {
        "name": "Enterprise",
        "price": 500,  # in INR
        "max_incoming_channels": -1,  # Unlimited
        "max_outgoing_channels": -1,  # Unlimited
        "max_messages_per_day": -1,  # Unlimited
        "features": PREMIUM_FEATURES + ["priority_support", "custom_development"]
    }

bot_config = BotConfig()

