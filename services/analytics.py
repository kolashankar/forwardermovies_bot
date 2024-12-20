import requests
from config.settings import Settings

class AnalyticsService:
    def __init__(self):
        self.settings = Settings()
        self.enabled = self.settings.ENABLE_ANALYTICS
        self.token = self.settings.ANALYTICS_TOKEN
        self.base_url = "https://api.analytics-provider.com/v1"  # Replace with actual analytics API URL

    def track_event(self, event_name, user_id, properties=None):
        if not self.enabled:
            return

        data = {
            "event": event_name,
            "user_id": user_id,
            "properties": properties or {}
        }

        try:
            response = requests.post(
                f"{self.base_url}/track",
                json=data,
                headers={"Authorization": f"Bearer {self.token}"}
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error tracking analytics event: {str(e)}")

    def get_user_stats(self, user_id):
        if not self.enabled:
            return None

        try:
            response = requests.get(
                f"{self.base_url}/users/{user_id}/stats",
                headers={"Authorization": f"Bearer {self.token}"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching user stats: {str(e)}")
            return None

analytics_service = AnalyticsService()

