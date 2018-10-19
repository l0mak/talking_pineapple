import discord
from discord.ext import commands

class test():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send('da-da, ya')
                    
def setup(bot):
    bot.add_cog(test(bot))