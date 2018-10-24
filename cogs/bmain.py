import discord
from discord.ext import commands
import random
import asyncio
from asyncio.tasks import sleep
import io
import aiohttp

class bmain():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):    
        embed = discord.Embed(title="Привет!", description="Я Говорящий Ананасик! На самом деле пока я не умею говорить! Надеюсь скоро™ смогу. Сейчас я умею:", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="**;thot ;guild**", value="Информация о любимой гильдии Господина Ананасика", inline=False) 
        embed.add_field(name='**;userinfo <username>**', value='Информация об Ананасике', inline=False) 
        embed.add_field(name='**;voice**', value='Информация о голосовых возможностях бота. Все очень плохо...', inline=False)       
#        embed.add_field(name="**;add X Y**", value="Сложение **X** и **Y** где **X** и **Y** натуральные числа", inline=False)
#        embed.add_field(name="**;multiply X Y**", value="Умножение **X** и **Y** где **X** и **Y** натуральные числа", inline=False)
#        embed.add_field(name="**;ping**", value="Ping urself! Ой! Простите...", inline=False)
        embed.add_field(name="**;bosslist ;bossiques ;listboss**", value="Список имен боссов по которым можно получить тактику", inline=False)
#        embed.add_field(name="**;<boss_name>**", value="Тактика на босса.", inline=False)
        embed.add_field(name="**;random ;roll ;rand** ", value='''**;roll** Случайное чилсо от 0 до 100. 
                                                                **;roll X Y** Случайное число в конкретном диапазоне. 
                                                                **;roll coin** Монетка. 
                                                                **;roll user** Случайный Ананасик.''', inline=False)
        embed.add_field(name="**;shippering ;shipping ;pairing**", value='''Дает двум случайным Ананасикам право не скрывать впредь своих чувств! Найдите друг друга в игре, обнимитесь и совершите любой подвиг, достойный героев Ордорейда!
                                                                            ***По заказу <@!197381022118051840>***''', inline=False)
        embed.add_field(name="**;countdown**", value="РЧ на пулл!", inline=False)
        embed.add_field(name="**;author**", value="Дает Вам представление о человеке, пишущем Бота.", inline=False)
#        embed.add_field(name="**;saythanks**", value="Ссылка на самый благодарный аддон в игре! Disclaimer: многие игроки на него негативно реагируют!", inline=False)
        embed.add_field(name="**;info**", value="Вызов справки по Боту.", inline=False)
        embed.add_field(name="**;help**", value="Вызов этого сообщения.", inline=False)
        embed.set_footer(text="Отдельная благодарность господину Суи...")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['guild'])
    async def thot(self, ctx):    
        embed = discord.Embed(title="**Two Healers One Tank**", description="Два Лекаря Один Танк - гильдия Ананасиков с различных имиджборд.", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="**Фракция**", value="Орда", inline=False)
        embed.add_field(name="**Сервер**", value="Twisting Nether", inline=False)
        embed.add_field(name="**РТ**", value="Каждую пятницу, субботу и воскресенье в вечернее время. Подробнее в #info в дискорде ", inline=False)
        embed.add_field(name="**WoWprogress**", value='[Link](https://www.wowprogress.com/guild/eu/twisting-nether/Two+Healers+One+Tank)', inline=False)
        embed.add_field(name="**Информация**", value='''Мы ходим вместе в рейды и ключики, делаем ачивки и просто весело проводим время в игре.
                                                    Рады всем ананасикам независимо от уровня игры. С нами играют и ньюфаги, и хардкорные рейдеры, и поехавшие сычи-солоплееры и казуальные битурды. Всех нас объединяет желание рейдить с анонами.
                                                    Из-за того что модератор удаляет наши посты в треде, мы перенесли всю кооперацию в дискорд:
                                                    https://discord.gg/XJVagge - обязательно заходите, мы рады всем.''', inline=False)
        embed.add_field(name="**Правила**", value='''**Быть аноном**
                                                **Не обижать других ананасиков**
                                                **Посещение рейдов полностью свободное, но в рейд нужно приходить готовыми и стараться, а не надеяться, что тебя протащат и подарят лутеш.**
                                                ***В обычную сложность необходим 335 илвл, в героическую - 350***''', inline=False)
        embed.add_field(name="**Как попасть**", value='''Чтобы попасть в рейд, зайдите в «Заранее собранные группы - Другое – Ордорейд» в назначенное время. Пароль – название борды.
                                                    В нормал, героик и ключи вы можете ходить персонажами с любого сервера.
                                                    В рейды эпохальной сложности – только персонажем с сервера Twisting Nether или ждать межсерверные мифики.
                                                    Изменения в расписании и анонсы дополнительных рейдов в #info и #lfg дискорда.''', inline=False)
        embed.add_field(name="**Battle.tag для связи**", value='''Sprotae#2918
                                                            Fluttershy#2165
                                                            Tinkeron#1337''', inline=False)
        embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд [discord.gg/XJVagge]")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def author(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://i.imgur.com/jH1LRM0.jpg') as resp:
                if resp.status != 200:
                    return await ctx.send('Ой-ой! Не могу загрузить картинку!')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'cool_image.png'))
