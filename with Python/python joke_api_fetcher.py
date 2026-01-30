"""
Random Joke Fetcher
This program fetches random jokes from JokeAPI (no API key required!)
"""

import requests
import json

class JokeFetcher:
    def __init__(self):
        """Initialize the joke fetcher"""
        self.base_url = "https://v2.jokeapi.dev/joke"
    
    def fetch_joke(self, category="Any"):
        """
        Fetch a random joke
        
        Args:
            category (str): Joke category (Programming, Misc, Dark, Pun, Spooky, Christmas)
            
        Returns:
            dict: Joke data or None if request fails
        """
        try:
            # Build URL with category
            url = f"{self.base_url}/{category}"
            
            print(f"\n😄 Fetching a {category} joke...")
            
            # Make the API request
            response = requests.get(url)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as err:
            print(f"❌ Error fetching joke: {err}")
            return None
    
    def display_joke(self, data):
        """
        Display joke in a user-friendly format
        
        Args:
            data (dict): Joke data from API
        """
        if not data or data.get('error'):
            print("❌ Could not fetch joke!")
            return
        
        print("\n" + "="*60)
        print("😂 HERE'S YOUR JOKE!")
        print("="*60)
        
        # Check joke type (single or two-part)
        if data['type'] == 'single':
            print(f"\n{data['joke']}\n")
        else:
            print(f"\n{data['setup']}")
            input("\n[Press Enter for the punchline...]")
            print(f"\n👉 {data['delivery']}\n")
        
        print("="*60)
        print(f"Category: {data['category']}")
        print("="*60)


def main():
    """Main function"""
    print("="*60)
    print("🎭 RANDOM JOKE FETCHER")
    print("="*60)
    
    fetcher = JokeFetcher()
    
    categories = ["Any", "Programming", "Misc", "Pun", "Spooky", "Christmas"]
    
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    # Get category choice
    choice = input("\nSelect category (1-6) or press Enter for 'Any': ").strip()
    
    if choice and choice.isdigit() and 1 <= int(choice) <= len(categories):
        category = categories[int(choice) - 1]
    else:
        category = "Any"
    
    # Fetch and display joke
    joke_data = fetcher.fetch_joke(category)
    
    if joke_data:
        fetcher.display_joke(joke_data)
        
        # Ask for another joke
        another = input("\n🔄 Want another joke? (y/n): ").lower()
        if another == 'y':
            main()
    
    print("\n👋 Thanks for using Joke Fetcher!")


if __name__ == "__main__":
    main()