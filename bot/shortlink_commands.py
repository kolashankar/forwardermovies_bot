from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from services.shortlink_service import ShortlinkService

PROVIDER, API_KEY, API_URL = range(3)

shortlink_service = ShortlinkService()

async def start_add_provider(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter the name of the shortlink provider:")
    return PROVIDER

async def provider_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['provider_name'] = update.message.text
    await update.message.reply_text("Please enter the API key:")
    return API_KEY

async def api_key_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['api_key'] = update.message.text
    await update.message.reply_text("Please enter the API URL:")
    return API_URL

async def api_url_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    api_url = update.message.text
    provider = await shortlink_service.add_shortlink_provider(
        update.effective_user.id,
        context.user_data['provider_name'],
        context.user_data['api_key'],
        api_url
    )
    await update.message.reply_text(f"Shortlink provider {provider.provider_name} added successfully!")
    return ConversationHandler.END

async def create_shortlink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide a URL to shorten.")
        return

    long_url = context.args[0]
    shortlink, error = await shortlink_service.create_shortlink(update.effective_user.id, long_url)
    
    if shortlink:
        await update.message.reply_text(f"Here's your shortened URL: {shortlink}")
    else:
        await update.message.reply_text(f"Error creating shortlink: {error}")

