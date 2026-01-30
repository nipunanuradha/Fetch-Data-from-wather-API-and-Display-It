"""
Simple Multi-API Fetcher
This program fetches data from multiple free APIs (no API keys required!)
"""

import requests
import json


def fetch_random_joke():
    """Fetch a random programming joke"""
    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
        data = response.json()
        
        if not data.get('error'):
            print("\n" + "="*60)
            print("😂 RANDOM PROGRAMMING JOKE")
            print("="*60)
            print(f"\n{data['joke']}\n")
            print("="*60)
        else:
            print("❌ Could not fetch joke")
            
    except Exception as e:
        print(f"❌ Error: {e}")


def fetch_cat_fact():
    """Fetch a random cat fact"""
    try:
        response = requests.get("https://catfact.ninja/fact")
        data = response.json()
        
        print("\n" + "="*60)
        print("🐱 RANDOM CAT FACT")
        print("="*60)
        print(f"\n{data['fact']}\n")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {e}")


def fetch_dog_image():
    """Fetch a random dog image URL"""
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()
        
        print("\n" + "="*60)
        print("🐕 RANDOM DOG IMAGE")
        print("="*60)
        print(f"\nImage URL: {data['message']}")
        print("\n(Open this URL in your browser to see the dog!)")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {e}")


def fetch_quote():
    """Fetch an inspirational quote"""
    try:
        response = requests.get("https://api.quotable.io/random")
        data = response.json()
        
        print("\n" + "="*60)
        print("💭 INSPIRATIONAL QUOTE")
        print("="*60)
        print(f"\n\"{data['content']}\"")
        print(f"\n— {data['author']}\n")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {e}")


def fetch_activity():
    """Fetch a random activity suggestion"""
    try:
        response = requests.get("https://www.boredapi.com/api/activity")
        data = response.json()
        
        print("\n" + "="*60)
        print("🎯 ACTIVITY SUGGESTION")
        print("="*60)
        print(f"\nActivity: {data['activity']}")
        print(f"Type: {data['type']}")
        print(f"Participants: {data['participants']}")
        print(f"Price: {'$' * int(data['price'] * 5) if data['price'] > 0 else 'Free!'}\n")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {e}")


def fetch_number_fact():
    """Fetch a random number fact"""
    try:
        import random
        number = random.randint(1, 100)
        response = requests.get(f"http://numbersapi.com/{number}")
        fact = response.text
        
        print("\n" + "="*60)
        print("🔢 NUMBER FACT")
        print("="*60)
        print(f"\n{fact}\n")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {e}")


def display_menu():
    """Display the menu options"""
    print("\n" + "="*60)
    print("🌐 MULTI-API DATA FETCHER")
    print("="*60)
    print("\nSelect an option:")
    print("1. 😂 Get a programming joke")
    print("2. 🐱 Get a cat fact")
    print("3. 🐕 Get a random dog image")
    print("4. 💭 Get an inspirational quote")
    print("5. 🎯 Get an activity suggestion")
    print("6. 🔢 Get a number fact")
    print("7. 🎲 Get ALL of the above!")
    print("0. ❌ Exit")
    print("="*60)


def fetch_all():
    """Fetch data from all APIs"""
    print("\n🎲 Fetching from all APIs...\n")
    fetch_random_joke()
    fetch_cat_fact()
    fetch_dog_image()
    fetch_quote()
    fetch_activity()
    fetch_number_fact()


def main():
    """Main function with menu"""
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (0-7): ").strip()
        
        if choice == '0':
            print("\n👋 Thanks for using the API Fetcher! Goodbye!")
            break
        elif choice == '1':
            fetch_random_joke()
        elif choice == '2':
            fetch_cat_fact()
        elif choice == '3':
            fetch_dog_image()
        elif choice == '4':
            fetch_quote()
        elif choice == '5':
            fetch_activity()
        elif choice == '6':
            fetch_number_fact()
        elif choice == '7':
            fetch_all()
        else:
            print("\n❌ Invalid choice! Please select 0-7.")
        
        # Ask if user wants to continue
        if choice != '0':
            continue_choice = input("\n🔄 Continue? (y/n): ").lower()
            if continue_choice != 'y':
                print("\n👋 Thanks for using the API Fetcher! Goodbye!")
                break


if __name__ == "__main__":
    print("\n✨ Welcome to the Multi-API Data Fetcher!")
    print("📝 This program demonstrates fetching data from various public APIs.")
    print("🚀 No API keys required - just run and explore!\n")
    
    main()