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
            await message.channel.send(random_faile)

def setup(bot):
    bot.add_cog(kagugoroku(bot))