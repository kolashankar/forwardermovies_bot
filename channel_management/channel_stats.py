from telegram import Bot
from datetime import datetime, timedelta

class ChannelStats:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def get_member_count(self, channel_id):
        chat = await self.bot.get_chat(channel_id)
        return chat.get_member_count()

    async def get_message_count(self, channel_id, days=7):
        chat = await self.bot.get_chat(channel_id)
        messages = 0
        async for message in chat.iter_messages(limit=None, offset_date=datetime.now() - timedelta(days=days)):
            messages += 1
        return messages

    async def get_active_users(self, channel_id, days=7):
        chat = await self.bot.get_chat(channel_id)
        active_users = set()
        async for message in chat.iter_messages(limit=None, offset_date=datetime.now() - timedelta(days=days)):
            active_users.add(message.from_user.id)
        return len(active_users)

    async def get_channel_info(self, channel_id):
        chat = await self.bot.get_chat(channel_id)
        return {
            'id': chat.id,
            'title': chat.title,
            'username': chat.username,
            'description': chat.description,
            'invite_link': chat.invite_link,
            'member_count': await self.get_member_count(channel_id)
        }

