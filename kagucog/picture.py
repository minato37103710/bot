import discord
from discord.ext import commands
import random
from tinydb import TinyDB, Query

db=TinyDB('picture.json')

User = Query()

class kagugoroku(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return

        if message.content == 'おはよう':
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
            a=random.choice(('0.png', '1.png', '2.png', '3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png'))
            await message.channel.send('語録あげる')
            await message.channel.send(file=discord.File(a))

        if 'vun' in message.content:
            emoji='<:vun:749229525572780062>'
            await message.add_reaction(emoji)

    @commands.command(name='add')
    async def _add(seld,ctx,*,arg):
        attachment = str(ctx.message.attachments[0])
        db.insert({'name':'arg','picture':attachment})

def setup(bot):
    bot.add_cog(kagugoroku(bot))