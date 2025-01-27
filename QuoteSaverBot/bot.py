import discord
from discord.ext import commands
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configure logging
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Bot setup
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user}")
    print(f"Bot logged in as {bot.user}")

# Command: Add a quote
@bot.command(name="addquote")
async def addquote(ctx, *, quote):
    from utils.helpers import add_quote
    result = add_quote(str(ctx.guild.id), quote)
    await ctx.send(result)
    logging.info(f"Quote added: {quote}")

# Command: Get a random quote
@bot.command(name="randomquote")
async def randomquote(ctx):
    from utils.helpers import get_random_quote
    quote = get_random_quote(str(ctx.guild.id))
    await ctx.send(quote)
    logging.info("Random quote retrieved.")

# Command: List all quotes
@bot.command(name="listquotes")
async def listquotes(ctx):
    from utils.helpers import list_quotes
    quotes = list_quotes(str(ctx.guild.id))
    await ctx.send(f"Quotes:\n{quotes}")
    logging.info("Quotes listed.")

# Command: Delete a quote by index
@bot.command(name="deletequote")
async def deletequote(ctx, index: int):
    from utils.helpers import delete_quote
    result = delete_quote(str(ctx.guild.id), index)
    await ctx.send(result)
    logging.info(f"Quote deleted: Index {index}")

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    logging.error("DISCORD_TOKEN is not set in the environment variables.")
