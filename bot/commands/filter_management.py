from telegram import Update
from telegram.ext import CallbackContext
from database.models import User, Session

def remove_keywords(update: Update, context: CallbackContext):
    update.message.reply_text("Please provide keywords to remove, separated by commas.")
    context.user_data['next_step'] = 'set_remove_keywords'

def replace_keywords(update: Update, context: CallbackContext):
    update.message.reply_text("Please provide keyword replacements in the format: old_word:new_word, separated by commas.")
    context.user_data['next_step'] = 'set_replace_keywords'

def remove_replacekeywords(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.replace_keywords = None
        session.commit()
        update.message.reply_text("Replacement rules removed successfully.")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()

def blacklist(update: Update, context: CallbackContext):
    update.message.reply_text("Please provide words to blacklist, separated by commas.")
    context.user_data['next_step'] = 'set_blacklist'

def remove_blacklist(update: Update, context: CallbackContext):
    update.message.reply_text("Please provide words to remove from the blacklist, separated by commas.")
    context.user_data['next_step'] = 'remove_from_blacklist'

def set_remove_keywords(update: Update, context: CallbackContext):
    keywords = [k.strip() for k in update.message.text.split(',')]
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.remove_keywords = ','.join(keywords)
        session.commit()
        update.message.reply_text(f"Keywords to remove: {', '.join(keywords)}")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()
    context.user_data['next_step'] = None

def set_replace_keywords(update: Update, context: CallbackContext):
    replacements = update.message.text.split(',')
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.replace_keywords = ','.join(replacements)
        session.commit()
        update.message.reply_text(f"Keyword replacements set: {', '.join(replacements)}")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()
    context.user_data['next_step'] = None

def set_blacklist(update: Update, context: CallbackContext):
    blacklist_words = [w.strip() for w in update.message.text.split(',')]
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user:
        user.blacklist = ','.join(blacklist_words)
        session.commit()
        update.message.reply_text(f"Blacklisted words: {', '.join(blacklist_words)}")
    else:
        update.message.reply_text("User not found. Please start the bot with /start command.")
    session.close()
    context.user_data['next_step'] = None

def remove_from_blacklist(update: Update, context: CallbackContext):
    words_to_remove = [w.strip() for w in update.message.text.split(',')]
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if user and user.blacklist:
        current_blacklist = set(user.blacklist.split(','))
        updated_blacklist = current_blacklist - set(words_to_remove)
        user.blacklist = ','.join(updated_blacklist)
        session.commit()
        update.message.reply_text(f"Removed from blacklist: {', '.join(words_to_remove)}")
    else:
        update.message.reply_text("User not found or blacklist is empty.")
    session.close()
    context.user_data['next_step'] = None

