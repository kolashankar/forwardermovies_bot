from telegram import Bot
from models.forwarding_task import ForwardingTask
from models.forwarding_stats import ForwardingStats
from services.filter_service import FilterService
from services.text_service import TextService

class MessageForwarder:
    def __init__(self, bot: Bot, filter_service: FilterService, text_service: TextService):
        self.bot = bot
        self.filter_service = filter_service
        self.text_service = text_service

    async def forward_message(self, task: ForwardingTask, message):
        if not self.filter_service.should_forward(task, message):
            return

        modified_message = self.text_service.modify_message(task, message)
        
        try:
            await self.bot.send_message(
                chat_id=task.destination_channel,
                text=modified_message.text,
                parse_mode=modified_message.parse_mode,
                disable_web_page_preview=modified_message.disable_web_page_preview
            )
            
            self.update_forwarding_stats(task.user_id)
        except Exception as e:
            print(f"Error forwarding message: {str(e)}")

    def update_forwarding_stats(self, user_id):
        stats = ForwardingStats.get_or_create(user_id)
        stats.increment_forwarded_count()

    async def forward_media(self, task: ForwardingTask, message):
        if not self.filter_service.should_forward(task, message):
            return

        modified_caption = self.text_service.modify_caption(task, message.caption)

        try:
            if message.photo:
                await self.bot.send_photo(
                    chat_id=task.destination_channel,
                    photo=message.photo[-1].file_id,
                    caption=modified_caption
                )
            elif message.video:
                await self.bot.send_video(
                    chat_id=task.destination_channel,
                    video=message.video.file_id,
                    caption=modified_caption
                )
            elif message.document:
                await self.bot.send_document(
                    chat_id=task.destination_channel,
                    document=message.document.file_id,
                    caption=modified_caption
                )
            
            self.update_forwarding_stats(task.user_id)
        except Exception as e:
            print(f"Error forwarding media: {str(e)}")

