import discord
from discord.ext import commands
import asyncio
from discord.ext import tasks
from time import monotonic

class weakup(commands.Cog):
    """These are the developer commands"""

    def __init__(self, bot):
        self.bot = bot
  
    @commands.Cog.listener()
    async def on_ready(self):
      await self.bot.change_presence(activity=discord.Game('起動中'))      
      self.bot.load_extension("turuhashicogs.member")
      print('memberロード完了')
      self.bot.load_extension("turuhashicogs.dev")
      print('devロード完了')
      self.bot.load_extension('turuhashicogs.adminonly')
      print('adminonlyロード完了')
      self.bot.load_extension('turuhashicogs.music')
      print('musicロード完了')
      self.bot.load_extension('cogs.eval')
      self.bot.load_extension('turuhashicogs.user')
      self.bot.load_extension('turuhashicogs.error_get')
      self.bot.load_extension('turuhashicogs.button')
      self.bot.load_extension('turuhashicogs.listener')
      print('全cogロード完了')
      self.bot.load_extension('cogs.ping')
      await self.bot.change_presence(activity=discord.Game('起動完了'))

def setup(bot):
	bot.add_cog(weakup(bot))