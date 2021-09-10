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
            discord.SelectOption(label='ハトマル帝国', description='ハトマル帝国の説明が見れます'),
            discord.SelectOption(label='リネア王国', description='リネア王国の説明が見れます'),
            discord.SelectOption(label='ラードラネット王国', description='ラードラネット王国の説明が見れます'),
            discord.SelectOption(label='ネオ・ジオン', description='ネオ・ジオンの説明が見れます'),
            discord.SelectOption(label='ロック・フィア', description='ロック・フィアの説明が見れます'),
            discord.SelectOption(label='エル・ドラド社会主義国', description='エル・ドラド社会主義国の説明が見れます'),
            discord.SelectOption(label='エルネシア王国', description='エルネシア王国の説明が見れます'),
            discord.SelectOption(label='ジャンクフード王国', description='ジャンクフード王国の説明が見れます'),
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
            await interaction.user.send(descr[0]['description'])
            print(self.values[0])
class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # ビューオブジェクトにドロップダウンを追加します。
        self.add_item(Dropdown())

class selects(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name='pr')
    async def _select(self,ctx):
      view = DropdownView()

    # ビューを含むメッセージの送信
      await ctx.send('国を選択してください※サーバーメンバーからのダイレクトメッセージを許可してください', view=view)
        
    @commands.command(name='description_add',aliases=['des_add'])
    async def add(self,ctx,country,*,arg):
        role=ctx.guild.get_role(866287022082490398)
        if not role in ctx.author.roles:
            await ctx.send('Not enough of your permission')
            return
        if len(db.search(use.country == country))<=0:
            db.insert({'country':country,'description':arg})
            await ctx.send('ok')
        else:
            db.update({'description':description}, use.country == country)
            await ctx.send('ok')
            
def setup(bot):
    bot.add_cog(selects(bot))
