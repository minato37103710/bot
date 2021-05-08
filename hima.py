import discord
from discord.ext import commands

intent=discord.Intents.all()

bot = commands.Bot(command_prefix=','  # 定義した関数を渡しています
,
  cose_insensitive=True
,
  intents=intent
,
  help_command=True
)

@bot.event
async def on_ready():
    print('ok')

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

bot.run('ODQwNDQzNTM2NzA0Mjc0NDYz.YJYSCQ.WnBOMo8n1xro3TFUgLgpWbxUbUo')