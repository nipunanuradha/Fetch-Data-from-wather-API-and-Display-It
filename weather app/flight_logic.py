import os
import requests
from dotenv import load_dotenv

class FlightFetcher:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("AVIATIONSTACK_API_KEY")
        self.base_url = "http://api.aviationstack.com/v1/flights"

    def fetch_flight(self, flight_number):
        if not flight_number or not str(flight_number).strip():
            return None
        
        if not self.api_key:
            print("WARNING: No AviationStack API key found.")
            return None

        # Aviationstack accepts flight_iata for the common flight number format (e.g. AA100)
        params = {
            'access_key': self.api_key,
            'flight_iata': flight_number.upper().strip()
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            if response.status_code != 200:
                print(f"Error: {response.status_code} - {response.text}")
                return None
            
            data = response.json()
            if 'data' in data and len(data['data']) > 0:
                # Aviationstack flight data can contain historical flights, we ideally want an active or scheduled one
                flights = data['data']
                
                # Sort flights by departure time descending so we get the most recent one
                flights.sort(key=lambda x: x['departure']['estimated'] or x['departure']['scheduled'] or "1970", reverse=True)
                
                # Try to find one that is active or scheduled first
                active_flight = next((f for f in flights if f['flight_status'] in ['active', 'scheduled']), None)
                return active_flight if active_flight else flights[0]
            else:
                return None
                
        except requests.RequestException as e:
            print(f"Request exception: {e}")
            return None
