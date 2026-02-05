import secrets, smtplib
from flask import Flask, render_template, request, session
from weather_logic import WeatherFetcher
from email.mime.text import MIMEText
from twilio.rest import Client

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

API_KEY = "1c79708b20d740c097d145309263001"
fetcher = WeatherFetcher(API_KEY)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    history_graph = [] # පසුගිය දින 7 සඳහා
    hourly_labels, hourly_temps = [], []

    if 'history' not in session: session['history'] = []

    if request.method == 'POST':
        city = request.form.get('city')
        weather_data = fetcher.fetch_weather(city)
        
        if weather_data:
            # 1. පසුගිය දින 7ක ඉතිහාසය ලබා ගැනීම
            history_graph = fetcher.fetch_7day_history(city)
            
            # 2. පැය 24ක දත්ත (Chart 1)
            for hour in weather_data['forecast']['forecastday'][0]['hour']:
                hourly_labels.append(hour['time'].split(' ')[1])
                hourly_temps.append(hour['temp_c'])
            
            # 3. Search History Update
            name = weather_data['location']['name']
            if name not in session['history']:
                session['history'] = [name] + session['history'][:4]
                session.modified = True

    return render_template('index.html', data=weather_data, history_list=session['history'], 
                           labels=hourly_labels, temps=hourly_temps, history_graph=history_graph)

if __name__ == '__main__':
    app.run(debug=True)