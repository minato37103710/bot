import discord
from discord.ext import commands
from re import findall

print('tokendel読み込み完了')

class tokendel(commands.Cog):
      def __init__(self, bot):
        self.bot = bot 
        
      def token_check(self, content: str) -> bool:
        return bool(findall("([a-zA-Z]{24}).([a-zA-Z]{6}).([a-zA-Z]{27})", content))
      @commands.Cog.listener()
      async def on_message(self,message):
        if self.token_check(message.content):
          await message.author.ban(reason="token爆したから自動BAN")

def setup(bot):
    bot.add_cog(tokendel(bot))
