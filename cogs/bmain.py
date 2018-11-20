import discord
from discord.ext import commands
import random
import asyncio
from asyncio.tasks import sleep


class bmain():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):    
        embed = discord.Embed(title="Привет!", description="Я Говорящий Ананасик! На самом деле пока я не умею говорить! Надеюсь скоро™ смогу. Сейчас я умею:", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="**;wt ;wf ;wq**", value="WowToken, Warfronts, WorldQuests", inline=False)
        embed.add_field(name="**;wowlinks ;uselesslinks**", value="Ссылки на никому не нужную информацию.", inline=False)
        embed.add_field(name="**;thot ;guild**", value="Информация о любимой гильдии Господина Ананасика.", inline=False) 
        embed.add_field(name="**;bosslist ;bossiques ;listboss**", value="Список подземелий по которым можно получить тактику.", inline=False)
        embed.add_field(name='**;userinfo <username>**', value='Информация об Ананасике. **<username> - @mention или ник Ананасика** (чувствительно к регистру). Просто **;userinfo** выдаст информацию о Вас', inline=False) 
        embed.add_field(name='**;serverinfo**', value='Информация о дискорд сервере Ордорейда.', inline=False)
        embed.add_field(name='**;choose X Y Z**', value='Случайный выбор из введенных вариантов (не больше 6; просто потому что!).', inline=False)
        embed.add_field(name="**;random ;roll ;rand** ", value='''**;roll** Случайное чилсо от 0 до 100. 
                                                                **;roll X Y** Случайное число в конкретном диапазоне. 
                                                                **;roll coin** Монетка. 
                                                                **;roll user** Случайный Ананасик.
                                                                ''', inline=False)
        embed.add_field(name="**;shippering ;shipping ;pairing**", value='''Дает двум случайным Ананасикам право не скрывать впредь своих чувств! Найдите друг друга в игре, обнимитесь и совершите любой подвиг, достойный героев Ордорейда!
                                                                            Доказавшие свой подвиг скриншотом Ананасики, получат по 1000 золотых на TN!
                                                                            ***По заказу <@!197381022118051840>***''', inline=False)
        embed.add_field(name="**;countdown**", value="РЧ на пулл!", inline=False)
        embed.add_field(name="**;info**", value="Вызов справки по Боту.", inline=False)
        embed.add_field(name="**;help**", value="Вызов этого сообщения.", inline=False)
        embed.add_field(name='**;voice**', value='Информация о голосовых возможностях бота. *Все очень плохо...*', inline=False)
        embed.add_field(name='**;other**', value='Прочие команды.', inline=False)       
        embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд")
        await ctx.send(embed=embed)

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
                ulist = []
                for user in ctx.channel.members:
                   if user.status != discord.Status.offline and user.bot == False:
                        ulist.append(user)
                randomUser = random.choice(ulist)
                user = randomUser.mention
                author = ctx.message.author.mention
                await ctx.send(f'{user}! RNG избрал Вас! Все вопросы к {author}! Я только посредник.')
                return
            elif len(arg) == 1:
                start = 1
                end = int(arg[0])
            elif len(arg) > 1:
                start = int(arg[0])
                end = int(arg[1])
            await ctx.send(f':thinking: Случайное число ({start} - {end}): {random.randint(start, end)}')

    @commands.command()
    async def choose(self, ctx, *choices : str):
        if len(choices) > 6:
            await ctx.send('Слишком сложно! Попробуйте ввести 6 или меньше вариантов!')
        else:
            await ctx.send(f':thinking: {random.choice(choices[:6])} - RNG боги сделали выбор!')

    @commands.command(aliases=['shipping', 'pairing'])
    @commands.cooldown(1, 7200, commands.BucketType.guild)
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
               await ctx.send('Ой-ой! Что-то пошло не так и я не смог выбрать второго ананасика! Вызвайте экзорциста! Или вы надо мной подтруниваете и решили проверить вызову ли я Вас дважды если Вы один в канале?! Хитро (нет)')
            else:
                randomUser1 = random.choice(ulist1)
                await ctx.send(f'{randomUser.mention} и...')
                await sleep(1)
                await ctx.send(f'...{randomUser1.mention}! Нет лучше пары в Ордорейде!')

    @commands.command()
    async def countdown(self, ctx):
        countdown = ['Пять!', 'Четыре!', 'Три!', 'Два!', 'Один!']
        for num in countdown:
            await ctx.send('**{0}**'.format(num))
            await asyncio.sleep(1)
        await ctx.send('**За Орду! За Ананасиков! За Выдроликого!**')

    @commands.command()
    async def userinfo(self, ctx, *, name=''):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                user = ctx.guild.get_member(str(name))
            if not user:
                user = self.bot.get_user(str(name))
            if not user:
                await ctx.send('Не могу найти такого Ананасика! Команда чувствительна к регистру.')
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

    @staticmethod
    def _getRoles(roles):
        string = ''
        for role in roles:
            if not role.is_default():
                string += f'{role.mention}, '
        if string is '':
            return 'None'
        else:
            return string[:-2]

    @staticmethod
    def _getEmojis(emojis):
        string = ''
        for emoji in emojis:
            string += str(emoji)
        if string is '':
            return 'None'
        else:
            return string[:1000]

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.guild)
    async def serverinfo(self, ctx):
        emojis = self._getEmojis(ctx.guild.emojis)
        roles = self._getRoles(ctx.guild.roles)
        embed = discord.Embed(title='**Это мой дом!**', colour=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд")
        embed.add_field(name='Название', value=ctx.guild.name, inline=True)
        embed.add_field(name='ID', value=ctx.guild.id, inline=True)
        embed.add_field(name='Создатель', value=ctx.guild.owner.mention, inline=True)
        embed.add_field(name='Регион', value=ctx.guild.region, inline=True)
        embed.add_field(name='Количество Ананасиков', value=ctx.guild.member_count, inline=True)
        embed.add_field(name='Дата создания', value=ctx.guild.created_at.strftime('%d.%m.%Y'), inline=True)
        embed.add_field(name='AFK таймаут', value=f'{int(ctx.guild.afk_timeout / 60)} min', inline=True)
        embed.add_field(name='AFK канал', value=ctx.guild.afk_channel, inline=True)
        embed.add_field(name='Фильтр контента', value=ctx.guild.explicit_content_filter, inline=True)
        embed.add_field(name='Уровень верификации', value=ctx.guild.verification_level, inline=True)
        embed.add_field(name='Роли', value=roles, inline=True)
        embed.add_field(name='Емодзи', value=emojis, inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(bmain(bot))
