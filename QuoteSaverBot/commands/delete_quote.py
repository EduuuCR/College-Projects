# delete_quote.py
import json

DATA_FILE = "data/quotes.json"

def load_quotes():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_quotes(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def delete_quote(guild_id, index):
    quotes = load_quotes()
    if guild_id in quotes and 0 < index <= len(quotes[guild_id]):
        removed_quote = quotes[guild_id].pop(index - 1)
        save_quotes(quotes)
        return f"Deleted Quote: \"{removed_quote}\""
    return "Invalid quote index or no quotes saved."

# Example usage
guild_id = "1234567890"  # Replace with actual guild/server ID
quote_index = 1  # Replace with the index of the quote to delete
result = delete_quote(guild_id, quote_index)
print(result)
