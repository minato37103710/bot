import discord
from discord.ext import commands
import sys
import asyncio
import ast
from functools import partial
from tinydb import TinyDB,Query

db=TinyDB('db.json')

User=Query()

class dev_command(commands.Cog):
    """These are the developer commands"""

    def __init__(self, bot):
        self.bot = bot
    
    async def cog_check(self, ctx):  

		    return ctx.author.id == self.bot.author_id

    @commands.command(
		  name='reload',  # Name of the command, defaults to function name.
		  aliases=['rl']  # Aliases for the command.
	  )  
    async def reload(self, ctx, cog):

		    extensions = self.bot.extensions  
		    if cog == 'all':  # Lets you reload all cogs at once
			    for extension in extensions:
			    	self.bot.unload_extension(f'cogs.{cog}')
			    	self.bot.load_extension(f'cogs.{cog}')
			    await ctx.send('Done')
		    if cog in extensions:
			    self.bot.unload_extension(cog)  # Unloads the cog
			    self.bot.load_extension(cog)  # Loads the cog
			    await ctx.send('Done')  # Sends a message where content='Done'
		    else:
		    	await ctx.send('Unknown Cog')  # If the cog isn't found/loaded.
	
    @commands.command(name="unload", aliases=['ul']) 
    async def unload(self, ctx, cog):

		    extensions = self.bot.extensions
		    if cog not in extensions:
		    	await ctx.send("Cog is not loaded!")
		    	return
		    self.bot.unload_extension(cog)
		    await ctx.send(f"`{cog}` has successfully been unloaded.")
	
    @commands.command(name="load")
    async def load(self, ctx, cog):
      
		    try:

			    self.bot.load_extension(cog)
			    await ctx.send(f"`{cog}` has successfully been loaded.")

		    except commands.errors.ExtensionNotFound:
		    	await ctx.send(f"`{cog}` does not exist!")

    @commands.command(name="coglist",aliases=['lc'])
    async def listcogs(self, ctx):


		    base_string = "```css\n"  # Gives some styling to the list (on pc side)
		    base_string += "\n".join([str(cog) for cog in self.bot.extensions])
		    base_string += "\n```"
		    await ctx.send(base_string)

    @commands.command(name='guilds')
    async def guilds(self,ctx):
      await ctx.send(f'{self.bot.guilds}')
    
    @commands.command(name='test')
    async def test(self,ctx):
      count = 0
      count += 1
      print(count)
      db.update({'age':count}, User.name == ctx.author.id)

def setup(bot):
	bot.add_cog(dev_command(bot))