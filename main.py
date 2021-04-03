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
inten = discord.Intents.default()

intent = discord.Intents.all()

db=TinyDB('db.json')

User = Query()

async def prefix_from_json(bot,message):
    """
    prefix.json を読み込んで該当するprefix（無ければ ! ）を返す。
    """

    async with aiofiles.open("prefix.json") as f:
        contents = await f.read()
    data = json.loads(contents)  # json形式として読み込む
    return data.get(str(message.guild.id),",")

bot = commands.Bot(command_prefix=prefix_from_json  # 定義した関数を渡しています
,
  cose_insensitive=True
,
  intents=intent
,
  help_command=None
,
  activity=discord.Game(f'標準prefixは[,]です。||  prefixを忘れてしまった場合は[タイマーボット]と発言してください。DMにてリセット方法をご案内します。||現在のBOT導入鯖数[{len(bot.guilds)}]')
  )

@bot.event
async def on_ready():
  print('------------')
  print(bot.user)
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
        if not message.guild:
            print('dm')
    await bot.process_commands(message)

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
    messa = await ctx.send(embed=discord.Embed(title='Geting an error.',description=''))
    await asyncio.sleep(0.5)
    await messa.edit(embed=discord.Embed(title='Geting an error..',description=''))
    await asyncio.sleep(0.5)
    await messa.edit(embed=discord.Embed(title='Geting an error...',description=''))
    await asyncio.sleep(0.5)
    await messa.edit(embed=discord.Embed(title='Geting an error.',description=''))
    await asyncio.sleep(0.5)
    await messa.edit(embed=discord.Embed(title='Geting an error..',description=''))
    await asyncio.sleep(0.5)
    await messa.edit(embed=discord.Embed(title='Geting an error...',description=''))
    await asyncio.sleep(1)
    await messa.edit(embed=discord.Embed(title='error',description=f'`{error_msg}`'))
    print(error_msg)
    print(ctx.author.guild)

@bot.command()
async def timerm(ctx,query):  #コマンドを判定
            await ctx.send("timer start")
            await asyncio.sleep(int(query) * 60)  #分を取得&60倍
            await ctx.send(embed=discord.Embed(title='timer finished',description=f'{int(query)}'))  #内容を変換

@bot.command()
async def timerh(ctx,query):  #コマンドを判定
            await ctx.send("timer start")
            await asyncio.sleep(int(query) * 3600)  #分を取得&60倍
            await ctx.send(embed=discord.Embed(title='timer finished',description=f'{int(query)}'))  #内容を変換

@bot.command()
async def timers(ctx,query):  #コマンドを判定
            await ctx.send(f"{ctx.author.name} is timer start")
            print(f'{ctx.guild}')
            await asyncio.sleep(int(query))  #分を取得&60倍
            await ctx.send(embed=discord.Embed(title='timer finished',description=f'{int(query)}'))  #内容を変換

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
async def my_status(ctx):
  status=discord.Embed(title='your status',description=f'{ctx.author.status}',color=discord.Color.random())
  await ctx.send(embed=status)

@bot.command()
async def my_guild(ctx):
  guil=discord.Embed(title='your guild',description=f'{ctx.author.guild}')
  await ctx.send(embed=guil)

@bot.command()
async def member(ctx):
  mes = '\n'.join([m.name for m in ctx.guild.members])
  lod = await ctx.send(embed=discord.Embed(title='loading',description=''))
  await asyncio.sleep(5)
  await lod.edit(embed=discord.Embed(title='メンバーの名前一覧',description=f'`{mes}`',color=discord.Color.random()))
  print(ctx.author.guild)
  print(mes)

@bot.command()
async def ping(ctx):
# Δt = t1 - t0 の t0 を定義する。
    t0 = monotonic()

        # Discord を通す関数を挟む。(応答速度)
    ping_message = await ctx.send(embed=discord.Embed(title="計算中...",description=' '))

        # Δt = t1 - t0, latency は ping 的な意味、応答速度。1000倍は、ms(ミリセカンド)にするため。
    latency = (monotonic() - t0) * 1000

        # 送っていたメッセージを編集。ここで、応答速度を表示する。int にしているのは、小数点を消すため。( int は整数値)
    await ping_message.edit(embed=discord.Embed(title=f"Pong! 応答速度**{int(latency)}** ms です。",color=discord.Color.random()))

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

@bot.command()
async def set_prefix(ctx,prefix):
    async with aiofiles.open("prefix.json") as f:
        contents = await f.read()
        data = json.loads(contents)  # json形式として読み込む
        before_prefix = data.get(str(ctx.guild.id),',')
        data[str(ctx.guild.id)] = prefix  # 辞書内で prefix を変更しておく

    async with aiofiles.open("prefix.json","w") as f:
        await f.write(json.dumps(data))  # 変更済みの辞書をjson形式で出力

    await ctx.send(f"prefixが {before_prefix} から {prefix} に変更されました。")
    print('prefix変更通知')


bot.run('ODAyNjk4MzE4MzY3MDMxMjk2.YAzBEA.kRAnyRmg10SvkT4bswJZwxL8tfE')