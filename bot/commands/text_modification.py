from telegram import Update
from telegram.ext import CallbackContext
from database.models import User, Session

def begin_text(update: Update, context: CallbackContext):
    update.message.reply_text("Please provide the text to add at the beginning of forwarded messages.")
    context.user_data['next_step'] = 'set_begin_text'

def end_text(update: Update, context: CallbackContext):
    update.message.reply_text("Please provide the text to add at the end of forwarded messages.")
    context.user_data['next_step'] = 'set_end_text'

def remove_endtext(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.end_text = None
        session.commit()
        update.message.reply_text("Ending text removed successfully.")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()

def set_begin_text(update: Update, context: CallbackContext):
    begin_text = update.message.text.strip()
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.begin_text = begin_text
        session.commit()
        update.message.reply_text(f"Beginning text set to: {begin_text}")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()
    context.user_data['next_step'] = None

def set_end_text(update: Update, context: CallbackContext):
    end_text = update.message.text.strip()
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.end_text = end_text
        session.commit()
        update.message.reply_text(f"Ending text set to: {end_text}")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()
    context.user_data['next_step'] = None

