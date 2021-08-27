import discord
from discord.ext import commands,tasks


intent=discord.Intents.all()
prefix = 'T!'


class Greet(commands.Cog, name='あいさつ'):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="こんにちは")
    async def hello(self, ctx):
        """出会いのあいさつをする"""
        await ctx.send(f"どうも、{ctx.author.name}さん!")

    @commands.command(name="さようなら")
    async def goodbye(self, ctx):
        """別れの挨拶をする"""
        await ctx.send(f"じゃあね、{ctx.author.name}さん!")


class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (f"各コマンドの説明: {prefix}help <コマンド名>\n"
                f"各カテゴリの説明: {prefix}help <カテゴリ名>\n")

    @bot.event
    async def on_command_error(ctx, error):
      if isinstance(error,commands.errors.CommandNotFound):
          await ctx.send("エラー！") 

    
bot = commands.Bot(command_prefix=prefix, help_command=JapaneseHelpCommand(),intents=intent)
bot.add_cog(Greet(bot=bot))

bot.author_id=757106917947605034

bot.load_extension('jishaku')

bot.load_extension("turuhashicogs.weakup")

bot.run('ODcwMTI0NTQxMjcwMTcxNzgw.YQIMoA._6BZr1uWoWWAvF6j7JKWBxKu3TU')
