import discord
from discord.ext import commands

class nuke_joke(commands.Cog,name='ジョークコマンド'):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name='nuke',description='テキストチャンネルのメッセージを全消しします')
    async def nuke(self,ctx):
        """ジョークコマンドです"""
        channel=ctx.channel
        await ctx.send('8秒以内に確認と送信してね')

        def hello_check(m):
            return m.content == '確認' and m.channel == channel and m.author==ctx.author
        try:
            msg = await self.bot.wait_for('message', check=hello_check,timeout=8)
            await channel.send(f'{ctx.author.mention}、え？何しようとしてるの？（）メッセージ全消しとか害悪すぎでしょw')
        except Asyncio.TimeoutError:
            await channel.send('時間だ')
def setup(bot):
    bot.add_cog(nuke_joke(bot))
