from telegram import Update
from telegram.ext import CallbackContext
from models.user import User
from services.filter_service import FilterService

filter_service = FilterService()

def remove_keywords(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    if not context.args:
        update.message.reply_text("Please provide keywords to remove, separated by spaces.")
        return
    
    keywords = context.args
    filter_service.set_remove_keywords(user, keywords)
    update.message.reply_text(f"Keywords to remove: {', '.join(keywords)}")

def replace_keywords(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    if not context.args or len(context.args) % 2 != 0:
        update.message.reply_text("Please provide keyword replacements in the format: old_word new_word")
        return
    
    replacements = {context.args[i]: context.args[i+1] for i in range(0, len(context.args), 2)}
    filter_service.set_replace_keywords(user, replacements)
    update.message.reply_text(f"Keyword replacements set: {replacements}")

def remove_replacekeywords(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    filter_service.clear_replace_keywords(user)
    update.message.reply_text("All keyword replacements have been removed.")

def blacklist(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    if not context.args:
        update.message.reply_text("Please provide words to blacklist, separated by spaces.")
        return
    
    words = context.args
    filter_service.add_to_blacklist(user, words)
    update.message.reply_text(f"Words added to blacklist: {', '.join(words)}")

def remove_blacklist(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    if not context.args:
        update.message.reply_text("Please provide words to remove from the blacklist, separated by spaces.")
        return
    
    words = context.args
    filter_service.remove_from_blacklist(user, words)
    update.message.reply_text(f"Words removed from blacklist: {', '.join(words)}")

