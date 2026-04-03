import discord
from discord.ext import commands
import random
import string
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def generate_username(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def user(ctx, length: int):
    username = generate_username(length)
    await ctx.send(f"🎯 Username: `{username}`")

bot.run(os.getenv("TOKEN"))
