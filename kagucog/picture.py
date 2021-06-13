import discord
from discord.ext import commands
import random

class kagugoroku(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    random_faile= random.choice('0.png')

    @commands.Cog.listener()
    async def on_message(message):
        if message.content == 'おはよう':
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="家具語録だ、よーく見てろ。", value=random.choice(('0.png', '1.png', '2.png', '3.png')), inline=False)
        await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(kagugoroku(bot))