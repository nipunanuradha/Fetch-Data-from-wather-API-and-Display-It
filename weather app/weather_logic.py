import requests
from datetime import datetime, timedelta

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.forecast_url = "http://api.weatherapi.com/v1/forecast.json"
        self.history_url = "http://api.weatherapi.com/v1/history.json"

    def fetch_weather(self, city):
        params = {'key': self.api_key, 'q': city, 'days': 5, 'aqi': 'yes'}
        try:
            response = requests.get(self.forecast_url, params=params)
            return response.json()
        except: return None

    def fetch_7day_history(self, city):
        history_data = []
        # අද සිට ආපස්සට දින 7ක දත්ත ලබා ගැනීම
        for i in range(1, 8):
            date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
            params = {'key': self.api_key, 'q': city, 'dt': date}
            try:
                res = requests.get(self.history_url, params=params).json()
                history_data.append({
                    'date': date[5:], # MM-DD පමණක් ගනිමු
                    'temp': res['forecast']['forecastday'][0]['day']['avgtemp_c']
                })
            except: continue
        return history_data[::-1] # දත්ත පිළිවෙළට සකසයි