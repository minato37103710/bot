import discord
from discord.ext import commands

class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name='user_info',aliases=['ui'])
    async def userab(self,ctx, member : discord.Member):
        usab = discord.Embed(title=f'{member}の詳細', description='詳細だよ', color=discord.Color.orange())
        usab.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        usab.set_thumbnail(url=member.avatar_url)
        usab.add_field(name='名前', value=f'**{member.display_name}#{member.discriminator}**')
        usab.add_field(name='あなたはBot?', value=member.bot)
        usab.add_field(name='ID', value=member.id)
        usab.add_field(name='作成時間', value=member.created_at)
        usab.add_field(name='サーバーに参加した時間', value=member.joined_at)
        await ctx.send(embed=usab)

def setup(bot):
    bot.add_cog(user(bot))