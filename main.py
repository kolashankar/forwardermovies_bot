import asyncio
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters
from config import config
from bot.handlers import setup_handlers
from bot.premium_commands import optimize_content, generate_analytics, predict_performance
from bot.auth_handlers import (
    start_phone_auth, phone_number_received, otp_received,
    start_email_verification, email_received, email_otp_received
)
from bot.shortlink_commands import (
    start_add_provider, provider_received, api_key_received, api_url_received, create_shortlink
)
from database import engine
from services.scheduler import scheduler_service
import models

PHONE, OTP, EMAIL, EMAIL_OTP = range(4)
PROVIDER, API_KEY, API_URL = range(3)

async def main():
    # Create database tables
    models.Base.metadata.create_all(bind=engine)

    # Create the Application and pass it your bot's token
    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()

    # Setup handlers
    setup_handlers(application)

    # Add premium command handlers
    application.add_handler(CommandHandler("optimize", optimize_content))
    application.add_handler(CommandHandler("analytics", generate_analytics))
    application.add_handler(CommandHandler("predict", predict_performance))

    # Add authentication handlers
    phone_auth_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start_phone_auth)],
        states={
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, phone_number_received)],
            OTP: [MessageHandler(filters.TEXT & ~filters.COMMAND, otp_received)],
        },
        fallbacks=[],
    )
    application.add_handler(phone_auth_handler)

    email_verification_handler = ConversationHandler(
        entry_points=[CommandHandler("verify_email", start_email_verification)],
        states={
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, email_received)],
            EMAIL_OTP: [MessageHandler(filters.TEXT & ~filters.COMMAND, email_otp_received)],
        },
        fallbacks=[],
    )
    application.add_handler(email_verification_handler)

    # Add shortlink handlers
    shortlink_provider_handler = ConversationHandler(
        entry_points=[CommandHandler("add_shortlink_provider", start_add_provider)],
        states={
            PROVIDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, provider_received)],
            API_KEY: [MessageHandler(filters.TEXT & ~filters.COMMAND, api_key_received)],
            API_URL: [MessageHandler(filters.TEXT & ~filters.COMMAND, api_url_received)],
        },
        fallbacks=[],
    )
    application.add_handler(shortlink_provider_handler)
    application.add_handler(CommandHandler("shortlink", create_shortlink))

    # Start the scheduler
    scheduler_service.start()

    # Start the Bot
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())

