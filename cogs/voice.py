import discord
from discord.ext import commands
#from discord.voice_client import VoiceClient

class voice():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def voice(self, ctx):    
        embed = discord.Embed(title="Oora! Я учусь говорить!", description="Кого я обманываю...", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png')
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png")
        embed.add_field(name="**;test**", value="__", inline=False) 
        embed.add_field(name='**;adeek**', value='__', inline=False)       
        embed.add_field(name="**;theseller**", value='__', inline=False)
        embed.set_footer(text="Этот модуль пока не работает")
        await ctx.send(embed=embed)

#    @commands.command()
#    async def sum(self, ctx):
#        await self.bot.join(ctx.message.author.voice.voice_channel)
     
#    @commands.command(pass_context=True)
#    async def join(self):
#        author = ctx.message.author
#        channel = author.voice_channel
#        await self.bot.join_voice_channel('85112295897702400')      
      
def setup(bot):
    bot.add_cog(voice(bot))