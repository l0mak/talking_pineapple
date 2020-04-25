import discord
from discord.ext import commands
import random
try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError:
    import Image
    import ImageDraw
    import ImageFont

from io import BytesIO


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

        embed.add_field(name="**;wowtoday**", value="Информация с сайта WowHead об актуальных событиях в игре! **В данный момент в разработке**", inline=True)
        embed.add_field(name="**;wt**", value="WowToken", inline=True)
        # embed.add_field(name="**;wf**", value="WarFronts", inline=True)
        # embed.add_field(name="**;wq**", value="WorldQuests", inline=True)
        embed.add_field(name="**;wowlinks ;uselesslinks**", value="Ссылки на никому не нужную информацию.", inline=False)
        embed.add_field(name="**;wowclasses ;classsites**", value="Ссылки на никому не нужную классовую информацию.", inline=False)
        embed.add_field(name="**;bosslist ;bossiques ;listboss**", value="Список подземелий по которым можно получить тактику.", inline=False)

        embed.add_field(name="**;ml**", value="Mythic List. Список мифических Ананасиков.", inline=False)
        embed.add_field(name="**;mladd <role>**", value="Записаться в ряды мифических ананасиков. Роли **tank heal dd** ```;mladd tank```", inline=False)
        embed.add_field(name="**;mlrm**", value="Убрать себя из списка мифических Ананасиков.", inline=False)
        embed.add_field(name="**;mlclear**", value="Очистить список мифических Ананасиков.", inline=False)
        # embed.add_field(name="**;mlassemble**", value="Вызов всех записавшихся Ананасиков!", inline=False)


        embed.add_field(name='**;userinfo <username>**', value='Информация об Ананасике. **<username> - @mention или ник Ананасика** (чувствительно к регистру). Просто **;userinfo** выдаст информацию о Вас', inline=False)
        embed.add_field(name='**;serverinfo**', value='Информация о дискорд сервере.', inline=False)

        embed.add_field(name='**;choose X, Y, Z**', value='Случайный выбор из введенных через запятую вариантов (не больше 10; просто потому что!) ```;choose Druid, Shaman, Priest```', inline=False)
        embed.add_field(name="**;random ;roll ;rand** ", value='''**;roll** Случайное чилсо от 0 до 100. 
                                                                **;roll X Y** Случайное число в конкретном диапазоне. 
                                                                **;roll coin** Монетка. 
                                                                **;roll user** Случайный Ананасик.
                                                                ''', inline=False)

        embed.add_field(name="**;roles**", value="Просмотреть список доступных ролей.", inline=False)
        embed.add_field(name="**;role <number>**", value="Назначить себе роль с ID из списка выше.", inline=False)
        embed.add_field(name="**;addrole <color>**", value="Создать роль с цветом. Цвет можно выбрать в гугле по запросу **color picker**. ```;addrole #6fd1a5```", inline=False)


        embed.add_field(name='**;voice**', value='Информация о голосовых возможностях бота.', inline=False)
        embed.add_field(name='**;other**', value='Прочие команды.', inline=False)
        embed.add_field(name="**;info**", value="Вызов справки по Боту.", inline=False)
        embed.add_field(name="**;help**", value="Вызов этого сообщения.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def roles(self, ctx):
        embed = discord.Embed(title="Роли!", description=f"Информация по выбору ролей на {ctx.guild.name}", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="Роли по цвету класса **;role <class_name>**:", value='''Death Knight
                                                                                    Demon Hunter	
                                                                                    Druid	
                                                                                    Hunter	
                                                                                    Mage	
                                                                                    Monk	
                                                                                    Paladin	
                                                                                    Priest
                                                                                    Rogue
                                                                                    Shaman
                                                                                    Warlock	
                                                                                    Warrior	
                                                                                    ''', inline=False)
        await ctx.send(embed=embed)

        await ctx.send(f'Или Вы можете выбрать из уже добавленных на сервер {ctx.guild.name} ролей командой **;role <id>**:')

        colors = []
        for role in ctx.guild.roles:
            if str(role.name).startswith('#'):
                colors.append(str(role.name))

        for i in range(len(colors)):
            img = Image.new('RGBA', (240, 32), (0, 0, 0, 0))

            font_path = 'font.otf'
            font = ImageFont.truetype(font_path, size=20)

            d = ImageDraw.Draw(img)
            d.text((10, 10), f'Color ID {i}', fill=colors[i], font=font)

            img_byte_arr = BytesIO()
            img.save(img_byte_arr, 'png')
            img_byte_arr.seek(0)

            # img_byte_arr.getvalue() was there...
            await ctx.send(file=discord.File(img_byte_arr, 'pic.png'))



    @commands.command()
    async def role(self, ctx, *arg):
        class_dict = {'DEATH KNIGHT': '#C41F3B',
                      'DEMON HUNTER': '#A330C9	',
                      'DRUID': '#FF7D0A',
                      'HUNTER': '#ABD473',
                      'MAGE': '#69CCF0',
                      'MONK': '#00FF96',
                      'PALADIN': '#F58CBA',
                      'PRIEST': '#FFFFFF',
                      'ROGUE': '#FFF569',
                      'SHAMAN': '#0070DE',
                      'WARLOCK': '#9482C9',
                      'WARRIOR': '#C79C6E', }

        if ctx.invoked_subcommand is None:
            if not arg:
                await ctx.send('Вы не указали цвет! Посмотреть все цвета на сервере можно командой **;roles**, выбрать **;role <id>** или **;role <class_name>**, добавить свой цвет командой **;addcolor <hex_color>** (<hex_color> можно выбрать в гугле, по запросу **color picker**)')

            elif str(ctx.message.clean_content).upper()[6:] in class_dict:
                await self.addrole(ctx, str(ctx.message.clean_content).upper()[6:])

            elif int(arg[0]) < 0:
                await ctx.send('Ля какой хитрый вульперенок!')

            elif int(arg[0]) >= 0:
                color_id = int(arg[0])

                colors = []
                for role in ctx.guild.roles:
                    if str(role.name).startswith('#'):
                        colors.append(str(role.name))

                user = ctx.message.author
                for role in user.roles:
                    if str(role.name) in colors:
                        if str(role.name) == colors[color_id]:
                            await ctx.send('Так она же у вас есть!')
                        else:
                            await user.remove_roles(role, reason='Delete old one!')
                            await ctx.send('Удалил старую!')


                role_name = colors[color_id].upper()
                role = discord.utils.get(ctx.guild.roles, name=role_name)

                if role:
                    await ctx.author.add_roles(role, reason='Add new one!')
                    await ctx.send('Добавил Вам новую роль!')
                else:
                    await ctx.send('Что-то пошло не так!')



            #
            #
            # elif int(arg[0]) >= 0:
            #     color_id = int(arg[0])
            #
            #     colors = []
            #     for role in ctx.guild.roles:
            #         if str(role.name).startswith('#'):
            #             colors.append(str(role.name))
            #
            #     user = ctx.message.author
            #     for role in user.roles:
            #         if str(role.name).startswith('#'):
            #             if str(role.name) == colors[color_id]:
            #                 await ctx.send('Так она же у вас есть!')
            #             else:
            #                 await user.remove_roles(role, reason='Delete old one!')
            #                 await ctx.send('Удалил старую!')
            #
            #                 role_name = colors[color_id].upper()
            #                 role = discord.utils.get(ctx.guild.roles, name=role_name)
            #
            #                 if role:
            #                     await ctx.author.add_roles(role, reason='Add new one!')
            #                     await ctx.send('Добавил Вам новую роль!')

            else:
                await ctx.send(f'Я запутался и не смог разобрать какой Вы хотите цвет! Простите!')


    @commands.command()
    async def rmroles(self, ctx):
        if await ctx.bot.is_owner(ctx.author):
            for role in ctx.guild.roles:
                if str(role.name).startswith('#'):
                    await role.delete()
            await ctx.send('yep')
        else:
            await ctx.send('nope')

    @commands.command()
    async def purgeroles(self, ctx):
        if await ctx.bot.is_owner(ctx.author):
            i = 0
            for role in ctx.guild.roles:
                if str(role.name).startswith('#') and len(role.members) == 0:
                    await role.delete()
                    i+=1

            await ctx.send(f'yep {i} times')
        else:
            await ctx.send('nope')

    @commands.command()
    async def addrole(self, ctx, *arg):
        class_dict = {'DEATH KNIGHT' : '#C41F3B',
                    'DEMON HUNTER' : '#A330C9	',
                    'DRUID' : '#FF7D0A',
                    'HUNTER' : '#ABD473',
                    'MAGE' : '#69CCF0',
                    'MONK' : '#00FF96',
                    'PALADIN' : '#F58CBA',
                    'PRIEST' : '#FFFFFF',
                    'ROGUE' : '#FFF569',
                    'SHAMAN' : '#0070DE',
                    'WARLOCK' : '#9482C9',
                    'WARRIOR' : '#C79C6E',}

        user = ctx.message.author
        for role in user.roles:
            if str(role.name).startswith('#') or str(role.name) in class_dict:
                await user.remove_roles(role, reason='Delete old one!')
                await ctx.send('Удалил старую!')


        role_name = str(arg[0]).upper()
        role = discord.utils.get(ctx.guild.roles, name=role_name)

        if role:
            await ctx.author.add_roles(role, reason='Add new one!')
            await ctx.send('Добавил Вам новую роль!')

        else:
            if str(arg[0]).startswith('#'):
                new_role = await ctx.guild.create_role(name=role_name, color=discord.Colour(int(arg[0][1:], 16)))

            elif arg[0] in class_dict:
                new_role = await ctx.guild.create_role(name=role_name, color=discord.Colour(int(class_dict.get(role_name)[1:], 16)))

            else:
                await ctx.send(f'Ошибка {arg[0]} - {role_name} - {class_dict}')



            await ctx.author.add_roles(new_role, reason='Add new one!')
            await ctx.send('Добавил Вам новую роль!')

            bot_role = discord.utils.get(ctx.guild.roles, name='Ananasique')

            role = discord.utils.get(ctx.guild.roles, name=role_name)

            await role.edit(position=bot_role.position - 1)


    @commands.command()
    async def echo(self, ctx, channel: str, *message: str):
        if isinstance(ctx.message.channel, discord.DMChannel):
            await ctx.send('Сообщение отправлено!')
        else:
            try:
                await ctx.message.delete()
            except:
                await ctx.send('Не могу тут удалять сообщения! Удалите сами, пожалуйста, а то анонимно не получится!')

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
        choose_list = choose_str.split(',')
        if len(choose_list) <= 1:
            await ctx.send('Боюсь, что тут выбор очевиден! Вы Dodique!')
        elif len(choose_list) > 10:
            await ctx.send('Слишком сложно! Попробуйте ввести меньше вариантов!')
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
