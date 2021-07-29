import discord
from discord.ext import commands

guild_id = 623002521207832586

class adminonly(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='adoy')
    async def adoy(self,ctx):
      if ctx.invoked_subcommand is None:
        await ctx.send('サブコマンド入れて')

    @commands.command(name='mute')
    @commands.has_permissions(manage_channels=True)
    async def mute(self,ctx,member:discord.Member):
      role = ctx.guild.get_role(698769459023839232)
      await member.add_roles(role)
      print('ok')
    
    @commands.command(name='muteremove',aliases=['muterem'])
    @commands.has_permissions(manage_channels=True)
    async def remove(self,ctx,member:discord.Member):
      role = ctx.guild.get_role(698769459023839232)
      await member.remove_roles(role)
      print('ok')
    
    

def setup(bot):
	bot.add_cog(adminonly(bot))