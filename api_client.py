import requests
import logging

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self, limit=5000):
        try:
            url = f"{self.base_url}?$limit={limit}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            return None
