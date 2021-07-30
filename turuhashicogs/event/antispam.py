import discord
from discord.ext import commands
import glob, random
from tinydb import TinyDB, Query
import asyncio
from tinydb import TinyDB, Query
from tinydb.operations import increment

db=TinyDB('spam.json')

User = Query()

class antispam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_message(self,msg):

        spamming_list = []

        if str(msg.author.id) not in spamming_list:
            
            try:
                
                spamming_list.append(str(msg.author.id))
                
                def checki(m):
                    return m.author == msg.author and m.channel == msg.channel
                
                respa = await self.bot.wait_for('message', timeout=0.6, check=checki)
                if respa:
                    respd = await self.bot.wait_for('message', timeout=0.6, check=checki)
                    if respd:
                        respe = await self.bot.wait_for('message', timeout=0.6, check=checki)
                        if respe:
                            respw= await self.bot.wait_for('message', timeout=0.6, check=checki)
                            if respw:
                                respq = await self.bot.wait_for('message', timeout=0.6, check=checki)
                                
                                def is_me(m):
                                    return m.author == msg.author

                                def bot(m):
                                    return m.author == self.bot.user

                                role=msg.guild.get_role(867046102455943199)
                                logch=self.bot.get_channel(870501783770910720)

                                await msg.author.add_roles(role)

                                if len(db.search(User.name==msg.author.id)) > 0:
                                    pass
                                
                                else: 
                                    db.insert({'name':msg.author.id, 'age':1})
                                
                                db.update(increment('age'), User.name == msg.author.id)
                                await msg.channel.purge(limit=12, check=is_me)
                                mes=await msg.channel.send(f"Stop spamming {msg.author.mention}")
                                await msg.author.send('Please stop spam')
                                await asyncio.sleep(5)
                                await msg.channel.purge(limit=4,check=bot)
                                count=db.search(User.name == msg.author.id)
                                log=discord.Embed(title='spam log')
                                log.add_field(name="spam user",value=f"{msg.author.name}\n{msg.author.id}")
                                log.add_field(name="spam count",value=f"{count[0]['name']}回")
                                await logch.send(embed=log)
                                  
                                
                                spamming_list.remove(str(msg.author.id))

            except asyncio.TimeoutError:
            
                spamming_list.remove(str(msg.author.id))
                return


def setup(bot):
    bot.add_cog(antispam(bot))