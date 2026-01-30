from flask import Flask, render_template, request, session
from weather_logic import WeatherFetcher
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16) # Sneed secret key for session management

fetcher = WeatherFetcher("1c79708b20d740c097d145309263001")

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    hourly_labels = []
    hourly_temps = []
    
    # initialize search history in session
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = fetcher.fetch_weather(city)
            
            if weather_data:
                #  Search History 
                city_name = weather_data['location']['name']
                if city_name not in session['history']:
                    # maintain only last 5 searches
                    new_history = [city_name] + session['history']
                    session['history'] = new_history[:5]
                    session.modified = True
                
                # 2. get data for hourly chart
                # first day's hourly data in 24 hours
                for hour in weather_data['forecast']['forecastday'][0]['hour']:
                    # show the time in HH:MM format
                    time_label = hour['time'].split(' ')[1]
                    hourly_labels.append(time_label)
                    hourly_temps.append(hour['temp_c'])

    return render_template('index.html', 
                           data=weather_data, 
                           history=session['history'],
                           labels=hourly_labels, 
                           temps=hourly_temps)

if __name__ == '__main__':
    app.run(debug=True)