import requests
from datetime import datetime, timedelta

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.forecast_url = "http://api.weatherapi.com/v1/forecast.json"
        self.history_url = "http://api.weatherapi.com/v1/history.json"
        # News ලබා ගැනීමට NewsAPI (නොමිලේ ලබාගත හැක) හෝ මෙහි පෙන්වා ඇති පරිදි ලබා ගත හැක
        self.news_url = "https://gnews.io/api/v4/search?q=weather&token=YOUR_GNEWS_API_KEY&lang=en"

    def fetch_weather(self, city):
        params = {'key': self.api_key, 'q': city, 'days': 5, 'aqi': 'yes'}
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
        # සාම්පල පුවත් දත්ත (සැබෑ API එකක් සම්බන්ධ කරන තෙක්)
        # ඔබ සතුව GNews හෝ NewsAPI key එකක් තිබේ නම් ඉහත URL එක භාවිතා කරන්න.
        try:
            # මෙහිදී අපි සරල නිදසුනක් පෙන්වමු
            news_data = [
                {
                    "title": "Global Warming: 2026 Set to be Warmest Year",
                    "description": "Climate scientists warn of rising temperatures globally.",
                    "image": "https://images.unsplash.com/photo-1564314968303-86c5ad2b9a4c?auto=format&fit=crop&w=400",
                    "publishedAt": "2026-02-05T10:00:00Z",
                    "url": "https://example.com/news1"
                },
                {
                    "title": "Severe Storms Predicted for South Asia",
                    "description": "Monsoon patterns are shifting earlier than expected this year.",
                    "image": "https://images.unsplash.com/photo-1527482797697-8795b05a13fe?auto=format&fit=crop&w=400",
                    "publishedAt": "2026-02-05T09:30:00Z",
                    "url": "https://example.com/news2"
                }
            ]
            return news_data
        except: return []