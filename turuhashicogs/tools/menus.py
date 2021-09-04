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
        
        if len(db.search(use.country == self.values[0])) <=0:
            await interaction.user.send(f'説明が登録されていません{self.values[0]}の国王にお問い合わせください')
        else:
            descr=db.search(use.country == self.values[0])
            await interaction.user.send(descr)

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

        
    @commands.command(name='description_add')
    async def add(self,ctx,country,description):
        if len(db.search(use.country == country))<=0:
            db.insert({'country':country,'description':description})
            await ctx.send('ok')
        else:
            db.update({'description':description}, use.country == country)
            await ctx.send('ok')
            
def setup(bot):
    bot.add_cog(selects(bot))
