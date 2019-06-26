import discord
from discord.ext import commands
import aiohttp
import io
import random
import re
import asyncio
from asyncio.tasks import sleep

#from discord.utils import get


class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def other(self, ctx):    
        embed = discord.Embed(title="**¯ \ _ (°\_o) \_ / ¯**", description="такие дела", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="**;guess**",
                        value="Игра низкой степни веселости.", inline=False)
        embed.add_field(name="**;shippering ;shipping ;pairing**",
                        value='''Дает двум случайным Ананасикам право не скрывать впредь своих чувств! 
                                ***По заказу <@!197381022118051840>***''', inline=False)
        embed.add_field(name="**;countdown**", value="РЧ на пулл!", inline=False)
        embed.add_field(name="**;defence**", value="Защитный кисулькен!", inline=False)
        embed.add_field(name="**;ping**", value="Ping urself! Ой! Простите...", inline=False)
        embed.add_field(name="**;author**", value="Дает Вам представление о человеке, пишущем Бота.", inline=False)
#        embed.add_field(name="**;add X Y**", value="Сложение **X** и **Y** где **X** и **Y** натуральные числа", inline=False)
#        embed.add_field(name="**;multiply X Y**", value="Умножение **X** и **Y** где **X** и **Y** натуральные числа", inline=False)
#        embed.add_field(name="**;saythanks**", value='''Ссылка на самый благодарный аддон в игре!
#                                               Disclaimer: многие игроки на него негативно реагируют!''', inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['shipping', 'pairing'])
    @commands.cooldown(1, 720, commands.BucketType.guild)
    async def shippering(self, ctx):
            ulist = []
            for user in ctx.channel.members:
                if user.status != discord.Status.offline and user.bot == False:
                    ulist.append(user)
            randomUser = random.choice(ulist)
            ulist1 = []
            for user in ctx.channel.members:
                if user.status != discord.Status.offline and user.bot == False and user != randomUser:
                    ulist1.append(user)            
            if len(ulist1) == 0:
               await ctx.send('''Ой-ой! Что-то пошло не так и я не смог выбрать второго ананасика! Вызвайте экзорциста! Или Вы надо мной подтруниваете и решили проверить вызову ли я Вас дважды если Вы один в канале?! Хитро (нет)''')
            else:
                randomUser1 = random.choice(ulist1)
                await ctx.send(f'{randomUser.name} и...')
                await sleep(1)
                await ctx.send(f'...{randomUser1.name}! Нет лучше пары в Ордорейде!')

    @commands.command()
    async def countdown(self, ctx):
        countdown = ['Пять!', 'Четыре!', 'Три!', 'Два!', 'Один!']
        for num in countdown:
            await ctx.send('**{0}**'.format(num))
            await asyncio.sleep(1)
        await ctx.send('**За Ананасиков!**')

    @commands.command()
    async def guess(self, ctx):
        await ctx.send('Угадайте число от 1 до 5')
        def is_correct(m):
            return m.author == ctx.author and m.content.isdigit()
        answer = random.randint(1, 5)
        try:
            guess = await self.bot.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await ctx.send('Простите! Вы слишком долго думали! Ответ был {}.'.format(answer))
        if int(guess.content) == answer:
            await ctx.send('Вы большой молодец!')
        else:
            await ctx.send('Вы не угадали! Ответ был {}.'.format(answer))


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
        await ctx.send('Pong!')

    @commands.command()
    async def author(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://i.imgur.com/jH1LRM0.jpg') as resp:
                if resp.status != 200:
                    await ctx.send('Ой-ой! Не могу загрузить картинку!')
                    return 
                else:
                    data = io.BytesIO(await resp.read())
                    await ctx.send(file=discord.File(data, 'pic.png'))

    @commands.command()
    async def defence(self, ctx, *name):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://s011.radikal.ru/i318/1611/88/10a8427ad95f.gif') as resp:
                if resp.status != 200:
                    await ctx.send('Ой-ой! Не могу загрузить защитную картинку!')
                    return 
                else:
                    data = io.BytesIO(await resp.read())
                    strnames = "".join( repr(e) for e in name)
                    def_object = re.sub('[^A-Za-z0-9А-Яа-я!,.<>@ %]+', ' ', strnames )
                    await ctx.send(f'Протокол защиты {def_object} активирован!')
                    await ctx.send(file=discord.File(data, 'pic.gif'))
#                    await ctx.message.delete()

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
#        await ctx.send('Оу! Аддон же еще! Вот ссылка - <https://yadi.sk/d/zcgFOHZb0isZIw> ')


def setup(bot):
    bot.add_cog(other(bot))
