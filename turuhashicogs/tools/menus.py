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
            discord.SelectOption(label='ハトマル', description='ハトマル国の説明が見れます'),
            discord.SelectOption(label='Green', description='Your favourite colour is green', emoji='🟩'),
            discord.SelectOption(label='Blue', description='Your favourite colour is blue', emoji='🟦')
        ]

        # プレースホルダーは、オプションが選択されなかった場合に表示されるものです。
        # 最小値と最大値は、3つの選択肢の中から1つしか選べないことを示しています。
        # optionsパラメータは、ドロップダウンのオプションを定義します。上記で定義した
        super().__init__(placeholder='国を選択してください', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # インタラクションオブジェクトを使用して、以下の内容のレスポンスメッセージを送信します。
        # は、ユーザーの好きな国や選択肢。自己のオブジェクトは、参照する
        # Selectオブジェクト、values属性は、ユーザーの 
        # 選択されたオプション 私たちは最初の1つだけが欲しいのです。
        await interaction.user.send(f'{interaction.user.display_name} favourite colour is {self.values[0]}')

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # ビューオブジェクトにドロップダウンを追加します。
        self.add_item(Dropdown())

class selects(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name='select')
    async def _select(self,ctx):
      view = DropdownView()

    # ビューを含むメッセージの送信
      await ctx.send('Pick your favourite colour:', view=view)

def setup(bot):
    bot.add_cog(selects(bot))
