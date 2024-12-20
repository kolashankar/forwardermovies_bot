from telegram.error import BadRequest

class ChannelValidator:
    def __init__(self, bot):
        self.bot = bot

    async def validate_channel(self, channel_id):
        try:
            chat = await self.bot.get_chat(channel_id)
            return True, chat.title
        except BadRequest as e:
            if "Chat not found" in str(e):
                return False, "Channel not found"
            elif "Not enough rights" in str(e):
                return False, "Bot doesn't have necessary permissions"
            else:
                return False, str(e)

    async def validate_user_in_channel(self, user_id, channel_id):
        try:
            member = await self.bot.get_chat_member(channel_id, user_id)
            return member.status in ['creator', 'administrator', 'member']
        except BadRequest:
            return False

    async def validate_bot_permissions(self, channel_id):
        try:
            bot_member = await self.bot.get_chat_member(channel_id, self.bot.id)
            return (
                bot_member.can_post_messages and
                bot_member.can_edit_messages and
                bot_member.can_delete_messages
            )
        except BadRequest:
            return False

