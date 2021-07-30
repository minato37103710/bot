import discord
from discord.ext import commands

guild_id = 623002521207832586

class adminonly(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    
    

def setup(bot):
	bot.add_cog(adminonly(bot))