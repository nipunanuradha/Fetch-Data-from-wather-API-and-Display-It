"""
Weather Fetcher - Working Demo Version
test demo version 
using Real API structure 
"""

import json
from datetime import datetime

# Simulated weather database (Real cities සහ realistic data)
WEATHER_DATABASE = {
    'colombo': {
        'name': 'Colombo',
        'sys': {'country': 'LK'},
        'coord': {'lon': 79.85, 'lat': 6.93},
        'main': {
            'temp': 28.5,
            'feels_like': 32.1,
            'temp_min': 26.8,
            'temp_max': 30.2,
            'humidity': 78,
            'pressure': 1010
        },
        'weather': [{'main': 'Clouds', 'description': 'partly cloudy', 'icon': '02d'}],
        'wind': {'speed': 4.5, 'deg': 220},
        'clouds': {'all': 40},
        'visibility': 10000
    },
    'kandy': {
        'name': 'Kandy',
        'sys': {'country': 'LK'},
        'coord': {'lon': 80.63, 'lat': 7.29},
        'main': {
            'temp': 24.3,
            'feels_like': 25.8,
            'temp_min': 22.1,
            'temp_max': 26.5,
            'humidity': 82,
            'pressure': 1012
        },
        'weather': [{'main': 'Rain', 'description': 'light rain', 'icon': '10d'}],
        'wind': {'speed': 3.2, 'deg': 180},
        'clouds': {'all': 75},
        'visibility': 8000
    },
    'galle': {
        'name': 'Galle',
        'sys': {'country': 'LK'},
        'coord': {'lon': 80.22, 'lat': 6.03},
        'main': {
            'temp': 27.8,
            'feels_like': 30.5,
            'temp_min': 26.2,
            'temp_max': 29.1,
            'humidity': 75,
            'pressure': 1009
        },
        'weather': [{'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
        'wind': {'speed': 5.8, 'deg': 240},
        'clouds': {'all': 10},
        'visibility': 10000
    },
    'kurunegala': {
        'name': 'Kurunegala',
        'sys': {'country': 'LK'},
        'coord': {'lon': 80.37, 'lat': 7.49},
        'main': {
            'temp': 26.5,
            'feels_like': 29.2,
            'temp_min': 24.8,
            'temp_max': 28.3,
            'humidity': 80,
            'pressure': 1011
        },
        'weather': [{'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}],
        'wind': {'speed': 4.1, 'deg': 200},
        'clouds': {'all': 50},
        'visibility': 9500
    },
    'london': {
        'name': 'London',
        'sys': {'country': 'GB'},
        'coord': {'lon': -0.13, 'lat': 51.51},
        'main': {
            'temp': 8.2,
            'feels_like': 5.1,
            'temp_min': 6.5,
            'temp_max': 9.8,
            'humidity': 81,
            'pressure': 1015
        },
        'weather': [{'main': 'Drizzle', 'description': 'light drizzle', 'icon': '09d'}],
        'wind': {'speed': 6.7, 'deg': 270},
        'clouds': {'all': 90},
        'visibility': 7000
    },
    'new york': {
        'name': 'New York',
        'sys': {'country': 'US'},
        'coord': {'lon': -74.01, 'lat': 40.71},
        'main': {
            'temp': 5.3,
            'feels_like': 1.2,
            'temp_min': 3.1,
            'temp_max': 7.5,
            'humidity': 65,
            'pressure': 1018
        },
        'weather': [{'main': 'Snow', 'description': 'light snow', 'icon': '13d'}],
        'wind': {'speed': 8.2, 'deg': 320},
        'clouds': {'all': 85},
        'visibility': 5000
    },
    'tokyo': {
        'name': 'Tokyo',
        'sys': {'country': 'JP'},
        'coord': {'lon': 139.69, 'lat': 35.69},
        'main': {
            'temp': 12.5,
            'feels_like': 11.2,
            'temp_min': 10.3,
            'temp_max': 14.8,
            'humidity': 55,
            'pressure': 1020
        },
        'weather': [{'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
        'wind': {'speed': 3.5, 'deg': 150},
        'clouds': {'all': 5},
        'visibility': 10000
    },
    'dubai': {
        'name': 'Dubai',
        'sys': {'country': 'AE'},
        'coord': {'lon': 55.30, 'lat': 25.26},
        'main': {
            'temp': 23.8,
            'feels_like': 23.1,
            'temp_min': 21.5,
            'temp_max': 25.2,
            'humidity': 42,
            'pressure': 1014
        },
        'weather': [{'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
        'wind': {'speed': 4.2, 'deg': 310},
        'clouds': {'all': 0},
        'visibility': 10000
    }
}


class WeatherFetcherDemo:
    """
    Demo Weather Fetcher Class
    Real API structure and  demo version 
    """
    
    def __init__(self):
        self.database = WEATHER_DATABASE
    
    def fetch_weather(self, city):
        """
        Simulate API call - data fetching from local database
        
        Args:
            city (str): City name
            
        Returns:
            dict: Weather data or None
        """
        city_key = city.lower().strip()
        
        print(f"\n🌍 {city}  weather data fetching ...")
        print("📡 API call simulating...")
        
        # Simulate network delay
        import time
        time.sleep(0.5)
        
        if city_key in self.database:
            print("✅ Data received successfully!")
            return self.database[city_key]
        else:
            print(f"❌ Error: '{city}' This city data not found in database.")
            return None
    
    def display_weather(self, data):
        """
        Weather data display using user-friendly format
        """
        if not data:
            return
        
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        weather_desc = data['weather'][0]['description'].title()
        weather_main = data['weather'][0]['main']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        clouds = data['clouds']['all']
        visibility = data['visibility'] / 1000  # Convert to km
        
        # Weather emoji select 
        weather_emoji = {
            'Clear': '☀️',
            'Clouds': '☁️',
            'Rain': '🌧️',
            'Drizzle': '🌦️',
            'Snow': '❄️',
            'Thunderstorm': '⛈️',
            'Mist': '🌫️',
            'Fog': '🌫️'
        }.get(weather_main, '🌤️')
        
        print("\n" + "="*70)
        print(f"📍 {city.upper()}, {country} in weather Report")
        print("="*70)
        
        print(f"\n{weather_emoji}  wather conditon: {weather_desc}")
        
        print(f"\n🌡️  Temperature Details:")
        print(f"   ├─ Now: {temp}°C")
        print(f"   ├─ Feels Like: {feels_like}°C")
        print(f"   ├─ Min: {temp_min}°C")
        print(f"   └─ Max: {temp_max}°C")
        
        print(f"\n💧 Humidity: {humidity}%")
        
        print(f"\n🎚️  Air Pressure: {pressure} hPa")
        
        print(f"\n💨 Wind:")
        print(f"   ├─ Speed: {wind_speed} m/s")
        print(f"   └─ Direction: {wind_deg}°")
        
        print(f"\n☁️  Cloud Cover: {clouds}%")
        
        print(f"\n👁️  Visibility: {visibility} km")
        
        print(f"\n📍 Locations:")
        print(f"   ├─ Longitude: {data['coord']['lat']}°")
        print(f"   └─ Latitude: {data['coord']['lon']}°")
        
        print("\n" + "="*70)
        
        # Weather interpretation
        print("\n💡 result:")
        if temp > 30:
            print("   🔥 Today is hot!")
        elif temp < 10:
            print("   🧊 Today is cold!")
        else:
            print("   😊 Today's temperature is normal.")
        
        if humidity > 80:
            print("   💦 High humidity - rainy day ahead!")
        
        if clouds > 70:
            print("   ☁️  Cloudy skies ahead!")
        elif clouds < 30:
            print("   ☀️  Clear skies ahead!")
        
        print("\n" + "="*70)
    
    def save_to_file(self, data, filename=None):
        """
        Weather data JSON file එකක save කරනවා
        """
        if not data:
            return
        
        if not filename:
            city_name = data['name'].lower().replace(' ', '_')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"weather_{city_name}_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"\n💾 ✅ Weather data '{filename}' එකට save වුණා!")
            print(f"📂 File path: {filename}")
        except Exception as e:
            print(f"\n❌ Save error: {e}")
    
    def show_available_cities(self):
        """
        Available cities list show 
        """
        print("\n📋 city in Database:")
        print("\n🇱🇰 Sri Lankan Cities:")
        lk_cities = [city for city, data in self.database.items() 
                     if data['sys']['country'] == 'LK']
        for city in lk_cities:
            print(f"   • {city.title()}")
        
        print("\n🌍 International Cities:")
        int_cities = [city for city, data in self.database.items() 
                      if data['sys']['country'] != 'LK']
        for city in int_cities:
            country = self.database[city]['sys']['country']
            print(f"   • {city.title()} ({country})")
        print()


def main():
    """
    Main program function
    """
    print("\n" + "="*70)
    print("🌤️  WEATHER DATA FETCHER - DEMO VERSION")
    print("="*70)
    
    print("\n✨ demo version :")
    print("   ✅ API key, no need")
    print("   ✅ Internet connection not required") 
    print("   ✅ Real API structure simulate ")
    print("   ✅ Used Realistic weather data ")
    
    fetcher = WeatherFetcherDemo()
    
    print("\n" + "="*70)
    fetcher.show_available_cities()
    print("="*70)
    
    while True:
        city = input("\nEnter city name ('list' = cities, 'exit' = quit): ").strip()
        
        if city.lower() == 'exit':
            print("\n👋 Weather Fetcher demo close. Thank you!")
            break
        
        if city.lower() == 'list':
            fetcher.show_available_cities()
            continue
        
        if not city:
            print("❌ Please enter a city name!")
            continue
        
        # Fetch weather data
        weather_data = fetcher.fetch_weather(city)
        
        # Display data
        if weather_data:
            fetcher.display_weather(weather_data)
            
            # Ask to save
            save_choice = input("\n💾 Do you want to save this data? (y/n): ").strip().lower()
            if save_choice == 'y':
                fetcher.save_to_file(weather_data)
            
            # Compare option
            compare = input("\n🔄 Do you want to compare with another city? (y/n): ").strip().lower()
            if compare != 'y':
                final = input("\n❓ Do you want to exit? (y/n): ").strip().lower()
                if final == 'y':
                    print("\n👋 Thank you! Goodbye!")
                    break
        
        print("\n" + "-"*70)


if __name__ == "__main__":
    print("\n🎯 API Data Fetching Task - Complete Working Demo")
    print("📝  demonstrates this:")
    print("   1. ✅ API call simulation")
    print("   2. ✅ Data parsing from JSON")
    print("   3. ✅ User-friendly output formatting")
    print("   4. ✅ Error handling")
    print("   5. ✅ File saving capability")
    print("   6. ✅ Multiple city support")
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program stopped by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()