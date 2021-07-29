import discord
from discord.ext import commands

class member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(member):
      role=member.guild.get_role(870330337878741062)#(870202263908532255)
      #removing the messages sent by them with the check=is_me using the discord.TextChannel.purge method.
      await member.add_roles(role)

def setup(bot):
    bot.add_cog(member_join(bot))