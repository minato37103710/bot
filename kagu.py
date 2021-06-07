import os
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio

intent=discord.Intents.all()

bot=commands.Bot(command_prefix='!',case_insensitive=True,intents=intent)

bot.author_id=757106917947605034

@bot.event
async def on_ready():
  print('on')



bot.load_extension("kagucog.weakup")

bot.run('ODQyOTk0NDUzMjQ5NTIzNzMz.YJ9Zww.oZVIOqgyp52Dqz_1r_JDZYbB3oQ')