import discord
from discord.ext import commands
import random

class kagugoroku(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    random_faile= random.choice('0.png')

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return

        if message.content == 'おはよう':
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
            a=random.choice(('picture.0', 'picture.1g', 'picture.2', 'picture3'))
            await message.channel.send('語録あげる')
            await message.channel.send(file=discord.File(a))

def setup(bot):
    bot.add_cog(kagugoroku(bot))