#        await ctx.send("https://imgur.com/gallery/jH1LRM0")
#        await ctx.send(file=discord.File('https://i.imgur.com/jH1LRM0.jpg'))
        
#    @commands.command()
#    async def add(self, ctx, a: int, b: int):
#        await ctx.send(a+b)

#    @commands.command()
#    async def multiply(self, ctx, a: int, b: int):
#        await ctx.send(a*b)        

    @commands.command(aliases=['rand', 'roll'])
    async def random(self, ctx, *arg):
        if ctx.invoked_subcommand is None:
            if not arg:
                start = 1
                end = 100
            elif arg[0] == 'flip' or arg[0] == 'coin':
                coin = ['Альянс', 'Орда']
                await ctx.send(f':thinking: {random.choice(coin)}')
                return
            elif arg[0] == 'user':
                members = ctx.message.guild.members
                randomuser = random.choice(members)
                if ctx.channel.permissions_for(ctx.author).mention_everyone:
                    user = randomuser.mention
                else:
                    user = randomuser.display_name
                await ctx.send(f'{user}! RNG избрал Вас!')
                return
            elif len(arg) == 1:
                start = 1
                end = int(arg[0])
            elif len(arg) > 1:
                start = int(arg[0])
                end = int(arg[1])
            await ctx.send(f':thinking: Случайное число ({start} - {end}): {random.randint(start, end)}')

    @commands.command(aliases=['shipping', 'pairing'])
    @commands.cooldown(1, 6000, commands.BucketType.user)
    async def shippering(self, ctx):
            members = ctx.message.guild.members
            membersonline = members
            randomuser1 = random.choice(membersonline)
            randomuser2 = random.choice(membersonline)
            await ctx.send(f'{randomuser1.mention}...')
            await sleep(3)
            await ctx.send(f'...и {randomuser2.mention}! Нет лучше пары в Ордорейде!')

    @commands.command()
    async def countdown(self, ctx):
        countdown = ['Пять!', 'Четыре!', 'Три!', 'Два!', 'Один!']
        for num in countdown:
            await ctx.send('**{0}**'.format(num))
            await asyncio.sleep(1)
        await ctx.send('**За Орду! За Ананасиков! За Выдроликого!**')

#    @commands.command()
#    async def saythanks(self, ctx): 
#        await ctx.send('Спасибо!')
#        await sleep(5)
#        await ctx.send('Оу! Аддон же еще! Вот ссылка - <https://yadi.sk/d/zcgFOHZb0isZIw> Простите...')
     
    @commands.command()
    async def userinfo(self, ctx, *, name=''):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                user = ctx.guild.get_member(int(name))
            if not user:
                user = self.bot.get_user(int(name))
            if not user:
                await ctx.send(self.bot.bot_prefix + 'Не могу найти такого Ананасика!')
                return
        else:
            user = ctx.message.author
        if user.avatar_url_as(static_format='png')[54:].startswith('a_'):
            avi = user.avatar_url.rsplit("?", 1)[0]
        else:
            avi = user.avatar_url_as(static_format='png')
        if isinstance(user, discord.Member):
            role = user.top_role.name
            if role == "@everyone":
                role = "Не знает свою роль..."
        embed = discord.Embed(title='**А не тинкерон ли Вы часом?**', colour=0xa500ff)
        embed.add_field(name='ID Ананасика', value=user.id, inline=True)
        embed.add_field(name='Имя Ананасика', value=user.name, inline=True)
        embed.add_field(name='Ник Ананасика', value=user.nick, inline=True)
        embed.add_field(name='Статус', value=user.status, inline=True)
        embed.add_field(name='Роль', value=role, inline=True)
        embed.add_field(name='Аккаунт Ананасика создан', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.add_field(name='Ананасик с нами', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.set_thumbnail(url=avi)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(bmain(bot))
