from typing import List, Dict, Any
from .external_service_client import ExternalServiceClient

class IntegrationManager:
    def __init__(self):
        self.integrations: Dict[str, ExternalServiceClient] = {}

    def add_integration(self, name: str, base_url: str, api_key: str):
        self.integrations[name] = ExternalServiceClient(base_url, api_key)

    def remove_integration(self, name: str):
        if name in self.integrations:
            del self.integrations[name]

    async def broadcast_message(self, message: str, channels: List[str]):
        results = []
        for integration_name, client in self.integrations.items():
            for channel in channels:
                try:
                    result = await client.send_message(channel, message)
                    results.append({
                        "integration": integration_name,
                        "channel": channel,
                        "status": "success",
                        "result": result
                    })
                except Exception as e:
                    results.append({
                        "integration": integration_name,
                        "channel": channel,
                        "status": "error",
                        "error": str(e)
                    })
        return results

    async def get_channel_info_all(self, channel_id: str) -> Dict[str, Any]:
        results = {}
        for integration_name, client in self.integrations.items():
            try:
                result = await client.get_channel_info(channel_id)
                results[integration_name] = {
                    "status": "success",
                    "info": result
                }
            except Exception as e:
                results[integration_name] = {
                    "status": "error",
                    "error": str(e)
                }
        return results

    async def update_user_status_all(self, user_id: str, status: str) -> Dict[str, Any]:
        results = {}
        for integration_name, client in self.integrations.items():
            try:
                result = await client.update_user_status(user_id, status)
                results[integration_name] = {
                    "status": "success",
                    "result": result
                }
            except Exception as e:
                results[integration_name] = {
                    "status": "error",
                    "error": str(e)
                }
        return results

    async def get_analytics_all(self, start_date: str, end_date: str) -> Dict[str, Any]:
        results = {}
        for integration_name, client in self.integrations.items():
            try:
                result = await client.get_analytics(start_date, end_date)
                results[integration_name] = {
                    "status": "success",
                    "analytics": result
                }
            except Exception as e:
                results[integration_name] = {
                    "status": "error",
                    "error": str(e)
                }
        return results

