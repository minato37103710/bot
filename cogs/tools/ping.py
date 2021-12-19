import discord
import asyncio
from discord.ext import commands
from time import monotonic
import random


class ping(commands.Cog):
    """These are the developer commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self,ctx):
      a=random.randint(1,100)

      b=random.randint(1,100)

      aaa = await ctx.send(f'{a}+{b}=')
      
      d=a+b
    
      def check(m):
          return m.content==d and m.channel == channel  
    try:
      raise #await self.bot.wait_for('ctx',check=check)
    
        
    # Δt = t1 - t0 の t0 を定義する。
      t0 = monotonic()
        # Discord を通す関数を挟む。(応答速度)
      ping_message = await ctx.send(embed=discord.Embed(title="計算中...",description=' '))

            # Δt = t1 - t0, latency は ping 的な意味、応答速度。1000倍は、ms(ミリセカンド)にするため。
      latency = (monotonic() - t0) * 1000

        # 送っていたメッセージを編集。ここで、応答速度を表示する。int にしているのは、小数点を消すため。( int は整数値)
      await ping_message.edit(embed=discord.Embed(title=f"Pong! 応答速度**{int(latency)}** ms です。",color=discord.Color.random()))
    except Except as e:
        print(e)

def setup(bot):
  bot.add_cog(ping(bot)) 
