# helpers.py
from storage import load_quotes, save_quotes

def add_quote(guild_id, quote):
    quotes = load_quotes()
    if guild_id not in quotes:
        quotes[guild_id] = []
    quotes[guild_id].append(quote)
    save_quotes(quotes)
    return f'Quote added: \"{quote}\"'

def get_random_quote(guild_id):
    quotes = load_quotes()
    if guild_id in quotes and quotes[guild_id]:
        import random
        return random.choice(quotes[guild_id])
    return "No quotes saved yet!"

def list_quotes(guild_id):
    quotes = load_quotes()
    if guild_id in quotes and quotes[guild_id]:
        return "\n".join([f"{i+1}. {quote}" for i, quote in enumerate(quotes[guild_id])])
    return "No quotes saved yet!"

def delete_quote(guild_id, index):
    quotes = load_quotes()
    if guild_id in quotes and 0 < index <= len(quotes[guild_id]):
        removed_quote = quotes[guild_id].pop(index - 1)
        save_quotes(quotes)
        return f"Deleted Quote: \"{removed_quote}\""
    return "Invalid quote index or no quotes saved."
