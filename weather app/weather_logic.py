import requests

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        # current.json වෙනුවට forecast.json භාවිතා කරයි
        self.base_url = "http://api.weatherapi.com/v1/forecast.json"

    def fetch_weather(self, city, days=3):
        params = {
            'key': self.api_key, 
            'q': city, 
            'days': days,  # දින 3ක දත්ත ඉල්ලයි
            'aqi': 'no'
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None