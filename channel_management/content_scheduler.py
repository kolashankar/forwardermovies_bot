from datetime import datetime, timedelta
from telegram import Bot
import asyncio

class ContentScheduler:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.scheduled_tasks = {}

    async def schedule_message(self, chat_id, message, send_time):
        task = asyncio.create_task(self._send_scheduled_message(chat_id, message, send_time))
        self.scheduled_tasks[id(task)] = task
        task.add_done_callback(lambda t: self.scheduled_tasks.pop(id(t)))

    async def _send_scheduled_message(self, chat_id, message, send_time):
        await asyncio.sleep((send_time - datetime.now()).total_seconds())
        await self.bot.send_message(chat_id=chat_id, text=message)

    def cancel_scheduled_message(self, task_id):
        if task_id in self.scheduled_tasks:
            self.scheduled_tasks[task_id].cancel()
            del self.scheduled_tasks[task_id]
            return True
        return False

    def get_scheduled_messages(self):
        return [{'task_id': task_id, 'task': task} for task_id, task in self.scheduled_tasks.items()]

