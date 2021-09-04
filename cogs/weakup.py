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
      try:
          self.bot.load_extension("cogs.tools.member")
      except commands.errors.CommandError:
          ch=self.bot.get_channel(871241336492285974)
          await ch.send(f'cog読み込みでエラーが発生しました')
      self.bot.load_extension('cogs.tools.user')
      self.bot.load_extension('cogs.event.antispam')
      self.bot.load_extension('cogs.event.URLBlocker')
      self.bot.load_extension('cogs.event.join')
      self.bot.load_extension('cogs.event.message')
      self.bot.load_extension('cogs.tools.nuke[joke]')
      self.bot.load_extension('cogs.tools.ping')
      self.bot.load_extension('cogs.tools.dispander')
      self.bot.load_extension('cogs.tools.buttons')
      self.bot.load_extension('cogs.tools.menus')
	
def setup(bot):
   bot.add_cog(weakup(bot))
