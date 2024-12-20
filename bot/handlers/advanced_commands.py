from telegram import Update
from telegram.ext import CallbackContext
from services.template_service import TemplateService
from services.filter_service import FilterService
from services.analytics_service import AnalyticsService
from services.translation_service import TranslationService
from services.watermark_service import WatermarkService
from services.backup_service import BackupService

template_service = TemplateService()
filter_service = FilterService()
analytics_service = AnalyticsService()
translation_service = TranslationService()
watermark_service = WatermarkService()
backup_service = BackupService()

def templates(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    templates = template_service.get_user_templates(user_id)
    update.message.reply_text(f"Your templates: {templates}")

def filters(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    filters = filter_service.get_user_filters(user_id)
    update.message.reply_text(f"Your filters: {filters}")

def analytics(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    stats = analytics_service.get_user_stats(user_id)
    update.message.reply_text(f"Your stats: {stats}")

def translate(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    settings = translation_service.get_user_settings(user_id)
    update.message.reply_text(f"Your translation settings: {settings}")

def watermark(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    settings = watermark_service.get_user_settings(user_id)
    update.message.reply_text(f"Your watermark settings: {settings}")

def backup(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    backup_data = backup_service.create_backup(user_id)
    update.message.reply_text(f"Backup created: {backup_data}")

def captions(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    captions = template_service.get_user_captions(user_id)
    update.message.reply_text(f"Your captions: {captions}")

def handle_advanced_command(update: Update, context: CallbackContext):
    command = update.message.text.split()[0][1:]
    command_functions = {
        'templates': templates,
        'filters': filters,
        'analytics': analytics,
        'translate': translate,
        'watermark': watermark,
        'backup': backup,
        'captions': captions
    }
    if command in command_functions:
        command_functions[command](update, context)
    else:
        update.message.reply_text("Unknown advanced command. Please use /help for a list of available commands.")

