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
      await ctx.send(f'{second}秒タイマーをかけます')
      await asyncio.sleep(int(second))
      await ctx.send(f'{second}秒が経ちました')

    @timer.command(name='minute',aliases=['mnt'])
    async def second(self,ctx,minute):
      await ctx.send(f'{minute}分タイマーをかけます')
      minute = minute*60
      await asyncio.sleep(int(minute))
      await ctx.send(f'{minute}分が経ちました')
    
    @timer.command(name='hour',aliases=['hu'])
    async def second(self,ctx,hour):
      await ctx.send(f'{hour}時間タイマーをかけます')
      hour = hour*600
      await asyncio.sleep(int(hour))
      await ctx.send(f'{hour}時間が経ちました')

def setup(bot):
	bot.add_cog(timer(bot)) 