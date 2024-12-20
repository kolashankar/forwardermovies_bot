import aiohttp
from models import ShortlinkProvider
from database import get_db

class ShortlinkService:
    async def create_shortlink(self, user_id, long_url):
        db = next(get_db())
        provider = db.query(ShortlinkProvider).filter(ShortlinkProvider.user_id == user_id).first()
        
        if not provider:
            return None, "No shortlink provider configured"

        async with aiohttp.ClientSession() as session:
            params = {
                "api": provider.api_key,
                "url": long_url
            }
            async with session.get(provider.api_url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("shortlink"), None
                else:
                    return None, f"Error: {response.status}"

    async def add_shortlink_provider(self, user_id, provider_name, api_key, api_url):
        db = next(get_db())
        provider = ShortlinkProvider(
            user_id=user_id,
            provider_name=provider_name,
            api_key=api_key,
            api_url=api_url
        )
        db.add(provider)
        db.commit()
        return provider

