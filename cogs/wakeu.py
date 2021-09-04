import discord
from discord.ext import commands
from os import listdir
from sys import argv

class weakup(commands.Cog):
    """These are the developer commands"""

    def __init__(self, bot):
        self.bot = bot
  
    @commands.Cog.listener()
    async def on_ready(self):
# cogsフォルダにあるエクステンションを読み込む。
        for path in listdir("cogs"):
            if path[0] in ("#", "."):
                continue
            if path.endswith(".py"):
                bot.load_extension("cogs." + path[:-3])
            elif "." not in path and path != "__pycache__" and path[0] != ".":
                bot.load_extension("cogs." + path)
            bot.print("Loaded extension", path)
            
def setup(bot):
	bot.add_cog(weakup(bot))            
