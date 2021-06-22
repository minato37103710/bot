import discord
from discord.ext import commands

class member(commands.Cog):
    """These are the developer commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ninzu')
    async def ninzu(self,ctx):
      kagueto=ctx.guild.get_role(625524533947924522)
      hatomaru=ctx.guild.get_role(635841540044095492)
      runeraito=ctx.guild.get_role(633182520531222544)
      gekka=ctx.guild.get_role(656629831550631948)
      fianos=ctx.guild.get_role(695178946668527696)
      rathiberuku=ctx.guild.get_role(749525902261616670)
      kurarus=ctx.guild.get_role(856904704163840000)
      await ctx.send(f'カグエト:{len(kagueto.members)}\nクラルス:{len(kurarus.members)}\nはとまる:{len(hatomaru.members)}\nルネライト:{len(runeraito.members)}\n月華:{len(gekka.members)}\nフィアノス:{len(fianos.members)}\nラティベルク:{len(rathiberuku.members)}')

    @commands.group(name='member')
    async def member(self,ctx):
      if ctx.invoked_subcommand is None:
        embed=discord.Embed(title='国家識別番号リスト',description='カグエト:1\nはとまる:3\nルネライト:4\n月華:5\nフィアノス:6\nラティベルク:7')
        embed.set_footer(text='member 国家識別番号　で人数を取得できます')
        await ctx.send(embed=embed)
    
    @member.command(name='1')
    async def kagueto(self,ctx):
      kagueto=ctx.guild.get_role(625524533947924522)
      await ctx.send(f'カグエト:{len(kagueto.members)}')

    @member.command(name='2')
    async def kurarus(self,ctx):
      kagueto=ctx.guild.get_role(856904704163840000)
      await ctx.send(f'クラルス:{len(kagueto.members)}')

    @member.command(name='3')
    async def hatomaru(self,ctx):
      hatomaru=ctx.guild.get_role(635841540044095492)
      await ctx.send(f'はとまる:{len(hatomaru.members)}')

    @member.command(name='4')
    async def runeraito(self,ctx):
      runeraito=ctx.guild.get_role(633182520531222544)
      await ctx.send(f'ルネライト:{len(runeraito.members)}')

    @member.command(name='5')
    async def gekka(self,ctx):
      gekka=ctx.guild.get_role(656629831550631948)
      await ctx.send(f'月華:{len(gekka.members)}')

    @member.command(name='6')
    async def fianos(self,ctx):
      fianos=ctx.guild.get_role(695178946668527696)
      await ctx.send(f'フィアノス:{len(fianos.members)}')

    @member.command(name='7')
    async def rathiberuku(self,ctx):
      rathiberuku=ctx.guild.get_role(749525902261616670)
      await ctx.send(f'ラティベルク:{len(rathiberuku.members)}')

def setup(bot):
	bot.add_cog(member(bot))