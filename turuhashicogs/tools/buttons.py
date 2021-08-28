import discord
from discord.ext import commands

class buttons(commands.Cog,name='ボタン'):
    
     def __init__(self,bot):
         self.bot=bot

     async def test_interaction(self,view, button, interaction):
    # Push me!が押されたら。
       await interaction.channel.send("Pushed button.")

     async def test_count(self,view, button, interaction):
    # 数字が押されたら。
       button.label = str(int(button.label) + 1)
       await interaction.message.edit(view=view)

     @commands.command(name="_componesy_test")
     async def test(self,ctx):
    # ViewをTestViewっていう名前で作る。
      view = componesy.View("TestView")
    # 上の二つを登録する。
      view.add_item("button", test_interaction, label="Push me!")
      view.add_item("button", test_count, label="0")
    # viewを送信する。
      await ctx.reply("test", view=view)

def setup(bot):
  bot.add_cog(buttons(bot))
