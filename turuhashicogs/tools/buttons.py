import discord
from discord.ext import commands
import random

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='✊', style=discord.ButtonStyle.green)
    async def goo(self, button: discord.ui.Button, interaction: discord.Interaction):
        j=['グー✊','チョキ✌','パー✋']
        a=random.choice(j)
        await interaction.send_message(f'{a}', ephemeral=True)
        self.value = False

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='✌', style=discord.ButtonStyle.grey)
    async def scissors(self, button: discord.ui.Button, interaction: discord.Interaction):
        j=['グー✊','パー✋','チョキ✌']
        a=random.choice(j)
        await interaction.send_message(f'{a}', ephemeral=True)
        self.value = False
        
    @discord.ui.button(label='✋', style=discord.ButtonStyle.grey)
    async def par(self, button: discord.ui.Button, interaction: discord.Interaction):
        j=['グー✊','パー✋','チョキ✌']
        a=random.choice(j)
        await interaction.send_message(f'{a}', ephemeral=True)
        self.value = False

class buttons(commands.Cog,name='ボタン'):
    
    def __init__(self,bot):
         self.bot=bot

    @commands.command(name='ask')
    async def ask(self,ctx: commands.Context):
      """Asks the user a question to confirm something."""
    # We create the view and assign it to a variable so we can wait for it later.
      view = Confirm()
      await ctx.send('Do you want to continue?', view=view)
    # Wait for the View to stop listening for input...
      await view.wait()
      if view.value is None:
        print('Timed out...')
      elif view.value:
        print('Confirmed...')
      else:
        print('Cancelled...')

def setup(bot):
  bot.add_cog(buttons(bot))
