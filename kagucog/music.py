import asyncio
from discord.ext import commands
import discord
import youtube_dl
from collections import deque
# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class music(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      self.d = deque()
    @commands.group()
    async def music(self, ctx):
      if ctx.invoked_subcommand is None:
          await ctx.send('メインコマンドの後にサブコマンドが必要です。')
    
    @music.command()
    async def join(self, ctx):
      if ctx.author.voice is None:
          await ctx.channel.send("あなたはボイスチャンネルに接続していません。")
          return
        # ボイスチャンネルに接続する
      await ctx.author.voice.channel.connect()
      await ctx.send("接続しました。")
    
    @music.command()
    async def leave(self, ctx):
      if ctx.guild.voice_client is None:
            await ctx.send("接続していません。")
            return
      if ctx.guild.voice_client.is_playing():
            await ctx.send("再生中です。")
            return
      self.d.clear()
      await ctx.guild.voice_client.disconnect()
      await ctx.send("切断しました。")
    
    async def play_only(self, ctx):
            urls = self.d[0]
            player = await YTDLSource.from_url(urls, loop=self.bot.loop)
            embed=discord.Embed(title="音楽キューシステム",description=f"キューリストに追加されました。" ,color=0xff0000)
            embed.add_field(name="音楽名",value=f"{urls}",inline=False)
            await ctx.send(embed=embed)
            return ctx.guild.voice_client.play(player, after=lambda _:self.bot.loop.create_task(self.play_end(ctx)))
    
    async def play_end(self, ctx):
            self.d.popleft()
            if len(self.d) == 0:
                return await ctx.send("キューの中身が空になりました。再生を終了します。")
            else:
                await ctx.send("次の曲を再生します。")
                return self.play_only(ctx)
    
    @music.command()
    async def play(self, ctx,*,message):
      # youtubeから音楽をダウンロードする
      if ctx.guild.voice_client is None:
            await ctx.channel.send("接続していません。")
            return
      url = message
      self.d.append(url)
      await ctx.send("キューに追加しました。")
      if len(self.d) == 1:
        await self.play_only(ctx)
    @music.command()
    async def pause(self, ctx):
      if ctx.guild.voice_client is None:
          await ctx.send("接続していません。")
          return

      # 再生中ではない場合は実行しない
      if not ctx.guild.voice_client.is_playing():
        await ctx.send("再生していません。")
        return
      ctx.guild.voice_client.stop()
      await ctx.send("再生中の曲を中断しました。")

    @music.command()
    async def resume(self, ctx):
      if ctx.guild.voice_client is None:
          await ctx.send("接続していません。")
          return
      if not ctx.guild.voice_client.stop():
        ctx.send("再生中です。")
      await self.play_only(ctx)
      await ctx.send("再生します。")
    @music.command()
    async def list(self, ctx):
      if len(self.d) == 0:
        await ctx.send("キューには何も入っていません。")
      else:
        await ctx.send(f"```{self.d}```")
    @music.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("ボイスチャンネルに接続していません。")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("音量を{}%に変更しました。".format(volume))
  


def setup(bot):
  return bot.add_cog(music(bot))