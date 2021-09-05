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
      
      if msg.author.id==750276955085078528:
        await msg.add_reaction('\N{AUBERGINE}')
        await msg.add_reaction('\N{FIRE}')
      if 'なす焼き' in msg.content or 'ナス焼き' in msg.content or 'なすやき' in msg.content:
        nasu=['なす焼き！（熱盛風）','<:20210831182900711:882779002903879720>','<:emoji_1:883695590213566504>']
        yaki=random.choice(nasu)
        await msg.channel.send(yaki)
      
      if '麻焼き' in msg.content:
        await msg.channel.send('https://media.discordapp.net/attachments/866291202528510002/884015121016455209/Screenshot_20210905-190017_Discord.jpg')

def setup(bot):
    bot.add_cog(nasuyaki(bot))
