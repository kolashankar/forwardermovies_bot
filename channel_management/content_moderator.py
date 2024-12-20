import aiohttp
from config.bot_config import bot_config

class ContentModerator:
    def __init__(self):
        self.api_key = bot_config.CONTENT_MODERATOR_API_KEY
        self.endpoint = bot_config.CONTENT_MODERATOR_ENDPOINT

    async def moderate_text(self, text):
        headers = {
            'Content-Type': 'text/plain',
            'Ocp-Apim-Subscription-Key': self.api_key,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.endpoint}/contentmoderator/moderate/v1.0/ProcessText/Screen", headers=headers, data=text) as response:
                result = await response.json()
                return result

    async def moderate_image(self, image_url):
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.api_key,
        }
        data = {'DataRepresentation': 'URL', 'Value': image_url}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.endpoint}/contentmoderator/moderate/v1.0/ProcessImage/Evaluate", headers=headers, json=data) as response:
                result = await response.json()
                return result

    def is_content_safe(self, moderation_result):
        # Implement logic to determine if content is safe based on moderation results
        # This is a simple example and should be adjusted based on your requirements
        if 'Classification' in moderation_result:
            return not (moderation_result['Classification']['IsAdult'] or moderation_result['Classification']['IsRacy'])
        return True

