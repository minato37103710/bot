import discord
from discord.ext import commands

class member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
      role = member.guild.get_role(870330199777112074)
      await member.add_roles(role)      

def setup(bot):
    bot.add_cog(member_join(bot))