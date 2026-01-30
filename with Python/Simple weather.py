"""
Simple Weather Fetcher - No API Key Required!
No need api running that code
"""

import requests
import json

def get_weather_simple(city):
    """
    Free weather API  used for weather data fetching
    wttr.in - No API key needed!
    """
    try:
        # Free API endpoint
        url = f"https://wttr.in/{city}?format=j1"
        
        print(f"\n🌍 {city} weather data loading ...")
        print("⏳ Please wait...")
        
        # API call 
        response = requests.get(url, timeout=15)
        
        # Checking success
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Error: Status code {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ Internet connection!")
        return None
    except requests.exceptions.Timeout:
        print("❌ Request timeout! try Again.")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def display_weather(data):
    """
    Weather data displaying user-friendly
    """
    try:
        # Data extract 
        current = data['current_condition'][0]
        location = data['nearest_area'][0]
        
        # Location details
        city = location['areaName'][0]['value']
        country = location['country'][0]['value']
        region = location['region'][0]['value']
        
        # Weather details
        temp_c = current['temp_C']
        temp_f = current['temp_F']
        feels_like_c = current['FeelsLikeC']
        humidity = current['humidity']
        pressure = current['pressure']
        weather_desc = current['weatherDesc'][0]['value']
        wind_kmph = current['windspeedKmph']
        visibility = current['visibility']
        uv_index = current['uvIndex']
        
        # Display 
        print("\n" + "="*70)
        print(f"📍 {city.upper()} Wather Information")
        print("="*70)
        
        print(f"\n📌 Location: {city}, {region}, {country}")
        print("\n" + "-"*70)
        
        print(f"\n🌡️  Temperature:")
        print(f"   ├─ Celsius:  {temp_c}°C")
        print(f"   └─ Fahrenheit: {temp_f}°F")
        
        print(f"\n🤔 Feels Like: {feels_like_c}°C")
        
        print(f"\n☁️  Weather Description: {weather_desc}")
        
        print(f"\n💧 Humidity: {humidity}%")
        
        print(f"\n🎚️  Air Pressure: {pressure} mb")
        
        print(f"\n💨 Wind Speed: {wind_kmph} km/h")
        
        print(f"\n👁️  Visibility: {visibility} km")
        
        print(f"\n☀️  UV Index: {uv_index}")
        
        print("\n" + "="*70)
        
        # Extra info
        if data.get('weather'):
            print("\n📅 24/7 wather data in future:")
            for i, hour in enumerate(data['weather'][0]['hourly'][:6], 1):
                time = hour['time']
                temp = hour['tempC']
                desc = hour['weatherDesc'][0]['value']
                # Convert time (e.g., "0" -> "00:00", "300" -> "03:00")
                time_str = f"{int(time):04d}"
                hour_str = f"{time_str[:2]}:{time_str[2:]}"
                print(f"   {hour_str} - {temp}°C - {desc}")
        
        print("\n" + "="*70)
        return True
        
    except KeyError as e:
        print(f"\n❌ Data parse error: {e}")
        print("💡 API response format may have changed or is incomplete.")
        return False
    except Exception as e:
        print(f"\n❌ Display error: {e}")
        return False


def save_weather_data(data, city):
    """
    Weather data saving in JSON file 
    """
    try:
        filename = f"weather_{city.lower().replace(' ', '_')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\n💾 ✅ Weather data '{filename}' saved successfully!")
        return filename
    except Exception as e:
        print(f"\n❌ Save error: {e}")
        return None


def main():
    """
    Main program
    """
    print("\n" + "="*70)
    print("🌤️  SIMPLE WEATHER FETCHER - No need API key!")
    print("="*70)
    
    print("\n✨ This program used wttr.in free API to fetch weather data.")
    print("💡 can check eny wather conditon!\n")
    
    # Examples show for users
    print("💡 Example city names you can try:")
    print("   • English: Colombo, Galle, Kandy, Kurunegala")
    print("   • World: London, New York, Tokyo, Paris, Dubai\n")
    
    while True:
        # City name get 
        city = input("Enter city name (or 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            print("\n👋 Weather Fetcher is closing. Thank you!")
            break
        
        if not city:
            print("❌ Please enter a valid city name!")
            continue
        
        # Weather data fetch 
        weather_data = get_weather_simple(city)
        
        if weather_data:
            # Display 
            success = display_weather(weather_data)
            
            if success:
                # Save data ask
                save_choice = input("\n💾 Do you want to save this data? (y/n): ").strip().lower()
                if save_choice == 'y':
                    save_weather_data(weather_data, city)
        else:
            print("\n❌ Weather data fetch failed!")
            print("💡 Tips:")
            print("   • Make sure the city name is spelled correctly")
            print("   • Check your internet connection")
            print("   • Try a different city name")
        
        # Continue or exit
        print("\n" + "-"*70)
        continue_choice = input("\n🔄 Do you want to check another city? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("\n👋 Thank you for using Weather Fetcher! Goodbye!")
            break
        print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    try:
        # Check requests library 
        import requests
        main()
    except ImportError:
        print("\n❌ 'requests' No library installed !")
        print("\n📝 How to Install? :")
        print("   pip install requests")
        print("\nInstall and run program.")
    except KeyboardInterrupt:
        print("\n\n👋 Program stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")