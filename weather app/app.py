import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, session
from weather_logic import WeatherFetcher
from twilio.rest import Client # SMS සඳහා
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Configurations
API_KEY = "1c79708b20d740c097d145309263001"
# Email Config
EMAIL_ADDRESS = "kasunlankalk48@gmail.com"
EMAIL_PASSWORD = "qzvi vdxx rymg faqz"
# Twilio SMS Config (Twilio එකෙන් මේවා ලබාගත හැක)
TWILIO_SID = 'ACf81c209ddf4f06a370dc2da7d6c57b83'
TWILIO_AUTH_TOKEN = 'db90280d3681067210e1e31185605f6e'
TWILIO_PHONE = '+18777804236'

fetcher = WeatherFetcher(API_KEY)

def send_alerts(city, condition, user_email, user_phone):
    # 1. Email Alert
    if user_email:
        try:
            msg = MIMEText(f"⚠️ WEATHER ALERT: {condition} in {city}. Stay safe!")
            msg['Subject'] = f"Weather Alert: {city}"
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = user_email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
        except Exception as e: print(f"Email Error: {e}")

    # 2. SMS Alert (Twilio)
    if user_phone:
        try:
            client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
            client.messages.create(
                body=f"⚠️ WeatherPro Alert: {condition} detected in {city}!",
                from_=TWILIO_PHONE,
                to=user_phone
            )
        except Exception as e: print(f"SMS Error: {e}")

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
            c_name = weather_data['location']['name']
            if c_name not in session['history']:
                session['history'] = [c_name] + session['history'][:4]
                session.modified = True

            # නරක කාලගුණය පරීක්ෂා කිරීම (වැස්ස > 70%)
            rain_chance = weather_data['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
            if rain_chance > 70:
                send_alerts(city, f"High rain chance ({rain_chance}%)", email, phone)

            for hour in weather_data['forecast']['forecastday'][0]['hour']:
                hourly_labels.append(hour['time'].split(' ')[1])
                hourly_temps.append(hour['temp_c'])

    return render_template('index.html', data=weather_data, history=session['history'], 
                           labels=hourly_labels, temps=hourly_temps)

if __name__ == '__main__':
    app.run(debug=True)