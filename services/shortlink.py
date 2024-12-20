import aiohttp
from config.settings import Settings

class ShortlinkService:
    def __init__(self):
        self.settings = Settings()
        self.api_url = self.settings.SHORTLINK_URL
        self.api_key = self.settings.SHORTLINK_API

    async def create_short_link(self, long_url):
        if not self.settings.ENABLE_SHORTLINKS:
            return long_url

        async with aiohttp.ClientSession() as session:
            params = {
                'api': self.api_key,
                'url': long_url
            }
            try:
                async with session.get(self.api_url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get('shorturl', long_url)
                    else:
                        print(f"Error creating shortlink: {response.status}")
                        return long_url
            except Exception as e:
                print(f"Exception while creating shortlink: {str(e)}")
                return long_url

