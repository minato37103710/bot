import discord
from discord.ext import commands,tasks


intent=discord.Intents.all()

class Help(commands.HelpCommand):
    def __init__(self):
        super().__init__()
        self.no_category = "カテゴリ未設定"
        self.command_attrs["description"] = "コマンドリストを表示します。"
    # ここでメソッドのオーバーライドを行います。

bot = commands.Bot(command_prefix="!",intents=intent,help_command=Help(),
    description="ヘルプコマンドの説明用BOT")

bot.author_id=757106917947605034

bot.load_extension('jishaku')

bot.load_extension("turuhashicogs.weakup")

bot.run('ODcwMTI0NTQxMjcwMTcxNzgw.YQIMoA._6BZr1uWoWWAvF6j7JKWBxKu3TU')
