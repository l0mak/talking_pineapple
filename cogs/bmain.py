import discord
from discord.ext import commands
import random


class BotMain(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):    
        embed = discord.Embed(title="Привет!", description="Я Говорящий Ананасик! Сейчас я умею:", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="**;echo**",
                        value='''Вы хотите выговориться, но при этом остаться анонимным?
                                Введите команду в формате ;echo <channel_id> <text> и я скажу все за Вас.
                                ```;echo 499938558174560256 Привет, Я Господин Ананасик!```''', inline=False)
        embed.add_field(name="**;channels**", value="Получить список каналов и их ID для этого сервера", inline=False)
        embed.add_field(name="**;wt**", value="WowToken", inline=True)
        embed.add_field(name="**;wf**", value="WarFronts", inline=True)
        embed.add_field(name="**;wq**", value="WorldQuests", inline=True)
        embed.add_field(name="**;wowlinks ;uselesslinks**", value="Ссылки на никому не нужную информацию.", inline=False)
        embed.add_field(name="**;ml**", value="Mythic List. Список мифических Ананасиков.", inline=False)
        embed.add_field(name="**;mladd <role>**", value="Записаться в ряды мифических ананасиков. Роли **tank heal dd** ```;mladd tank```", inline=False)
        embed.add_field(name="**;mlrm**", value="Убрать себя из списка мифических Ананасиков.", inline=False)
        embed.add_field(name="**;mlclear**", value="Очистить список мифических Ананасиков.", inline=False)
        embed.add_field(name="**;bosslist ;bossiques ;listboss**", value="Список подземелий по которым можно получить тактику.", inline=False)
        embed.add_field(name='**;userinfo <username>**', value='Информация об Ананасике. **<username> - @mention или ник Ананасика** (чувствительно к регистру). Просто **;userinfo** выдаст информацию о Вас', inline=False) 
        embed.add_field(name='**;serverinfo**', value='Информация о дискорд сервере Ордорейда.', inline=False)
        embed.add_field(name='**;choose X Y Z**', value='Случайный выбор из введенных вариантов (не больше 10; просто потому что!) ```;choose Druid Shaman Priest```', inline=False)
        embed.add_field(name="**;random ;roll ;rand** ", value='''**;roll** Случайное чилсо от 0 до 100. 
                                                                **;roll X Y** Случайное число в конкретном диапазоне. 
                                                                **;roll coin** Монетка. 
                                                                **;roll user** Случайный Ананасик.
                                                                ''', inline=False)
        embed.add_field(name='**;voice**', value='Информация о голосовых возможностях бота.', inline=False)
        embed.add_field(name='**;music**', value='Информация о музыкальном плеере бота.', inline=False)
        embed.add_field(name='**;other**', value='Прочие команды.', inline=False)
        embed.add_field(name="**;info**", value="Вызов справки по Боту.", inline=False)
        embed.add_field(name="**;help**", value="Вызов этого сообщения.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def echo(self, ctx, channel: str, *message: str):
        if isinstance(ctx.message.channel, discord.DMChannel):
            await ctx.send('Сообщение отправлено!')
        else:
            await ctx.message.delete()

        ch = self.bot.get_channel(int(channel))

        msg = ' '.join(message)

        embed = discord.Embed(title='Анонимное сообщение:', description=f'{msg}', color=0xa500ff)
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_footer(text='Я тут ни при чем')

        await ch.send(embed=embed)

    @commands.command()
    async def channels(self, ctx):
        tch = []
        for channel in ctx.guild.text_channels:
            tch.append(channel.name + ' = ' + f'**{str(channel.id)}**')
        # await ctx.send(tch)

        vch = []
        for channel in ctx.guild.voice_channels:
            vch.append(channel.name + ' = ' + f'**{str(channel.id)}**')
        # await ctx.send(vch)

        embed = discord.Embed(title=f'Список каналов сервера **{ctx.guild.name}**', color=0xa500ff)
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_footer(text='Помогите, меня держат в заложниках!')

        embed.add_field(name='Текстовые каналы', value='\n'.join(tch))
        embed.add_field(name='Голосовые каналы', value='\n'.join(vch))

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
                user_list = []
                for user in ctx.channel.members:
                    if user.status != discord.Status.offline and user.bot == False:
                        user_list.append(user)
                random_user = random.choice(user_list)
                user = random_user.mention
                author = ctx.message.author.mention
                await ctx.send(f'{user}! RNG избрал Вас! Все вопросы к {author}, Я только посредник!')
                return

            elif len(arg) == 1:
                start = 1
                end = int(arg[0])
            elif len(arg) > 1:
                start = int(arg[0])
                end = int(arg[1])
            await ctx.send(f':thinking: Случайное число ({start} - {end}): {random.randint(start, end)}')

    @commands.command()
    async def choose(self, ctx, *choices: str):
        choose_str = " ".join(choices)
        choose_list = choose_str.split(' ')
        if len(choose_list) <= 1:
            await ctx.send('Боюсь, что тут выбор очевиден! Вы Dodique!')
        elif len(choose_list) > 10:
            await ctx.send('Слишком сложно! Попробуйте ввести 10 или меньше вариантов!')
        else:
            await ctx.send(f':thinking: RNG боги сделали выбор! {random.choice(choose_list)}')

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.user)
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
        avi = user.avatar_url_as(static_format='png')
        if isinstance(user, discord.Member):
            role = user.top_role.name
            if role == "@everyone":
                role = "Не знает свою роль..."
        embed = discord.Embed(title='**Настало время прочекать Ваши привилегии!**', colour=0xa500ff)
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
            return string[:1200]

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.guild)
    async def serverinfo(self, ctx):
        emojis = self._getEmojis(ctx.guild.emojis)
        roles = self._getRoles(ctx.guild.roles)
        embed = discord.Embed(title='**Я тут живу!!**', colour=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name='Название', value=ctx.guild.name, inline=True)
        embed.add_field(name='ID', value=ctx.guild.id, inline=True)
        embed.add_field(name='Создатель', value=ctx.guild.owner.mention, inline=True)
        embed.add_field(name='Регион', value=ctx.guild.region, inline=True)
        embed.add_field(name='Количество друзей', value=ctx.guild.member_count, inline=True)
        embed.add_field(name='Дата создания', value=ctx.guild.created_at.strftime('%d.%m.%Y'), inline=True)
        embed.add_field(name='AFK таймаут', value=f'{int(ctx.guild.afk_timeout / 60)} min', inline=True)
        embed.add_field(name='AFK канал', value=ctx.guild.afk_channel, inline=True)
        embed.add_field(name='Фильтр контента', value=ctx.guild.explicit_content_filter, inline=True)
        embed.add_field(name='Уровень верификации', value=ctx.guild.verification_level, inline=True)
        embed.add_field(name='Роли', value=roles, inline=True)
        embed.add_field(name='Емодзи', value=emojis, inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BotMain(bot))
