import discord
from discord.ext import commands

class member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
      ch=self.bot.get_channel(866265731301376002)
      await ch.send(f'よろしくお願いします！\nもしよければ、ホワイトリスト申請のところに自分のゲーマータグを書いて、新規さんガイドを読んでください！')

def setup(bot):
    bot.add_cog(member_join(bot))