import requests
from datetime import datetime, timedelta

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.forecast_url = "http://api.weatherapi.com/v1/forecast.json"
        self.history_url = "http://api.weatherapi.com/v1/history.json"
        # News ලබා ගැනීමට NewsAPI (නොමිලේ ලබාගත හැක) හෝ මෙහි පෙන්වා ඇති පරිදි ලබා ගත හැක
        self.news_api_key = "de583baf345141545d4711727b8073cb" 
        self.news_url = f"https://gnews.io/api/v4/search?q=weather&token={self.news_api_key}&lang=en"

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
            response = requests.get(self.news_url)
            if response.status_code == 200:
                data = response.json()
                # GNews API එකේ පුවත් එන්නේ 'articles' කියන key එක යටතේ
                articles = data.get('articles', [])
                
                news_list = []
                for article in articles:
                    news_list.append({
                        "title": article.get("title"),
                        "description": article.get("description"),
                        "image": article.get("image"), # GNews වල image URL එක එන්නේ 'image' නමින්
                        "publishedAt": article.get("publishedAt"),
                        "url": article.get("url")
                    })
                return news_list
            else:
                print(f"Error fetching news: {response.status_code}")
                return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []