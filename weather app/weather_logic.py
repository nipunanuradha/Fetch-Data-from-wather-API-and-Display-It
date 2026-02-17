import requests, os
from datetime import datetime, timedelta
from dotenv import load_dotenv

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.forecast_url = "http://api.weatherapi.com/v1/forecast.json"
        self.history_url = "http://api.weatherapi.com/v1/history.json"
        #self.news_api_key = "e1a536d8f3d146fca027ce533789ecb8" 
        self.news_api_key = os.getenv("NEWS_API_KEY")
        self.news_url = "https://newsapi.org/v2/everything"

    def fetch_weather(self, city):
        # Forecast API using for get'astro' data (Sunrise/Sunset) in auto-update
        params = {'key': self.api_key, 'q': city, 'days': 7, 'aqi': 'yes'}
        try:
            response = requests.get(self.forecast_url, params=params)
            return response.json()
        except: return None

    def fetch_7day_history(self, city):
        history_data = []
        for i in range(1, 8):
            date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
            params = {'key': self.api_key, 'q': city, 'dt': date}
            try:
                res = requests.get(self.history_url, params=params).json()
                history_data.append({
                    'date': date[5:], 
                    'temp': res['forecast']['forecastday'][0]['day']['avgtemp_c']
                })
            except: continue
        return history_data[::-1]

    def fetch_weather_news(self):
        params = {
            'q': 'weather AND climate',
            'language': 'en',
            'sortBy': 'publishedAt',
            'apiKey': self.news_api_key
        }
        try:
            response = requests.get(self.news_url, params=params)
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
                news_list = []
                for article in articles[:50]: # Get top 50 articles
                    news_list.append({
                        "title": article.get("title"),
                        "description": article.get("description"),
                        "image": article.get("urlToImage"),
                        "publishedAt": article.get("publishedAt"),
                        "url": article.get("url")
                    })
                return news_list
            return []
        except: return []