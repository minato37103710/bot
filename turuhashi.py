import discord
from discord.ext import commands,tasks


intent=discord.Intents.all()

bot=commands.Bot(command_prefix='!',case_insensitive=True,intents=intent)

bot.author_id=757106917947605034

bot.load_extension('jishaku')

bot.load_extension("turuhashicogs.weakup")

bot.run('ODcwMTI0NTQxMjcwMTcxNzgw.YQIMoA._6BZr1uWoWWAvF6j7JKWBxKu3TU')
