# add_quote.py
import json
import os

DATA_FILE = "data/quotes.json"

def ensure_data_file():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)

ensure_data_file()

def load_quotes():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_quotes(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_quote(guild_id, quote):
    quotes = load_quotes()
    if guild_id not in quotes:
        quotes[guild_id] = []
    quotes[guild_id].append(quote)
    save_quotes(quotes)
    return f'Quote added: \"{quote}\"'

# Example usage
guild_id = "1234567890"  # Replace with actual guild/server ID
quote = "This is an example quote."
result = add_quote(guild_id, quote)
print(result)
