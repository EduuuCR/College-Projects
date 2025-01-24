# random_quote.py
import json
import random

DATA_FILE = "data/quotes.json"

def load_quotes():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def get_random_quote(guild_id):
    quotes = load_quotes()
    if guild_id in quotes and quotes[guild_id]:
        return random.choice(quotes[guild_id])
    return "No quotes saved yet!"

# Example usage
guild_id = "1234567890"  # Replace with actual guild/server ID
random_quote = get_random_quote(guild_id)
print(random_quote)
