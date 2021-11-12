import qrcode
import discord
from discord.ext import commands

class qrcodemaker(commands.Cog):
    def __init__(self,bot):
         self.bot=bot

    @commands.command(name='make_qr',aliases=['mkqr'])
    async def qrcodemake(self,ctx,*,url):
        img = qrcode.make(arg)
        print(arg)
        print(type(img))
        print(img.size)
        # <class 'qrcode.image.pil.PilImage'>
        # (290, 290)
        img.save('cogs/img/_qrcode.png')
        await ctx.send(file=discord.File('cogs/img/_qrcode.png'))

def setup(bot):
    bot.add_cog(qrcodemaker(bot))
