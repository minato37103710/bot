import discord
import asyncio
from discord.ext import commands

class timer(commands.Cog):
    """These are the developer commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def timer(self,ctx):
      await ctx.send('引数が不正です')

    @timer.command(name='second',aliases=['sec'])
    async def second(self,ctx,second):
      await asyncio.sleep(int(second))
      await ctx.send(f'{second}秒が経ちました')

    

def setup(bot):
	bot.add_cog(timer(bot)) 