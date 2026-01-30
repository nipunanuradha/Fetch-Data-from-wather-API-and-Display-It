from flask import Flask, render_template, request, session
from weather_logic import WeatherFetcher
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# ඔයාගේ API Key එක මෙතනට දාන්න
fetcher = WeatherFetcher("1c79708b20d740c097d145309263001")

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    hourly_labels = []
    hourly_temps = []
    
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = fetcher.fetch_weather(city)
            if weather_data:
                city_name = weather_data['location']['name']
                # History එක update කිරීම
                if city_name not in session['history']:
                    new_history = [city_name] + session['history']
                    session['history'] = new_history[:5]
                    session.modified = True
                
                # Chart දත්ත
                for hour in weather_data['forecast']['forecastday'][0]['hour']:
                    hourly_labels.append(hour['time'].split(' ')[1])
                    hourly_temps.append(hour['temp_c'])

    return render_template('index.html', 
                           data=weather_data, 
                           history=session['history'],
                           labels=hourly_labels, 
                           temps=hourly_temps)

if __name__ == '__main__':
    app.run(debug=True)