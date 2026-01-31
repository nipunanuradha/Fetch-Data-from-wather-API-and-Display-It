import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, session
from weather_logic import WeatherFetcher
from twilio.rest import Client
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Config
API_KEY = "1c79708b20d740c097d145309263001"
# Alerts Config (Replace with your actual credentials)
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
TWILIO_SID = 'your_sid'
TWILIO_TOKEN = 'your_token'
TWILIO_PHONE = 'your_phone'

fetcher = WeatherFetcher(API_KEY)

def send_alerts(city, condition, user_email, user_phone):
    if user_email:
        try:
            msg = MIMEText(f"⚠️ Weather Alert for {city}: {condition}")
            msg['Subject'] = "WeatherPro Alert"
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
        except: pass
    if user_phone:
        try:
            client = Client(TWILIO_SID, TWILIO_TOKEN)
            client.messages.create(body=f"⚠️ Alert: {condition} in {city}", from_=TWILIO_PHONE, to=user_phone)
        except: pass

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    hourly_labels, hourly_temps = [], []
    if 'history' not in session: session['history'] = []

    if request.method == 'POST':
        city = request.form.get('city')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        weather_data = fetcher.fetch_weather(city)
        if weather_data:
            name = weather_data['location']['name']
            if name not in session['history']:
                session['history'] = [name] + session['history'][:4]
                session.modified = True
            
            rain = weather_data['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
            if rain > 70: send_alerts(name, f"High Rain Chance ({rain}%)", email, phone)

            for hour in weather_data['forecast']['forecastday'][0]['hour']:
                hourly_labels.append(hour['time'].split(' ')[1])
                hourly_temps.append(hour['temp_c'])

    return render_template('index.html', data=weather_data, history=session['history'], 
                           labels=hourly_labels, temps=hourly_temps)

if __name__ == '__main__':
    app.run(debug=True)