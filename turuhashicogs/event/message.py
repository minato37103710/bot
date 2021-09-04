import discord
from discord.ext import commands

class nasuyaki(commands.Cog):
    def __init__(self,bot):
      self.bot=bot

    @commands.Cog.listener()
    async def listenr(self,msg):
      if 'なす焼き' in msg.content or 'ナス焼き' in msg.content or 'なすやき' in msg.content:
        await msg.channel.send('なす焼き！（熱盛風）')

def setup(bot):
    bot.add_cog(nasuyaki(bot))
