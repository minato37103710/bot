import discord
from discord.ext import commands

class nuke_joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nuke')
    async def nuke(self,ctx):
        channel=ctx.channel
        await ctx.send('5秒以内にこんにちはと送信してね！')

        def hello_check(m):
            return m.content == 'こんにちは' and m.channel == channel

        msg = await self.bot.wait_for('message', check=hello_check,timeout=5)
        await channel.send(f'{ctx.author.mention}、こんにちは！')

def setup(bot):
    bot.add_cog(nuke_joke(bot))
