import requests

# API URL
url = "https://official-joke-api.appspot.com/random_joke"

try:
    # Fetch data from API
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors

    # Parse JSON data
    data = response.json()

    # Extract required information
    setup = data["setup"]
    punchline = data["punchline"]

    # Display data in user-friendly format
    print("\n😂 Random Joke 😂")
    print("-----------------")
    print("Setup:", setup)
    print("Punchline:", punchline)

except requests.exceptions.RequestException as e:
    print("Error fetching data from API:", e)
