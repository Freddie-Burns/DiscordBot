"""
I had to open IE as admin, go to discord.com, click the lock to the
right of the url and issue a certificate to connect through SSL.
"""
import os
import random

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

global current_roll
current_roll = None

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='horl')
async def nine_nine(ctx):
    global current_roll
    response = random.randint(1, 6)
    current_roll = response
    await ctx.send(response)


@bot.command(name='higher', aliases=['h', 'hi'])
async def higher(ctx):
    global current_roll
    second_roll = random.randint(1, 6)
    if current_roll is None:
        response = "Roll before betting."
    elif second_roll > current_roll:
        response = f"{second_roll} - Higher was correct!"
    else:
        response = f"{second_roll} - Higher was wrong"
    current_roll = None
    await ctx.send(response)


@bot.command(name='lower', aliases=['l', 'lo'])
async def lower(ctx):
    global current_roll
    second_roll = random.randint(1, 6)
    if current_roll is None:
        response = "Roll before betting."
    elif second_roll < current_roll:
        response = f"{second_roll} - Lower was correct!"
    else:
        response = f"{second_roll} - Lower was wrong"
    current_roll = None
    await ctx.send(response)


@bot.command(name='same', aliases=['s',])
async def same(ctx):
    global current_roll
    second_roll = random.randint(1, 6)
    if current_roll is None:
        response = "Roll before betting."
    elif second_roll == current_roll:
        response = f"{second_roll} - The same was correct!"
    else:
        response = f"{second_roll} - The same was wrong"
    current_roll = None
    await ctx.send(response)


@bot.command(name='cancel', aliases=['c', 'e', 'q', 'exit', 'quit'])
async def cancel(ctx):
    global current_roll
    current_roll = None


bot.run(TOKEN)
