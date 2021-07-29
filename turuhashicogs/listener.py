import discord
from discord.ext import commands
import glob, random
from tinydb import TinyDB, Query
import asyncio
import traceback

db=TinyDB('picture.json')

User = Query()

class kagugoroku(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_message(self,msg,error):
        spamming_list = []
    #you can use a json, if you have a public bot but for now let's just use this
        #checking if the author is in the list, to prevent bot spamming.
        if str(msg.author.id) not in spamming_list:
            try:
                spamming_list.append(str(msg.author.id))
                #appending it so it stops the spam
                def checki(m):
                    return m.author == msg.author and m.channel == msg.channel
                #big brain part comes here, the bot waits for the message for 2 seconds and if thats satisfied it waits again for a message for 2 seconds and if the playing reaches the end it means they spammed
                respa = await self.bot.wait_for('message', timeout=1, check=checki)
                if respa:
                    respd = await self.bot.wait_for('message', timeout=1, check=checki)
                    if respd:
                        respe = await self.bot.wait_for('message', timeout=1, check=checki)
                        if respe:
                            respw= await self.bot.wait_for('message', timeout=1, check=checki)
                            if respw:
                                respq = await self.bot.wait_for('message', timeout=1, check=checki)
                                #getting the message author
                                def is_me(m):
                                    return m.author == msg.author
                                #removing the messages sent by them with the check=is_me using the discord.TextChannel.purge method.
                                await msg.author.add_role(msg.guild.get_roles(870202263908532255))  
                                await msg.channel.purge(limit=4, check=is_me)
                                await msg.channel.send(f"Stop spamming {msg.author.mention}")
                                  
                                #removing them from the list
                                spamming_list.remove(str(msg.author.id))
            except asyncio.TimeoutError:
                #it means they are not spamming also removing it
                spamming_list.remove(str(msg.author.id))
                return
def setup(bot):
    bot.add_cog(kagugoroku(bot))