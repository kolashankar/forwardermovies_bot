import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackQueryHandler
from config.bot_config import bot_config
from bot.handlers.setup_handlers import setup_handlers
from services.scheduler_service import SchedulerService
from services.logging_service import logging_service
from services.ocr_service import OCRService
from services.captcha_service import CaptchaService
from advanced_filtering.sentiment_filter import SentimentFilter
from advanced_filtering.language_filter import LanguageFilter
from advanced_filtering.regex_filter import RegexFilter
from advanced_filtering.content_category_filter import ContentCategoryFilter
from media_processing.image_enhancer import ImageEnhancer
from media_processing.video_trimmer import VideoTrimmer
from media_processing.audio_converter import AudioConverter
from media_processing.file_converter import FileConverter
from channel_management.channel_stats import ChannelStats
from channel_management.content_scheduler import ContentScheduler
from channel_management.content_moderator import ContentModerator
from channel_management.auto_tagger import AutoTagger
from user_engagement.poll_creator import PollCreator
from user_engagement.quiz_manager import QuizManager
from user_engagement.gamification import Gamification
from user_engagement.feedback_collector import FeedbackCollector
from analytics_reporting.user_activity_tracker import UserActivityTracker
from analytics_reporting.performance_metrics import PerformanceMetrics
from analytics_reporting.report_generator import ReportGenerator
from analytics_reporting.dashboard_generator import DashboardGenerator
from integration_api.api_server import start_api_server
from integration_api.webhook_handler import setup_webhook_handler
from integration_api.integration_manager import IntegrationManager
from services.nlp_service import NLPService
from services.machine_learning_service import MachineLearningService
from premium_features.ai_assistance import AIAssistance
from premium_features.content_optimization import ContentOptimization
from premium_features.advanced_automation import AdvancedAutomation
from premium_features.advanced_user_engagement import AdvancedUserEngagement
from premium_features.security_features import SecurityFeatures
from premium_features.multi_channel_management import MultiChannelManagement
from premium_features.advanced_content_creation import AdvancedContentCreation
from premium_features.audience_insights import AudienceInsights
from premium_features.advanced_notification_system import AdvancedNotificationSystem
from premium_features.content_monetization import ContentMonetization
from premium_features.collaboration_tools import CollaborationTools
from premium_features.advanced_search_and_archiving import AdvancedSearchAndArchiving
from premium_features.compliance_and_governance import ComplianceAndGovernance
from premium_features.crisis_management import CrisisManagement
from premium_features.advanced_localization import AdvancedLocalization
from premium_features.advanced_analytics import AdvancedAnalytics
from premium_features.advanced_scheduling import AdvancedScheduling
from premium_features.smart_content_distribution import SmartContentDistribution
from premium_features.advanced_a_b_testing import AdvancedABTesting
from premium_features.predictive_analytics import PredictiveAnalytics
from premium_features.content_performance_optimization import ContentPerformanceOptimization
from premium_features.advanced_user_segmentation import AdvancedUserSegmentation
from premium_features.dynamic_content_personalization import DynamicContentPersonalization
from premium_features.advanced_sentiment_analysis import AdvancedSentimentAnalysis
from premium_features.content_trend_forecasting import ContentTrendForecasting
from premium_features.advanced_competitor_analysis import AdvancedCompetitorAnalysis
from premium_features.ai_powered_content_recommendations import AIPoweredContentRecommendations

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    application = Application.builder().token(bot_config.TELEGRAM_BOT_TOKEN).build()

    # Initialize services
    scheduler_service = SchedulerService(application.bot)
    ocr_service = OCRService()
    captcha_service = CaptchaService()
    sentiment_filter = SentimentFilter()
    language_filter = LanguageFilter()
    regex_filter = RegexFilter()
    content_category_filter = ContentCategoryFilter()
    image_enhancer = ImageEnhancer()
    video_trimmer = VideoTrimmer()
    audio_converter = AudioConverter()
    file_converter = FileConverter()
    channel_stats = ChannelStats(application.bot)
    content_scheduler = ContentScheduler(application.bot)
    content_moderator = ContentModerator()
    auto_tagger = AutoTagger()
    poll_creator = PollCreator(application.bot)
    quiz_manager = QuizManager()
    gamification = Gamification()
    feedback_collector = FeedbackCollector(application.bot)
    user_activity_tracker = UserActivityTracker()
    performance_metrics = PerformanceMetrics()
    report_generator = ReportGenerator()
    dashboard_generator = DashboardGenerator()
    integration_manager = IntegrationManager()
    nlp_service = NLPService()
    ml_service = MachineLearningService()

    # Initialize premium features
    ai_assistance = AIAssistance()
    content_optimization = ContentOptimization()
    advanced_automation = AdvancedAutomation()
    advanced_user_engagement = AdvancedUserEngagement()
    security_features = SecurityFeatures()
    multi_channel_management = MultiChannelManagement()
    advanced_content_creation = AdvancedContentCreation()
    audience_insights = AudienceInsights()
    advanced_notification_system = AdvancedNotificationSystem()
    content_monetization = ContentMonetization()
    collaboration_tools = CollaborationTools()
    advanced_search_and_archiving = AdvancedSearchAndArchiving()
    compliance_and_governance = ComplianceAndGovernance()
    crisis_management = CrisisManagement()
    advanced_localization = AdvancedLocalization()
    advanced_analytics = AdvancedAnalytics()
    advanced_scheduling = AdvancedScheduling()
    smart_content_distribution = SmartContentDistribution()
    advanced_ab_testing = AdvancedABTesting()
    predictive_analytics = PredictiveAnalytics()
    content_performance_optimization = ContentPerformanceOptimization()
    advanced_user_segmentation = AdvancedUserSegmentation()
    dynamic_content_personalization = DynamicContentPersonalization()
    advanced_sentiment_analysis = AdvancedSentimentAnalysis()
    content_trend_forecasting = ContentTrendForecasting()
    advanced_competitor_analysis = AdvancedCompetitorAnalysis()
    ai_powered_content_recommendations = AIPoweredContentRecommendations()

    # Set up command and message handlers
    setup_handlers(application, {
        'scheduler_service': scheduler_service,
        'ocr_service': ocr_service,
        'captcha_service': captcha_service,
        'sentiment_filter': sentiment_filter,
        'language_filter': language_filter,
        'regex_filter': regex_filter,
        'content_category_filter': content_category_filter,
        'image_enhancer': image_enhancer,
        'video_trimmer': video_trimmer,
        'audio_converter': audio_converter,
        'file_converter': file_converter,
        'channel_stats': channel_stats,
        'content_scheduler': content_scheduler,
        'content_moderator': content_moderator,
        'auto_tagger': auto_tagger,
        'poll_creator': poll_creator,
        'quiz_manager': quiz_manager,
        'gamification': gamification,
        'feedback_collector': feedback_collector,
        'user_activity_tracker': user_activity_tracker,
        'performance_metrics': performance_metrics,
        'report_generator': report_generator,
        'dashboard_generator': dashboard_generator,
        'integration_manager': integration_manager,
        'nlp_service': nlp_service,
        'ml_service': ml_service,
        'ai_assistance': ai_assistance,
        'content_optimization': content_optimization,
        'advanced_automation': advanced_automation,
        'advanced_user_engagement': advanced_user_engagement,
        'security_features': security_features,
        'multi_channel_management': multi_channel_management,
        'advanced_content_creation': advanced_content_creation,
        'audience_insights': audience_insights,
        'advanced_notification_system': advanced_notification_system,
        'content_monetization': content_monetization,
        'collaboration_tools': collaboration_tools,
        'advanced_search_and_archiving': advanced_search_and_archiving,
        'compliance_and_governance': compliance_and_governance,
        'crisis_management': crisis_management,
        'advanced_localization': advanced_localization,
        'advanced_analytics': advanced_analytics,
        'advanced_scheduling': advanced_scheduling,
        'smart_content_distribution': smart_content_distribution,
        'advanced_ab_testing': advanced_ab_testing,
        'predictive_analytics': predictive_analytics,
        'content_performance_optimization': content_performance_optimization,
        'advanced_user_segmentation': advanced_user_segmentation,
        'dynamic_content_personalization': dynamic_content_personalization,
        'advanced_sentiment_analysis': advanced_sentiment_analysis,
        'content_trend_forecasting': content_trend_forecasting,
        'advanced_competitor_analysis': advanced_competitor_analysis,
        'ai_powered_content_recommendations': ai_powered_content_recommendations,
    })

    # Set up conversation handler for advanced scheduling
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('schedule_content', advanced_scheduling.start_scheduling)],
        states={
            SELECTING_CHANNEL: [CallbackQueryHandler(advanced_scheduling.channel_selected, pattern='^channel_')],
            SELECTING_TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, advanced_scheduling.time_selected)],
            SELECTING_FREQUENCY: [CallbackQueryHandler(advanced_scheduling.frequency_selected, pattern='^freq_')],
            CONFIRMING: [CallbackQueryHandler(advanced_scheduling.confirm_scheduling, pattern='^confirm_')]
        },
        fallbacks=[CommandHandler('cancel', lambda u, c: ConversationHandler.END)]
    )
    application.add_handler(conv_handler)

    # Add handlers for viewing and cancelling scheduled tasks
    application.add_handler(CommandHandler('view_scheduled_tasks', advanced_scheduling.view_scheduled_tasks))
    application.add_handler(CommandHandler('cancel_scheduled_task', advanced_scheduling.cancel_scheduled_task))

    # Start the scheduler
    scheduler_service.start()

    # Log bot startup
    logging_service.info("Enhanced Telegram Auto Forwarder Bot started with advanced premium features")

    # Start the API server
    api_server = start_api_server(integration_manager)

    # Setup webhook handler
    setup_webhook_handler(application)

    # Start polling
    await application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

