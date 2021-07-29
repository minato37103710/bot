import discord
from discord.ext import commands
import glob, random
from tinydb import TinyDB, Query
import asyncio


class listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_message(self,msg):
        
        if 'https://' in msg.content:
            if '.png' in msg.content:
                pass

            elif '.jpeg' in msg.content:
                pass
            
            else:
                await msg.channel.purge(limit=1)
                await msg.channel.send(f'URLを検知したため削除いたしました\n送信者:{msg.author.mention}')

def setup(bot):
    bot.add_cog(listener(bot))