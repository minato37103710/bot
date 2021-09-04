import os
import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='Test!',intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(f'{bot.user} is online')
  print(bot.id)

bot.run(os.getenv('token'))
