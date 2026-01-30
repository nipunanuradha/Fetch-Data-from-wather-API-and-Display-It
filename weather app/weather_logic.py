import requests

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        # used forecast.json endpoint for multi-day forecast
        self.base_url = "http://api.weatherapi.com/v1/forecast.json"

    def fetch_weather(self, city, days=3):
        params = {
            'key': self.api_key, 
            'q': city, 
            'days': days,  # reqyuesting forecast for 3 days
            'aqi': 'no'
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None