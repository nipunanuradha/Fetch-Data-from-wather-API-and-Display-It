"""
Weather Data Fetcher
This program fetches weather data from WeatherAPI.com and displays it in a user-friendly format.
"""

import requests
import json
from datetime import datetime

class WeatherFetcher:
    def __init__(self, api_key):
        """Initialize the weather fetcher with API key"""
        self.api_key = api_key
        # Fixed: Using correct WeatherAPI.com base URL
        self.base_url = "http://api.weatherapi.com/v1/current.json"
    
    def fetch_weather(self, city):
        """
        Fetch weather data for a given city
        
        Args:
            city (str): Name of the city
            
        Returns:
            dict: Weather data or None if request fails
        """
        try:
            # Fixed: Correct parameters for WeatherAPI.com
            params = {
                'key': self.api_key,  # Changed from 'appid' to 'key'
                'q': city,
                'aqi': 'no'  # Air quality index not needed
            }
            
            # Make the API request
            print(f"\n🌍 Fetching weather data for {city}...")
            response = requests.get(self.base_url, params=params)
            
            # Check if request was successful
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                print(f"❌ Error: City '{city}' not found!")
            elif response.status_code == 401:
                print("❌ Error: Invalid API key!")
            else:
                print(f"❌ HTTP Error: {http_err}")
            return None
            
        except requests.exceptions.ConnectionError:
            print("❌ Error: No internet connection!")
            return None
            
        except requests.exceptions.Timeout:
            print("❌ Error: Request timed out!")
            return None
            
        except requests.exceptions.RequestException as err:
            print(f"❌ Error: {err}")
            return None
    
    def display_weather(self, data):
        """
        Display weather data in a user-friendly format
        
        Args:
            data (dict): Weather data from API
        """
        if not data:
            return
        
        # Fixed: Extract data from WeatherAPI.com response structure
        # Location data
        city = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        
        # Current weather data
        temp_c = data['current']['temp_c']
        temp_f = data['current']['temp_f']
        feels_like_c = data['current']['feelslike_c']
        feels_like_f = data['current']['feelslike_f']
        humidity = data['current']['humidity']
        pressure_mb = data['current']['pressure_mb']
        weather_desc = data['current']['condition']['text']
        wind_kph = data['current']['wind_kph']
        wind_mph = data['current']['wind_mph']
        wind_dir = data['current']['wind_dir']
        cloud = data['current']['cloud']
        uv = data['current']['uv']
        visibility = data['current']['vis_km']
        
        # Display in a formatted way
        print("\n" + "="*60)
        print(f"📍 WEATHER REPORT FOR {city.upper()}")
        print(f"   {region}, {country}")
        print("="*60)
        print(f"\n🌡️  Temperature: {temp_c}°C ({temp_f}°F)")
        print(f"🤔 Feels Like: {feels_like_c}°C ({feels_like_f}°F)")
        print(f"☁️  Conditions: {weather_desc}")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️  Cloud Cover: {cloud}%")
        print(f"🎚️  Pressure: {pressure_mb} mb")
        print(f"💨 Wind: {wind_kph} km/h ({wind_mph} mph) {wind_dir}")
        print(f"👁️  Visibility: {visibility} km")
        print(f"☀️  UV Index: {uv}")
        print("\n" + "="*60)
    
    def save_to_file(self, data, filename="weather_data.json"):
        """
        Save weather data to a JSON file
        
        Args:
            data (dict): Weather data
            filename (str): Output filename
        """
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"\n💾 Data saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")


def main():
    """Main function to run the weather fetcher"""
    
    print("="*60)
    print("🌤️  WEATHER DATA FETCHER")
    print("="*60)
    
    # Your WeatherAPI.com API Key
    api_key = "1c79708b20d740c097d145309263001"
    
    # Create weather fetcher instance
    fetcher = WeatherFetcher(api_key)
    
    # Get city from user
    city = input("\nEnter city name: ").strip()
    
    if not city:
        print("❌ City name cannot be empty!")
        return
    
    # Fetch weather data
    weather_data = fetcher.fetch_weather(city)
    
    # Display the data
    if weather_data:
        fetcher.display_weather(weather_data)
        
        # Ask if user wants to save data
        save = input("\n💾 Would you like to save this data to a file? (y/n): ").lower()
        if save == 'y':
            fetcher.save_to_file(weather_data)
        
        # Ask if user wants to check another city
        another = input("\n🔄 Check another city? (y/n): ").lower()
        if another == 'y':
            main()  # Recursive call to check another city


if __name__ == "__main__":
    main()