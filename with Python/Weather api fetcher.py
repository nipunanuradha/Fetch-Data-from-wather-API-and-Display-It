"""
Weather Data Fetcher
This program fetches weather data from OpenWeatherMap API and displays it in a user-friendly format.
"""

import requests
import json
from datetime import datetime

class WeatherFetcher:
    def __init__(self, api_key):
        """Initialize the weather fetcher with API key"""
        self.api_key = api_key
        self.base_url = "http://api.weatherapi.com/v1/current.json?key=1c79708b20d740c097d145309263001&q=London&aqi=no"
    
    def fetch_weather(self, city):
        """
        Fetch weather data for a given city
        
        Args:
            city (str): Name of the city
            
        Returns:
            dict: Weather data or None if request fails
        """
        try:
            # Parameters for API request
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Use Celsius
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
        
        # Extract relevant information
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        weather_desc = data['weather'][0]['description'].capitalize()
        wind_speed = data['wind']['speed']
        
        # Display in a formatted way
        print("\n" + "="*50)
        print(f"📍 WEATHER REPORT FOR {city.upper()}, {country}")
        print("="*50)
        print(f"\n🌡️  Temperature: {temp}°C")
        print(f"🤔 Feels Like: {feels_like}°C")
        print(f"☁️  Conditions: {weather_desc}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🎚️  Pressure: {pressure} hPa")
        print(f"💨 Wind Speed: {wind_speed} m/s")
        print("\n" + "="*50)
    
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
    
    print("="*50)
    print("🌤️  WEATHER DATA FETCHER")
    print("="*50)
    
    # API Key (You need to get your own from openweathermap.org)
    # Sign up at: https://openweathermap.org/api
    api_key = "1c79708b20d740c097d145309263001"
    
    if api_key == "1c79708b20d740c097d145309263001":
        #print("\n⚠️  WARNING: Please replace 'e89f55408ac4f980a093d7dbf1fba991' with your actual API key")
        #print("📝 Get a free API key at: https://openweathermap.org/api")
        print("\nFor demonstration, using a demo mode...\n")
        # You can continue with demo mode or exit
        return
    
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