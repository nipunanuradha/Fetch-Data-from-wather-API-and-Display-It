import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, session
from weather_logic import WeatherFetcher
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Config
API_KEY = "1c79708b20d740c097d145309263001"
EMAIL_ADDRESS = "kasunlankalk48@gmail.com" # sender email
EMAIL_PASSWORD = "qzvi vdxx rymg faqz" # sender email app password
fetcher = WeatherFetcher(API_KEY)

def send_alert_email(city, condition, user_email):
    msg = MIMEText(f"⚠️ WEATHER ALERT: Bad weather detected in {city}.\n\nDetail: {condition}\nStay safe!")
    msg['Subject'] = f"Alert: {city} Weather"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = user_email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return True
    except: return False

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    hourly_labels, hourly_temps = [], []
    alert_status = False

    if 'history' not in session: session['history'] = []

    if request.method == 'POST':
        city = request.form.get('city')
        user_email = request.form.get('email')
        
        weather_data = fetcher.fetch_weather(city)
        if weather_data:
            # History logic
            c_name = weather_data['location']['name']
            if c_name not in session['history']:
                session['history'] = [c_name] + session['history'][:4]
                session.modified = True

            # Rain Alert (Email)
            rain_chance = weather_data['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
            if rain_chance > 70 and user_email:
                send_alert_email(city, f"High chance of rain: {rain_chance}%", user_email)
                alert_status = True

            # Hourly Chart Data
            for hour in weather_data['forecast']['forecastday'][0]['hour']:
                hourly_labels.append(hour['time'].split(' ')[1])
                hourly_temps.append(hour['temp_c'])

    return render_template('index.html', data=weather_data, history=session['history'], 
                           labels=hourly_labels, temps=hourly_temps, alert=alert_status)

if __name__ == '__main__':
    app.run(debug=True)