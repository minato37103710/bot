import discord
from discord.ext import commands
from time import monotonic
import asyncio
import sys
import json
import aiofiles
import traceback
from tinydb import TinyDB, Query
from typing import List
from datetime import datetime
import discord

inten = discord.Intents.default()

intent = discord.Intents.all()

db=TinyDB('db.json')

User = Query()

bot = commands.Bot(command_prefix=','  # 定義した関数を渡しています
,
  cose_insensitive=True
,
  intents=intent
,
  help_command=None
)

bot.author_id = 757106917947605034

@bot.event
async def on_ready():
    print('------------')
    print(bot.user)
    print('online')
    print('------------')

@bot.event
async def on_member_join(member):
    print('ok')
    await channel.send(f'{member.mention}が入室しました')

@bot.event
async def on_message(message):
    if message.content == "タイマーボット":
        if message.guild: # 送信場所がDMだったら
            dm=discord.Embed(title=f'hi!.{message.author.name}',description="どうしたの？")
            dm.add_field(name='prefix忘れた？',value='そしたら[ここをクリックまたはタップしてね！](https://discord.gg/vZx52HvUYU)')
            await message.author.send(embed=dm)# メッセージ送信者に送信
            print(message.author.name)
            print(message.guild.id)
            print(message.author.guild)
    await bot.process_commands(message)

embed = discord.Embed(
    title="title",
    description="description",
    timestamp=datetime.now()
)

@bot.command()
async def memo(ctx,h):
    db.insert({'name':name,'age': h})
    await ctx.send(f'{h}を{name}として保存しました')

@bot.command()
async def out(ctx,p):
    n = db.search(User.name==p)
    await ctx.send(f"{n[0]['name'],n[0]['age']}")

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(embed=discord.Embed(title='error',description=f'```{error_msg}```',timestamp=datetime.now()))
    print(error_msg)
    print(ctx.author.guild)

@bot.command()
async def about(ctx):
    about = await ctx.send(embed=discord.Embed(title='loading...',description=''))
    await about.edit(embed=discord.Embed(title='timer bot stutas',description=f"{len(bot.guilds)}"))

@bot.command()
async def suggestion(ctx,*,arg):
    ch = bot.get_channel(826124044113018880)
    await ch.send(arg)
    await ch.send(ctx.author.guild)
    chack = "\N{WHITE HEAVY CHECK MARK}"
    await ctx.message.add_reaction(chack)

@bot.command()
async def my_avatar(ctx):
    avatar=discord.Embed(title='your_avatr',description=f"[this]({ctx.author.avatar_url})")
    avatar.set_thumbnail(url=ctx.author.avatar_url)
    ava = await ctx.send(embed=discord.Embed(title="searching for now",description=''))
    await asyncio.sleep(5)
    await ava.edit(embed=avatar)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send('good bye')
    await sys.exit()

@bot.command()
async def member(ctx):
    mes = '\n'.join([m.name for m in ctx.guild.members])
    lod = await ctx.send(embed=discord.Embed(title='loading',description=''))
    await asyncio.sleep(5)
    await lod.edit(embed=discord.Embed(title='メンバーの名前一覧',description=f'`{mes}`',color=discord.Color.random()))
    print(ctx.author.guild)
    print(mes)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, reason=None):
    kicknoti = discord.Embed(title='メンバーをキックしました', description='Kickしたメンバーにまた来てもらうには再招待してください', color=discord.Color.red())
    kicknoti.add_field(name='執行人', value=f'{ctx.author.mention}')
    kicknoti.add_field(name='Kickされた人', value=f'{member.mention}')
    kicknoti.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=kicknoti)
    await member.kick(reason=reason)

