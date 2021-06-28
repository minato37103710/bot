import discord
from discord.ext import commands
import asyncio
from discord.ext import tasks
from time import monotonic

class weakup(commands.Cog):
    """These are the developer commands"""

    def __init__(self, bot):
        self.bot = bot
  
    @tasks.loop(seconds=1)
    async def loop(self):
      guild=self.bot.get_guild(623002521207832586)
      await asyncio.sleep(5)
      await self.bot.change_presence(activity=discord.Game(f'{len(guild.members)}人'))
      await asyncio.sleep(5)
      await self.bot.change_presence(activity=discord.Game('!helpでhelp表示'))

    @tasks.loop(minutes=10)
    async def ping(self):

      ch=self.bot.get_channel(858675399320272916)
      t0 = monotonic()
        # Discord を通す関数を挟む。(応答速度)
      ping_message = await ch.send(embed=discord.Embed(title="計算中...",description=' '))

            # Δt = t1 - t0, latency は ping 的な意味、応答速度。1000倍は、ms(ミリセカンド)にするため。
      latency = (monotonic() - t0) * 1000

        # 送っていたメッセージを編集。ここで、応答速度を表示する。int にしているのは、小数点を消すため。( int は整数値)
      await ping_message.edit(embed=discord.Embed(title=f"Pong! 応答速度**{int(latency)}** ms です。",color=discord.Color.random()))

    @commands.Cog.listener()
    async def on_ready(self):
      await self.bot.change_presence(activity=discord.Game('起動中'))      
      self.bot.load_extension("kagucog.member")
      print('memberロード完了')
      self.bot.load_extension("kagucog.dev")
      print('devロード完了')
      self.bot.load_extension('kagucog.adminonly')
      print('adminonlyロード完了')
      self.bot.load_extension('kagucog.music')
      print('musicロード完了')
      self.bot.load_extension('cogs.eval')
      self.bot.load_extension('kagucog.picture')
      self.bot.load_extension('kagucog.user')
      self.bot.load_extension('kagucog.error_get')
      print('全cogロード完了')
      self.bot.load_extension('cogs.ping')
      self.bot.load_extension('jishaku')
      await asyncio.sleep(5)
      await self.bot.change_presence(activity=discord.Game('起動完了'))
      self.loop.start()
      self.ping.start()

def setup(bot):
	bot.add_cog(weakup(bot))