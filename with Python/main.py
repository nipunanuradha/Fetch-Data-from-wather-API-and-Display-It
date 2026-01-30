import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    
    try:
        # Fetching data from API
        response = requests.get(url)
        data = response.json()
        
        print("\n--- Here is a Joke for You! ---")
        
        # Checking the joke type
        if data["type"] == "single":
            print(f"Joke: {data['joke']}")
        else:
            print(f"Setup: {data['setup']}")
            print(f"Delivery: {data['delivery']}")
            
        print("-------------------------------\n")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_joke()