import discord
from discord.ext import commands

class error_get(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name='get')
    async def get(self,ctx):
        inpu=input('error:')
        await ctx.send(inpu)

def setup(bot):
    bot.add_cog(error_get(bot))
