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
          self.bot.load_extension("turuhashicogs.member")
      except CommandError:
          ch=bot.get_channel(871241336492285974)
          await ch.send(f'cog読み込みでエラーが発生しました')
      self.bot.load_extension("turuhashicogs.dev")
      self.bot.load_extension('turuhashicogs.adminonly')
      self.bot.load_extension('turuhashicogs.music')
      self.bot.load_extension('turuhashicogs.user')
      self.bot.load_extension('turuhashicogs.error_get')
      self.bot.load_extension('turuhashicogs.button')
      self.bot.load_extension('turuhashicogs.event.antispam')
      self.bot.load_extension('turuhashicogs.event.URLBlocker')
      self.bot.load_extension('turuhashicogs.event.join')
      self.bot.load_extension('turuhashicogs.nuke[joke]')
      self.bot.load_extension('turuhashicogs.ping')
      self.bot.load_extension('turuhashicogs.tools.dispander')
      self.bot.load_extension('turuhashicogs.tools.buttons')
      self.bot.load_extension('turuhashicogs.tools.menu')
	
def setup(bot):
	bot.add_cog(weakup(bot))
