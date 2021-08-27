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
      except:
          await self.bot.change_presence(activity=discord.Game('エラーが発生しました'), status=discord.Status.dnd)
      self.bot.load_extension("turuhashicogs.dev")
      self.bot.load_extension('turuhashicogs.adminonly')
      self.bot.load_extension('turuhashicogs.music')
      self.bot.load_extension('cogs.eval')
      self.bot.load_extension('turuhashicogs.user')
      self.bot.load_extension('turuhashicogs.error_get')
      self.bot.load_extension('turuhashicogs.button')
      self.bot.load_extension('turuhashicogs.event.antispam')
      self.bot.load_extension('turuhashicogs.event.URLBlocker')
      self.bot.load_extension('turuhashicogs.event.join')
      self.bot.load_extension('turuhashicogs.nuke[joke]')
      self.bot.load_extension('cogs.ping')
      await self.bot.change_presence(activity=discord.Game('起動完了'))

def setup(bot):
	bot.add_cog(weakup(bot))
