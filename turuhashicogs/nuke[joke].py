import discord
from discord.ext import commands

class nuke-joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nuke')
    async def nuke(self,ctx)
        msg = await client.wait_for('ctx',timeout=5)
        await channel.send(f'{msg.author.mention}、こんにちは！')

def setup(bot):
    bot.add_cog(nuke-joke(bot))
