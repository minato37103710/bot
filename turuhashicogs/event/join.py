import discord
from discord.ext import commands
import datetime

class member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
      ch1=self.bot.get_channel(866265731301376002)
      ch2=self.bot.get_channel(880344125042491402)
      usab = discord.Embed(title=f'{member}の詳細', description='詳細だよ', color=discord.Color.orange())
      usab.set_author(name=member.name, icon_url=member.avatar.url)
      usab.set_thumbnail(url=member.avatar.url)
      usab.add_field(name='名前', value=f'**{member.display_name}#{member.discriminator}**')
      usab.add_field(name='あなたはBot?', value=member.bot)
      usab.add_field(name='ID', value=member.id)
      usab.add_field(name='作成時間', value=member.created_at)
      usab.add_field(name='サーバーに参加した時間', value=member.joined_at)
      await ch1.send(f'よろしくお願いします！\nもしよければ、ホワイトリスト申請のところに自分のゲーマータグを書いて、新規さんガイドを読んでください！')
      await ch2.send(embed=usab)
        
def setup(bot):
    bot.add_cog(member_join(bot))
