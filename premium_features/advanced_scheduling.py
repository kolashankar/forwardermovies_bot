from utils.decorators import premium_required
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from datetime import datetime, timedelta

SELECTING_CHANNEL, SELECTING_TIME, SELECTING_FREQUENCY, CONFIRMING = range(4)

class AdvancedScheduling:
    def __init__(self):
        self.scheduled_tasks = {}

    @premium_required
    async def start_scheduling(self, update: Update, context: CallbackContext):
        user_channels = self.get_user_channels(update.effective_user.id)
        keyboard = [[InlineKeyboardButton(channel, callback_data=f"channel_{channel}")] for channel in user_channels]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Select a channel to schedule content for:", reply_markup=reply_markup)
        return SELECTING_CHANNEL

    async def channel_selected(self, update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        context.user_data['selected_channel'] = query.data.split('_')[1]
        await query.edit_message_text("Select the time for scheduling:")
        return SELECTING_TIME

    async def time_selected(self, update: Update, context: CallbackContext):
        context.user_data['selected_time'] = update.message.text
        keyboard = [
            [InlineKeyboardButton("Daily", callback_data="freq_daily")],
            [InlineKeyboardButton("Weekly", callback_data="freq_weekly")],
            [InlineKeyboardButton("Monthly", callback_data="freq_monthly")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Select the frequency of scheduling:", reply_markup=reply_markup)
        return SELECTING_FREQUENCY

    async def frequency_selected(self, update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        context.user_data['selected_frequency'] = query.data.split('_')[1]
        await query.edit_message_text(f"You've selected to schedule content for {context.user_data['selected_channel']} "
                                      f"at {context.user_data['selected_time']} {context.user_data['selected_frequency']}. "
                                      f"Is this correct?")
        keyboard = [
            [InlineKeyboardButton("Yes", callback_data="confirm_yes")],
            [InlineKeyboardButton("No", callback_data="confirm_no")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Confirm your selection:", reply_markup=reply_markup)
        return CONFIRMING

    async def confirm_scheduling(self, update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        if query.data == "confirm_yes":
            self.schedule_task(context.user_data)
            await query.edit_message_text("Your content has been scheduled successfully!")
        else:
            await query.edit_message_text("Scheduling cancelled. You can start over with /schedule_content")
        return ConversationHandler.END

    def schedule_task(self, user_data):
        task_id = f"{user_data['selected_channel']}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.scheduled_tasks[task_id] = user_data
        # Here you would typically set up a job in your task scheduler (e.g., APScheduler)

    def get_user_channels(self, user_id):
        # Placeholder: Replace with actual logic to get user's channels
        return ["Channel A", "Channel B", "Channel C"]

    @premium_required
    async def view_scheduled_tasks(self, update: Update, context: CallbackContext):
        if not self.scheduled_tasks:
            await update.message.reply_text("You have no scheduled tasks.")
            return

        task_list = "Your scheduled tasks:\n\n"
        for task_id, task_data in self.scheduled_tasks.items():
            task_list += f"ID: {task_id}\n"
            task_list += f"Channel: {task_data['selected_channel']}\n"
            task_list += f"Time: {task_data['selected_time']}\n"
            task_list += f"Frequency: {task_data['selected_frequency']}\n\n"

        await update.message.reply_text(task_list)

    @premium_required
    async def cancel_scheduled_task(self, update: Update, context: CallbackContext):
        if not context.args:
            await update.message.reply_text("Please provide the task ID to cancel.")
            return

        task_id = context.args[0]
        if task_id in self.scheduled_tasks:
            del self.scheduled_tasks[task_id]
            # Here you would typically remove the job from your task scheduler
            await update.message.reply_text(f"Task {task_id} has been cancelled.")
        else:
            await update.message.reply_text(f"Task {task_id} not found.")

