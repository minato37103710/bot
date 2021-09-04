import discord
from discord.ext import commands
import glob, random
import asyncio

class listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_message(self,msg):
        logch=self.bot.get_channel(870501783770910720)
        if 'giscord.gg' in msg.content:
              await msg.channel.purge(limit=1)
              await msg.channel.send(f'URLを検知したため削除いたしました\n発言者{msg.author.mention}')

        elif 'youtube' in msg.content or 'youtu.be' in msg.content:
              if 'RQR4c0w_gsk' in msg.content:
                await msg.channel.purge(limit=1)
                await msg.channel.send(f'荒連youtubeURLを検知したため削除&kickいたしました\n送信者:{msg.author.mention}')
                await msg.author.kick(reason='荒連youtubeURLを検知したため')
        elif 'https://twitter' in msg.content:
            await msg.channel.purge(limit=1,check=is_you)
            await msg.channel.send(f'URLを検知したため削除いたしました\n発言者{msg.author.mention}')

def setup(bot):
    bot.add_cog(listener(bot))
