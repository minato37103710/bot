import discord
from discord.ext import commands,tasks


intent=discord.Intents.all()

prefix='t!'

class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (f"各コマンドの説明: {prefix}help <コマンド名>\n"
                f"各カテゴリの説明: {prefix}help <カテゴリ名>\n")


bot = commands.Bot(command_prefix=prefix,intents=intent,help_command=JapaneseHelpCommand(),
    description="ヘルプコマンドの説明用BOT")

bot.author_id=757106917947605034

bot.load_extension('jishaku')

bot.load_extension("turuhashicogs.weakup")

bot.run('ODcwMTI0NTQxMjcwMTcxNzgw.YQIMoA._6BZr1uWoWWAvF6j7JKWBxKu3TU')
