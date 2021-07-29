
from discord.ext import commands

import discord

class CounterBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('$'))

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')



class Counter(discord.ui.View):

    @discord.ui.button(label='グー', style=discord.ButtonStyle.red)
    async def count(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='チョキ', style=discord.ButtonStyle.red)
    async def cou(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='パー', style=discord.ButtonStyle.red)
    async def cu(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=self)

counbot = CounterBot()

class count(commands.Cog):
    def __init__(self,counbot):
        self.bot=counbot
    @commands.command()
    async def counter(self,ctx: commands.Context):
        """Starts a counter for pressing."""
        await ctx.send('Press!', view=Counter())

def setup(bot):
    bot.add_cog(count(bot))