from telegram import Update
from telegram.ext import CallbackContext
from models.user import User
from services.scheduler_service import SchedulerService
from bot.core import TelegramForwarderBot  # Import your bot class

bot = TelegramForwarderBot()  # Create an instance of your bot

scheduler_service = SchedulerService(bot)  # Pass the bot instance

def time_scheduler(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    if not context.args:
        update.message.reply_text("Please provide the forwarding schedule in the format: HH:MM-HH:MM, separated by commas.")
        return
    
    schedule = context.args[0].split(',')
    scheduler_service.set_schedule(user, schedule)
    update.message.reply_text(f"Forwarding schedule set to: {', '.join(schedule)}")

def remove_slots(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    scheduler_service.clear_schedule(user)
    update.message.reply_text("All scheduled slots have been removed.")

def disconnect(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    user.clear_channels()
    scheduler_service.clear_schedule(user)
    update.message.reply_text("Disconnected from all channels and cleared the schedule.")

def status(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = User.get_by_id(user_id)
    
    incoming_channels = user.get_incoming_channels()
    outgoing_channels = user.get_outgoing_channels()
    schedule = scheduler_service.get_schedule(user)
    
    status_text = f"""
    Current Status:
    Incoming Channels: {', '.join(incoming_channels) if incoming_channels else 'None'}
    Outgoing Channels: {', '.join(outgoing_channels) if outgoing_channels else 'None'}
    Schedule: {', '.join(schedule) if schedule else 'Not set'}
    Premium: {'Yes' if user.is_premium else 'No'}
    """
    
    update.message.reply_text(status_text)
