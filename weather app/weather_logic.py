import requests

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.weatherapi.com/v1/forecast.json"

    def fetch_weather(self, city):
        # දින 5ක දත්ත සහ AQI දත්ත ලබා ගැනීමට පරාමිතීන් සකසයි
        params = {
            'key': self.api_key, 
            'q': city, 
            'days': 5, 
            'aqi': 'yes'
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Logic Error: {e}")
            return None