class PagerWithEmojis:
    """
    受け取った絵文字によってページを移動するためのクラス
    """
    LEFT_ARROW: str = "\N{LEFTWARDS BLACK ARROW}\N{VARIATION SELECTOR-16}"
    RIGHT_ARROW: str = "\N{BLACK RIGHTWARDS ARROW}\N{VARIATION SELECTOR-16}"
    STOP: str = "\N{CROSS MARK}"
    # 処理に必要な絵文字を変数として持っておく

    def __init__(self, pages:List[discord.Embed]):
        self.page_index: int = 0
        self.pages: List[discord.Embed] = pages

    @property
    def now_page(self) -> discord.Embed:
        return self.pages[self.page_index]

    @property
    def max_page_index(self) -> int:
        return len(self.pages) - 1

    @property
    def page_emojis(self) -> List[str]:
        """
        現在ページを出力する際に追加する必要のある絵文字のリストを返します。
        """
        emojis: List[str] = [self.LEFT_ARROW,self.RIGHT_ARROW,self.STOP]
        if self.page_index == 0:
            # もし、今最初のページにいるなら左へ移動する絵文字を除外する
            emojis.remove(self.LEFT_ARROW)
        if self.page_index == self.max_page_index:
            # もし、今最後のページにいるなら右へ移動する絵文字を除外する
            emojis.remove(self.RIGHT_ARROW)
        return emojis

    def move_page_by_emoji(self, emoji: str):
        """
        絵文字を受け取って、参照するページを変更します。
        """
        if emoji == self.LEFT_ARROW:
            self.page_index -= 1
        elif emoji == self.RIGHT_ARROW:
            self.page_index += 1
        elif emoji == self.LEFT_ARROW:
            self.page_index -= 1
        elif emoji == self.RIGHT_ARROW:
            self.page_index += 1
        elif emoji == self.LEFT_ARROW:
            self.page_index -= 1
        elif emoji == self.RIGHT_ARROW:
            self.page_index += 1
        elif emoji == self.LEFT_ARROW:
            self.page_index -= 1
        elif emoji == self.RIGHT_ARROW:
            self.page_index += 1
    async def discord_pager(self, ctx: commands.Context):
        """
        コマンドのContextを受け取って、Discord上でページ移動の受付・処理を行います。
        """
        now_page = self.now_page
        emojis = self.page_emojis
        # 現在ページ内容と、出力に必要な絵文字を取得
        msg: discord.Message = await ctx.send(embed=now_page)

        for emoji in emojis:
            await msg.add_reaction(emoji)

        def check(reaction: discord.Reaction, user: discord.User) -> bool:
            # リアクション先のメッセージや追加された絵文字が適切かどうか判断する。
            return str(reaction.emoji) in emojis and reaction.message == msg and user == ctx.author

        while True:
            reaction, _ = await ctx.bot.wait_for("reaction_add",check=check)
            await msg.clear_reactions()  # 事前に全てのリアクションを削除しておく。
            if str(reaction.emoji) == self.STOP:
                # 停止用の絵文字が追加された場合、リアクションを新たに付与することなく終了する。
                break
            self.move_page_by_emoji(str(reaction.emoji))
            now_page = self.now_page
            emojis = self.page_emojis
            await msg.edit(embed=now_page)
            

            for emoji in emojis:
                await msg.add_reaction(emoji)

@bot.command()
async def help(ctx: commands.Context):
    
    pages: list[discord.Embed] = [
        discord.Embed(
            title="ping",
            description='`>ping`\nBOTのpingが確認できます',
            color=discord.Color.random()
        ),
        discord.Embed(
            title="timers",
            description="`>timers <実行したい秒数>`\nタイマーを秒単位で実行できます",
            color=discord.Color.random()
        ),
        discord.Embed(
            title="timerm",
            description="`>timerm <実行したい分数>\nタイマーを分単位で実行できます",
            color=discord.Color.random()
        ),
        discord.Embed(
            title="my_avatar",
            description="じぶんのアイコンURLを取得できます",
            color=discord.Color.random()
        ),
        discord.Embed(
            title="kick",
            description="`(各鯖のprefix)kick <user id>`\nキックができます。",
            color=discord.Color.random()
        ),
                discord.Embed(
            title='suggestion',
            description="botのオーナーにメッセージを送ることができます",
            color=discord.Color.random()
        )
    ]
    pager = PagerWithEmojis(pages)
    await pager.discord_pager(ctx)

extensions = [
    'cogs.timer'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)

extensions = [
    'cogs.eval'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)

extensions = [
    'cogs.ping'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)

extensions = [
    'cogs.dev'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)

bot.run('ODAyNjk4MzE4MzY3MDMxMjk2.YAzBEA.kRAnyRmg10SvkT4bswJZwxL8tfE')