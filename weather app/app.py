from flask import Flask, render_template, request
from weather_logic import WeatherFetcher

app = Flask(__name__)
#  API Key 
fetcher = WeatherFetcher("1c79708b20d740c097d145309263001")

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = fetcher.fetch_weather(city)
    
    return render_template('index.html', data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)