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

    @commands.command(name='ping')
    async def ping(self,ctx):
        # Δt = t1 - t0 の t0 を定義する。
        t0 = monotonic()
        # Discord を通す関数を挟む。(応答速度)
        ping_message = await ctx.send(embed=discord.Embed(title="計算中...",description=' '))

            # Δt = t1 - t0, latency は ping 的な意味、応答速度。1000倍は、ms(ミリセカンド)にするため。
        latency = (monotonic() - t0) * 1000

        # 送っていたメッセージを編集。ここで、応答速度を表示する。int にしているのは、小数点を消すため。( int は整数値)
        await ping_message.edit(embed=discord.Embed(title=f"Pong! 応答速度**{int(latency)}** ms です。",color=discord.Color.random()))

def setup(bot):
	bot.add_cog(timer(bot)) 