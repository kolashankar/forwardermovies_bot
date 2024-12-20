from telegram import Update
from telegram.ext import CallbackContext
from database.models import User, Session

def time_scheduler(update: Update, context: CallbackContext):
    update.message.reply_text("Please provide the forwarding schedule in the format: HH:MM-HH:MM, separated by commas.")
    context.user_data['next_step'] = 'set_schedule'

def remove_slots(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.schedule = None
        session.commit()
        update.message.reply_text("Scheduled slots removed successfully.")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()

def disconnect(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.source_channel = None
        user.destination_channel = None
        session.commit()
        update.message.reply_text("Disconnected from all channels.")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()

def status(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        status_text = f"""
        Forwarding status:
        Source channel: {user.source_channel or 'Not set'}
        Destination channel: {user.destination_channel or 'Not set'}
        Schedule: {user.schedule or 'Not set'}
        Active: {'Yes' if user.is_active else 'No'}
        """
        update.message.reply_text(status_text)
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()

def set_schedule(update: Update, context: CallbackContext):
    schedule = update.message.text.strip()
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.schedule = schedule
        session.commit()
        update.message.reply_text(f"Forwarding schedule set to: {schedule}")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()
    context.user_data['next_step'] = None

