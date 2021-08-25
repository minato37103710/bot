import discord
from discord.ext import commands
import glob, random
import asyncio
from tinydb import TinyDB, Query
from tinydb.operations import increment
import json

db=TinyDB('spam.json')

User = Query()

class listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_message(self,msg):
        logch=self.bot.get_channel(870501783770910720)
        if 'https://' in msg.content or 'http://'in msg.content:
            if '.png' in msg.content:
                pass

            elif '.jpg' in msg.content:
                pass

            elif 'youtube' in msg.content:
                if 'RQR4c0w_gsk' in msg.content:
                    await msg.channel.purge(limit=1)
                    await msg.channel.send(f'荒連youtubeURLを検知したため削除&kickいたしました\n送信者:{msg.author.mention}')
                    await msg.author.kick(reason='荒連youtubeURLを検知したため')
          
            elif 'amazon' in msg.content:
                pass
            
            else:
                await msg.channel.purge(limit=1)
                await msg.channel.send(f'URLを検知したため削除いたしました\n送信者:{msg.author.mention}\n対象url:{msg.content.replace("https//", "httpsリンク")}')
                if len(db.search(User.name==msg.author.id)) > 0:
                    pass
                                
                else: 
                    db.insert({'name':msg.author.id, 'age':1})
                
                db.update(increment('age'), User.name == msg.author.id)
def setup(bot):
    bot.add_cog(listener(bot))
