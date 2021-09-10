import os
import discord
from discord.ext import commands
import asyncio
bot=commands.Bot(command_prefix='Test!',intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(f'{bot.user} is online')
  print(bot.user.id)

@bot.commands(name='test')
async def test(ctx,aaa):
  await ctx.send(aaa)

bot.load_extension('jishaku')
bot.run(os.getenv('token'))
