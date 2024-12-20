from telegram import Update
from telegram.ext import CallbackContext
from services.message_handler import MessageHandler
from models.user import User

message_handler = MessageHandler()

def handle_message(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    if not user:
        update.message.reply_text("Please start the bot with /start first.")
        return
    
    message = update.message
    
    if message.text:
        handle_text_message(user, message, context)
    elif message.photo:
        handle_photo_message(user, message, context)
    elif message.document:
        handle_document_message(user, message, context)
    else:
        update.message.reply_text("This type of message is not supported.")

def handle_text_message(user, message, context):
    processed_message = message_handler.process_text(user, message.text)
    forward_message(user, processed_message, context)

def handle_photo_message(user, message, context):
    processed_photo = message_handler.process_photo(user, message.photo[-1])
    forward_message(user, processed_photo, context, is_media=True)

def handle_document_message(user, message, context):
    processed_document = message_handler.process_document(user, message.document)
    forward_message(user, processed_document, context, is_media=True)

def forward_message(user, processed_message, context, is_media=False):
    outgoing_channels = user.get_outgoing_channels()
    
    for channel in outgoing_channels:
        try:
            if is_media:
                context.bot.send_photo(chat_id=channel, photo=processed_message.file_id, caption=processed_message.caption)
            else:
                context.bot.send_message(chat_id=channel, text=processed_message)
        except Exception as e:
            print(f"Error forwarding message to {channel}: {str(e)}")

