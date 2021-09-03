import discord
from discord.ext import commands
import typing
from tinydb import TinyDB, Query

db=TinyDB('color.json')

use = Query()

class Dropdown(discord.ui.Select):
    def __init__(self):

        # ドロップダウン内に表示されるオプションを設定します。
        options = [
            discord.SelectOption(label='ハトマル', description='ハトマルの説明はありません'),
            discord.SelectOption(label='Green', description='Your favourite colour is green', emoji='🟩'),
            discord.SelectOption(label='Blue', description='Your favourite colour is blue', emoji='🟦')
        ]

        # プレースホルダーは、オプションが選択されなかった場合に表示されるものです。
        # 最小値と最大値は、3つの選択肢の中から1つしか選べないことを示しています。
        # optionsパラメータは、ドロップダウンのオプションを定義します。上記で定義した
        super().__init__(placeholder='国を選択してください', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's 
        # selected options. We only want the first one.
        await interaction.response.send_message(f'{interaction.user.display_name} favourite colour is {self.values[0]}')
        if len(db.search(use.name == interaction.user.id))<=0:
            db.insert({'name':interaction.user.id , 'color':self.values[0]})
        else:
            db.update({'color':self.values[0]}, use.name == interaction.user.id)
class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())

class selects(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name='select')
    async def _select(self,ctx):
      view = DropdownView()

    # Sending a message containing our view
      await ctx.send('Pick your favourite colour:', view=view)

def setup(bot):
    bot.add_cog(selects(bot))
