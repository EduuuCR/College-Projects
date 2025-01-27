# list_quotes.py
import json

DATA_FILE = "data/quotes.json"

def load_quotes():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def list_quotes(guild_id):
    quotes = load_quotes()
    if guild_id in quotes and quotes[guild_id]:
        return "\n".join([f"{i+1}. {quote}" for i, quote in enumerate(quotes[guild_id])])
    return "No quotes saved yet!"

# Example usage
guild_id = "1234567890"  # Replace with actual guild/server ID
quotes_list = list_quotes(guild_id)
print(f"Quotes:\n{quotes_list}")
