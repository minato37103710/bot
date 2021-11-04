import discord
from discord.ext import commands
import glob, random
import asyncio


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
                                
                         
                                await msg.channel.purge(limit=12, check=is_me)
                                mes=await msg.channel.send(f"Stop spamming {msg.author.mention}")
                                await msg.author.send('Please stop spam')
                                await asyncio.sleep(5)
                                await msg.channel.purge(limit=4,check=bot)
                                log=discord.Embed(title='spam log')
                                log.add_field(name="spam user",value=f"{msg.author.name}\n{msg.author.id}")
                                await logch.send(embed=log)
                                  
                                
                                spamming_list.remove(str(msg.author.id))

            except asyncio.TimeoutError:
            
                spamming_list.remove(str(msg.author.id))
                return


def setup(bot):
    bot.add_cog(antispam(bot))
