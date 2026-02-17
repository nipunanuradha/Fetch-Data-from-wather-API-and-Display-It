import secrets, smtplib, os
from flask import Flask, render_template, request, session, send_from_directory
from weather_logic import WeatherFetcher
from email.mime.text import MIMEText
from twilio.rest import Client
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", secrets.token_hex(16))

API_KEY = os.getenv("WEATHER_API_KEY")
fetcher = WeatherFetcher(API_KEY)

# Alerts Config
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")    
TW_SID = os.getenv("TW_SID")
TW_TOKEN = os.getenv("TW_TOKEN")
TW_PHONE = os.getenv("TW_PHONE")

# PWA service Routes
@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory('static', 'sw.js')

def trigger_alerts(city, rain_chance, user_email, user_phone):
    if rain_chance > 70:
        msg = f"⚠️ Alert: High Rain Chance ({rain_chance}%) in {city}!"
        if user_email:
            try:
                mail = MIMEText(msg); mail['Subject'] = "Weather Alert"; mail['From'] = EMAIL_ADDR; mail['To'] = user_email
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s: s.login(EMAIL_ADDR, EMAIL_PASS); s.send_message(mail)
            except: pass
        if user_phone:
            try: Client(TW_SID, TW_TOKEN).messages.create(body=msg, from_=TW_PHONE, to=user_phone)
            except: pass

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data, weather_data2 = None, None
    history_graph = []
    h_labels, h_temps = [], []
    news_articles = fetcher.fetch_weather_news()
    
    if 'history' not in session: session['history'] = []

    if request.method == 'POST':
        city = request.form.get('city')
        city2 = request.form.get('city2') # Second city input for comparison
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        weather_data = fetcher.fetch_weather(city)
        if city2:
            weather_data2 = fetcher.fetch_weather(city2) # Get weather for second city if provided

        if weather_data:
            history_graph = fetcher.fetch_7day_history(city)
            trigger_alerts(city, weather_data['forecast']['forecastday'][0]['day']['daily_chance_of_rain'], email, phone)
            
            for hour in weather_data['forecast']['forecastday'][0]['hour']:
                h_labels.append(hour['time'].split(' ')[1])
                h_temps.append(hour['temp_c'])
            
            name = weather_data['location']['name']
            if name not in session['history']:
                session['history'] = [name] + session['history'][:4]
                session.modified = True

    return render_template('index.html', data=weather_data, data2=weather_data2, 
                           history_list=session['history'], labels=h_labels, 
                           temps=h_temps, history_graph=history_graph, news=news_articles)

if __name__ == '__main__':
    app.run(debug=True)