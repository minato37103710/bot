import discord
from discord.ext import commands
import random
class nasuyaki(commands.Cog):
    def __init__(self,bot):
      self.bot=bot

    @commands.Cog.listener()
    async def on_message(self,msg):
      if msg.author.bot:
        return

      if 'なす焼き' in msg.content or 'ナス焼き' in msg.content or 'なすやき' in msg.content:
        nasu=random.choice(['なす焼き！（熱盛風）','<:20210831182900711:882779002903879720>'])
        await msg.channel.send()

def setup(bot):
    bot.add_cog(nasuyaki(bot))
