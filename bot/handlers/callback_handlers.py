from telegram import Update
from telegram.ext import CallbackContext
from models.user import User
from services.subscription_manager import SubscriptionManager

subscription_manager = SubscriptionManager()

def handle_callback_query(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    data = query.data.split('_')
    action = data[0]
    
    if action == 'upgrade':
        handle_upgrade(update, context)
    elif action == 'channel':
        handle_channel_selection(update, context, data[1], data[2])
    else:
        query.edit_message_text(text="Invalid callback query.")

def handle_upgrade(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    if subscription_manager.upgrade_to_premium(user):
        text = "You've successfully upgraded to the premium plan!"
    else:
        text = "There was an error upgrading your plan. Please try again later or contact support."
    
    update.callback_query.edit_message_text(text=text)

def handle_channel_selection(update: Update, context: CallbackContext, channel_type, channel_id):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    if channel_type == 'incoming':
        success = user.add_incoming_channel(channel_id)
    elif channel_type == 'outgoing':
        success = user.add_outgoing_channel(channel_id)
    else:
        success = False
    
    if success:
        text = f"Successfully added {channel_id} to your {channel_type} channels."
    else:
        text = f"Failed to add {channel_id} to your {channel_type} channels. Please try again or contact support."
    
    update.callback_query.edit_message_text(text=text)

