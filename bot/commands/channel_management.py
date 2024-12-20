from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from database.models import User, Session
from datetime import date

SELECTING_INCOMING, SELECTING_OUTGOING = range(2)

def incoming(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    
    if not user:
        update.message.reply_text("Please start the bot with /start first.")
        return ConversationHandler.END
    
    if not user.is_premium and user.incoming_channels:
        update.message.reply_text("Free users can only have one incoming channel. Upgrade to premium for more!")
        return ConversationHandler.END
    
    args = context.args
    if args:
        channels = [arg for arg in args if arg.startswith('@')]
        if channels:
            return add_incoming_channels(update, context, user, channels)
    
    # If no arguments provided, show inline keyboard
    channels = ["@channel1", "@channel2", "@channel3"]  # Placeholder
    keyboard = [[InlineKeyboardButton(channel, callback_data=f"incoming_{i}")] for i, channel in enumerate(channels)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text("Select incoming channel(s) or use /incoming @channel1 @channel2:", reply_markup=reply_markup)
    return SELECTING_INCOMING

def outgoing(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    
    if not user:
        update.message.reply_text("Please start the bot with /start first.")
        return ConversationHandler.END
    
    if not user.is_premium and user.outgoing_channels:
        update.message.reply_text("Free users can only have one outgoing channel. Upgrade to premium for more!")
        return ConversationHandler.END
    
    args = context.args
    if args:
        channels = [arg for arg in args if arg.startswith('@')]
        if channels:
            return add_outgoing_channels(update, context, user, channels)
    
    # If no arguments provided, show inline keyboard
    channels = ["@group1", "@group2", "@group3"]  # Placeholder
    keyboard = [[InlineKeyboardButton(channel, callback_data=f"outgoing_{i}")] for i, channel in enumerate(channels)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text("Select outgoing channel(s) or use /outgoing @group1 @group2:", reply_markup=reply_markup)
    return SELECTING_OUTGOING

def add_incoming_channels(update: Update, context: CallbackContext, user, channels):
    if user.is_premium:
        current_channels = user.incoming_channels.split(',') if user.incoming_channels else []
        new_channels = [ch for ch in channels if ch not in current_channels]
        if len(current_channels) + len(new_channels) > 5:
            update.message.reply_text("You've reached the maximum number of incoming channels for premium users.")
            return ConversationHandler.END
        
        current_channels.extend(new_channels)
        user.incoming_channels = ','.join(current_channels)
        update.message.reply_text(f"Added {', '.join(new_channels)} to your incoming channels.")
    else:
        user.incoming_channels = channels[0]
        update.message.reply_text(f"Set {channels[0]} as your incoming channel.")
    
    Session().commit()
    return ConversationHandler.END

def add_outgoing_channels(update: Update, context: CallbackContext, user, channels):
    if user.is_premium:
        current_channels = user.outgoing_channels.split(',') if user.outgoing_channels else []
        new_channels = [ch for ch in channels if ch not in current_channels]
        if len(current_channels) + len(new_channels) > 5:
            update.message.reply_text("You've reached the maximum number of outgoing channels for premium users.")
            return ConversationHandler.END
        
        current_channels.extend(new_channels)
        user.outgoing_channels = ','.join(current_channels)
        update.message.reply_text(f"Added {', '.join(new_channels)} to your outgoing channels.")
    else:
        user.outgoing_channels = channels[0]
        update.message.reply_text(f"Set {channels[0]} as your outgoing channel.")
    
    Session().commit()
    return ConversationHandler.END

def handle_incoming_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    
    channel_index = int(query.data.split('_')[1])
    channels = ["@channel1", "@channel2", "@channel3"]  # Placeholder, same as in incoming()
    selected_channel = channels[channel_index]
    
    add_incoming_channels(update, context, user, [selected_channel])
    query.edit_message_text(f"Added {selected_channel} to your incoming channels.")
    
    session.close()
    return ConversationHandler.END

def handle_outgoing_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    
    channel_index = int(query.data.split('_')[1])
    channels = ["@group1", "@group2", "@group3"]  # Placeholder, same as in outgoing()
    selected_channel = channels[channel_index]
    
    add_outgoing_channels(update, context, user, [selected_channel])
    query.edit_message_text(f"Added {selected_channel} to your outgoing channels.")
    
    session.close()
    return ConversationHandler.END

# ... (rest of the file remains the same)

