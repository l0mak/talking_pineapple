# import discord
# from discord import Status
# from discord import utils
from discord.ext import commands
# import random

from bs4 import BeautifulSoup

import requests


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def tt(self, ctx):
        wpage = 'https://www.wowhead.com'
        page = requests.get(wpage)
        soup = BeautifulSoup(page.text, 'html.parser')
        cont = soup.find_all(class_='tiw-blocks-status-progress')

        names = []
        for d in cont:
            names.append(d.contents)

        str_names = "".join( repr(e) for e in names)

        await ctx.send(str_names)


#    @commands.command()
#    async def test(self, ctx):

#        member = discord.utils.find(lambda m: m.name == 'l0mak', ctx.message.guild.members)
#        ulist = []
#        for user in ctx.channel.members:
#            if user.status != discord.Status.offline and user.bot == False:
#                ulist.append(user)
#        randomUser = random.choice(ulist)
#        user = randomUser.mention

#        if await ctx.bot.is_owner(ctx.author):
#            await ctx.send(f'{user}')
#        else:
#            await ctx.send('Эта команда предназначена для логирования и тестов. Боюсь, что ее может использовать только мой автор. Простите!')
        
                    
def setup(bot):
    bot.add_cog(Test(bot))
