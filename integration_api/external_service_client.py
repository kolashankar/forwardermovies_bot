import aiohttp
from typing import Dict, Any

class ExternalServiceClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    async def make_request(self, method: str, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{self.base_url}{endpoint}"

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, json=data, headers=headers) as response:
                response.raise_for_status()
                return await response.json()

    async def get_channel_info(self, channel_id: str) -> Dict[str, Any]:
        return await self.make_request("GET", f"/channels/{channel_id}")

    async def send_message(self, channel_id: str, message: str) -> Dict[str, Any]:
        data = {"channel_id": channel_id, "message": message}
        return await self.make_request("POST", "/messages", data)

    async def update_user_status(self, user_id: str, status: str) -> Dict[str, Any]:
        data = {"user_id": user_id, "status": status}
        return await self.make_request("PUT", f"/users/{user_id}/status", data)

    async def get_analytics(self, start_date: str, end_date: str) -> Dict[str, Any]:
        params = {"start_date": start_date, "end_date": end_date}
        return await self.make_request("GET", "/analytics", params)

