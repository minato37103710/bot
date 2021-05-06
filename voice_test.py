import discord
import subprocess
import ffmpeg
from voice_generator import creat_WAV

client = commands.Bot(command_prefix='.')
voice_client = None

@client.event
async def on_ready():
    print('online')

@client.command()
async def join(ctx):
    #voicechannelを取得
    vc = ctx.author.voice.channel
    #voicechannelに接続
    await vc.connect()

@client.command()
async def bye(ctx):
    #切断
    await ctx.voice_client.disconnect()

@client.event
async def on_message(message: discord.Message):
    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return

    if message.content == "join":
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        # ボイスチャンネルに接続する
        await message.author.voice.channel.connect()
        await message.channel.send("接続しました。")

    elif message.content == "leave":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return

        # 切断する
            await message.guild.voice_client.disconnect()
            await message.channel.send("切断しました。")
    elif message.content == "play":
        if message.guild.voice_client is None:
           await message.channel.send("接続していません。")
           return
        message.guild.voice_client.play(discord.FFmpegPCMAudio("example.mp3"))
    
    if message.content.startswith('.'):
        pass

    else:
        if message.guild.voice_client:
            print(message.content)
            creat_WAV(message.content)
            source = discord.FFmpegPCMAudio("output.wav")
            message.guild.voice_client.play(source)
        else:
            pass

client.run('ODMyNjExMDY2MDM4OTc2NTky.YHmTew.sceOFU7S5YrVHvNJTBRm7MgE02I')