import aiohttp
from config.settings import Settings

class TelegramAPI:
    def __init__(self):
        self.settings = Settings()
        self.base_url = f"https://api.telegram.org/bot{self.settings.BOT_TOKEN}"

    async def send_message(self, chat_id, text, parse_mode=None, reply_markup=None):
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "reply_markup": reply_markup
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                return await response.json()

    async def forward_message(self, chat_id, from_chat_id, message_id):
        url = f"{self.base_url}/forwardMessage"
        payload = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                return await response.json()

    async def get_chat(self, chat_id):
        url = f"{self.base_url}/getChat"
        payload = {
            "chat_id": chat_id
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                return await response.json()

    async def get_chat_member(self, chat_id, user_id):
        url = f"{self.base_url}/getChatMember"
        payload = {
            "chat_id": chat_id,
            "user_id": user_id
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                return await response.json()

telegram_api = TelegramAPI()

