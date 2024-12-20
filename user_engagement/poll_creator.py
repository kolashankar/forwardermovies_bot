from telegram import Bot, Poll

class PollCreator:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def create_poll(self, chat_id, question, options, is_anonymous=True, allows_multiple_answers=False):
        poll = await self.bot.send_poll(
            chat_id=chat_id,
            question=question,
            options=options,
            is_anonymous=is_anonymous,
            allows_multiple_answers=allows_multiple_answers
        )
        return poll

    async def close_poll(self, chat_id, message_id):
        await self.bot.stop_poll(chat_id=chat_id, message_id=message_id)

    async def get_poll_results(self, chat_id, message_id):
        message = await self.bot.get_message(chat_id=chat_id, message_id=message_id)
        if message.poll:
            return message.poll.options
        return None

