import discord
from discord.ext import commands
import random

# Define your bot's command prefix (e.g., '/') and set intents
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Dictionary to store quotes (could be replaced with a database for persistent storage)
quote_storage = {}

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

@bot.command(name='quote_add')
async def add_quote(ctx, *, quote: str):
    """Adds a quote to the storage."""
    if ctx.guild.id not in quote_storage:
        quote_storage[ctx.guild.id] = []
    
    quote_storage[ctx.guild.id].append(quote)
    await ctx.send(f'Quote added: "{quote}"')

@bot.command(name='quote_random')
async def random_quote(ctx):
    """Sends a random quote from the storage."""
    if ctx.guild.id in quote_storage and quote_storage[ctx.guild.id]:
        quote = random.choice(quote_storage[ctx.guild.id])
        await ctx.send(f'Random Quote: "{quote}"')
    else:
        await ctx.send('No quotes saved yet! Use `/quote_add` to add one.')

@bot.command(name='quote_list')
async def list_quotes(ctx):
    """Lists all saved quotes for the server."""
    if ctx.guild.id in quote_storage and quote_storage[ctx.guild.id]:
        quotes = '\n'.join([f'{i+1}. {q}' for i, q in enumerate(quote_storage[ctx.guild.id])])
        await ctx.send(f'Quotes saved on this server:\n{quotes}')
    else:
        await ctx.send('No quotes saved yet! Use `/quote_add` to add one.')

@bot.command(name='quote_delete')
async def delete_quote(ctx, index: int):
    """Deletes a specific quote by its index."""
    if ctx.guild.id in quote_storage and 0 < index <= len(quote_storage[ctx.guild.id]):
        removed_quote = quote_storage[ctx.guild.id].pop(index - 1)
        await ctx.send(f'Deleted Quote: "{removed_quote}"')
    else:
        await ctx.send('Invalid quote index or no quotes saved yet.')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
