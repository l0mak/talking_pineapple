import discord
from discord.ext import commands
import aiohttp
import io
from discord.utils import get


class other():
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def other(self, ctx):    
        embed = discord.Embed(title="**¯\ (°_o)/¯**", description="Команды не связанные ни с ордорейдом, ни с игрой, ни с ботом:", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="**;ping**", value="Ping urself! Ой! Простите...", inline=False)
        embed.add_field(name="**;author**", value="Дает Вам представление о человеке, пишущем Бота.", inline=False)
        embed.add_field(name="**;echo**", value="Вы хотите выговориться, но при этом остаться анонимным? Введите команду в формате ;echo <channel_id> <text> и яскажу все за Вас", inline=False)
#        embed.add_field(name="**;add X Y**", value="Сложение **X** и **Y** где **X** и **Y** натуральные числа", inline=False)
#        embed.add_field(name="**;multiply X Y**", value="Умножение **X** и **Y** где **X** и **Y** натуральные числа", inline=False)
#        embed.add_field(name="**;saythanks**", value="Ссылка на самый благодарный аддон в игре! Disclaimer: многие игроки на него негативно реагируют!", inline=False)
        embed.set_footer(text="Этот модуль будет пополняться всяким шлаком")
        await ctx.send(embed=embed)

    @commands.command()
    async def echo(self, ctx, channel: str, *message: str):
        if await ctx.bot.is_owner(ctx.author):
            ch = self.bot.get_channel(int(channel))
            msg = ' '.join(message)
            await ch.send(msg)
            await ctx.message.delete()
        else:
            await ctx.send('Боюсь, что этой командой может пользоваться только мой автор. Простите!')

#    @commands.command()
#    async def react(self, ctx):
#        if await ctx.bot.is_owner(ctx.author):
#            await discord.Message.add_reaction(msg, 'Ⓜ️')
#            await ctx.message.delete()
#        else:
#            await ctx.send('Боюсь, что этой командой может пользоваться только мой автор. Простите!')

#    @commands.command()
#    async def quote(self, ctx, msg_id):
#        msg = await discord.utils.get_message(ctx.message.channel, msg_id)
#        await ctx.send('{0.timestamp} - {0.content}'.format(msg))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! :ananasique:')

    @commands.command()
    async def author(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://i.imgur.com/jH1LRM0.jpg') as resp:
                if resp.status != 200:
                    await ctx.send('Ой-ой! Не могу загрузить картинку!')
                    return 
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'pic.png'))
#        await ctx.send("https://imgur.com/gallery/jH1LRM0")
#        await ctx.send(file=discord.File('https://i.imgur.com/jH1LRM0.jpg'))

#    @commands.command()
#    async def add(self, ctx, a: int, b: int):
#        await ctx.send(a+b)

#    @commands.command()
#    async def multiply(self, ctx, a: int, b: int):
#        await ctx.send(a*b)        

#    @commands.command()
#    async def saythanks(self, ctx): 
#        await ctx.send('Спасибо!')
#        await sleep(5)
#        await ctx.send('Оу! Аддон же еще! Вот ссылка - <https://yadi.sk/d/zcgFOHZb0isZIw> Простите...')


def setup(bot):
    bot.add_cog(other(bot))
