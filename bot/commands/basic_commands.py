from telegram import Update
from telegram.ext import CallbackContext
from database.models import User, Session

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    session = Session()
    user = session.query(User).filter_by(telegram_id=user_id).first()
    if not user:
        user = User(telegram_id=user_id)
        session.add(user)
        session.commit()
    update.message.reply_text("Welcome to the Telegram Auto Forwarder Bot! Use /help to see available commands.")
    session.close()

def features(update: Update, context: CallbackContext):
    features_text = """
    Available features:
    - Auto-forwarding from multiple sources
    - Message filtering and text manipulation
    - Scheduling and time-based forwarding
    
    Free plan:
    - 1 incoming channel
    - 1 outgoing channel
    - 100 messages per day limit
    
    Premium plan (100 rupees per month):
    - Up to 5 incoming channels
    - Up to 5 outgoing channels
    - Unlimited messages per day
    - Priority support
    
    To upgrade to premium, use the /upgrade command.
    For more than 5 channels, please contact @Shankar_Kola.
    """
    update.message.reply_text(features_text)

def config(update: Update, context: CallbackContext):
    config_text = """
    Use the following commands to configure the bot:
    
    - /incoming: Set up source channels
    - /remove_incoming: Remove source channels
    - /blacklist: Manage blacklisted words
    - /time_scheduler: Set up forwarding schedule
    - /templates: Manage message templates
    - /filters: Set up advanced filters
    - /translate: Configure translation settings
    - /watermark: Set up media watermarking
    """
    update.message.reply_text(config_text)

def help_command(update: Update, context: CallbackContext):
    help_text = """
    Available commands:
    
    Basic Commands:
    /start - Initialize bot and show welcome message
    /features - Display available features and plans
    /config - Configure bot settings
    /help - Show this help information
    /upgrade - Upgrade to premium plan
    
    Channel Management:
    /incoming - Set up incoming channel(s)
    /outgoing - Set up outgoing channel(s)
    /remove_incoming - Remove incoming channels
    /begin_autoforwarder - Start forwarding process
    /stop - Stop forwarding process
    
    Filter Management:
    /remove_keywords - Set keywords to remove
    /replace_keywords - Set keyword replacements
    /remove_replacekeywords - Remove replacement rules
    /blacklist - Manage blacklisted words
    /remove_blacklist - Remove blacklisted words
    
    Text Modification:
    /begin_text - Set text to add at beginning
    /end_text - Set text to add at end
    /remove_endtext - Remove ending text
    
    Schedule Management:
    /time_scheduler - Manage forwarding schedule
    /remove_slots - Remove scheduled slots
    /disconnect - Disconnect from channels
    /status - Check forwarding status
    
    Additional Advanced Commands:
    /templates - Manage message templates
    /filters - Advanced filtering options
    /analytics - View usage statistics
    /translate - Translation settings
    /watermark - Media watermark settings
    /backup - Backup/restore settings
    /captions - Manage media captions
    """
    update.message.reply_text(help_text)

