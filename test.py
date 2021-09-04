import os
import discord
from discord.ext import commands
import asyncio
bot=commands.Bot(command_prefix='Test!',intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(f'{bot.user} is online')
  print(bot.user.id)

@bot.event
async def on_message(msg):
  if msg.content=='1234567890':
    await asyncio.sleep(1)
    await msg.channel.send('1234567890')

bot.load_extension('jishaku')
bot.run(os.getenv('token'))
