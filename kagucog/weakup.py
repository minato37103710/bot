import discord
from discord.ext import commands
import asyncio
from discord.ext import tasks

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

    @tasks.loop(hours=1)
    async def pr(self):
      ch=self.bot.get_channel(818455096647876628)
      await ch.send('a')

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
      print('全cogロード完了')
      self.bot.load_extension('cogs.ping')
      self.bot.load_extension('jishaku')
      await asyncio.sleep(5)
      await self.bot.change_presence(activity=discord.Game('起動完了'))
      self.loop.start()
      self.pr.start()

def setup(bot):
	bot.add_cog(weakup(bot))