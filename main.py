import asyncio
import random
import aiohttp
import io
import logging
from logging.handlers import RotatingFileHandler
import datetime
import time
import sys

import discord
from discord.ext import commands
from discord.utils import get


from config.config import bot_token, whitelist, blacklist, games, games_timer, piclist

__version__ = '1.3.2'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(filename='discordbot.log', maxBytes=1024*100, backupCount=2, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

extensions = ['cogs.bot_main',
              'cogs.wow',
              'cogs.test',
              'cogs.encounters',
              'cogs.errors_feedback',
              'cogs.other',
              'cogs.voice',
              'cogs.data_base',
              ]

description = "Talking Pineapple Project is a Bot for Discord Voice Chat."
prefix = ';'

bot = commands.Bot(command_prefix=prefix, description=description)

bot.remove_command('help')

home_channel = 499938558174560256
dm_copy_channels = 655745237926281248

dev_uid = 497897875733348353
dev_home_channel = 708713933124403261
bot.dev = False

async def _random_game():
    while True:
        guildCount = len(bot.guilds)
        memberCount = len(list(bot.get_all_members()))
        randomGame = random.choice(games)
        await bot.change_presence(activity=discord.Activity(type=randomGame[0],
                                                            name=randomGame[1].format(guilds = guildCount,
                                                                                      members = memberCount)))
        await asyncio.sleep(games_timer)


@bot.event
async def on_ready():
    if bot.user.id == dev_uid:
        bot.dev = True
        channel = bot.get_channel(dev_home_channel)
    else:
        channel = bot.get_channel(home_channel)
        logger.setLevel(logging.WARNING)

    print('-----------')
    print('Logged in as')
    print(f'Bot-Name: {bot.user.name}')
    print(f'Bot-ID: {bot.user.id}')
    print(f'Dev Mode: {bot.dev}')
    print(f'Discord Version: {discord.__version__}')
    print(f'Bot Version: {__version__}')
    print('-----------')

    for cog in extensions:
        try:
            bot.load_extension(cog)
            print(f'Loaded: {cog}')
        except Exception as some_error:
            print(f'Could not load cog: {cog} because of {some_error}.')

    bot.startTime = datetime.datetime.now()
    bot.startDate = time.strftime("%d %m %Y, %H:%M:%S")

    bot.botVersion = __version__
    bot.userAgentHeaders = {'User-Agent': f'Debian:(Talking Pineapple Discord Bot/v{bot.botVersion})'}
    bot.gamesLoop = asyncio.ensure_future(_random_game())


    await channel.send(f':white_circle: Время запуска - {bot.startDate}')

@bot.event
async def on_member_join(member):
    dedicated = get(member.guild.channels, name='user_count')
    main = get(member.guild.channels, id=member.guild.id)
    if dedicated:
        channel = dedicated
    elif main:
        channel = main
    else:
        channel = get(member.guild.channels, name='токсичный-канал')
    await channel.send(f'Сдается мне, у нас новый друг - {member.mention}! Oora!')

@bot.event
async def on_member_remove(member):
    dedicated = get(member.guild.channels, name='user_count')
    main = get(member.guild.channels, id=member.guild.id)
    if dedicated:
        channel = dedicated
    elif main:
        channel = main
    else:
        channel = get(member.guild.channels, name='токсичный-канал')
    await channel.send(f'Ананасик покинул наc! {member.mention}, куда же Вы!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author.id in blacklist:
        return
    if isinstance(message.channel, discord.DMChannel):
        channel = bot.get_channel(dm_copy_channels)
        await channel.send(f'{message.author} - {message.content}')

    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'привет' in message.content.lower():
            await message.channel.send('Здравствуйте!')
        else:
            await message.channel.send('''Простите, не понимаю Вас! Вы можете использовать команды **;info** и **;help**, чтобы больше узнать обо мне и моих возможностях! :hugging:''')

    if random.randint(0, 100) > 98:
        async with aiohttp.ClientSession() as session:
            source = random.choice(piclist)
            async with session.get(source) as resp:
                if resp.status != 200:
                    await message.channel.send('Ой-ой! Потерял боевую картиночку...')
                else:
                    data = io.BytesIO(await resp.read())
                    await message.channel.send(file=discord.File(data, 'pic.png'))
        await bot.process_commands(message)

    else:
        await bot.process_commands(message)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title='Да-да, я 🍍', description='''
                                                            С ботом можно взаимодействовать в личных сообщениях.
                                                            Туда же можно направить любые комментарии и предложения.
                                                            Предложения по функцианалу приветствуются!
                                                            ''', color=0xa500ff)
    embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
    embed.set_author(name=f'{bot.user.name}', icon_url='https://i.imgur.com/A7tQuJ1.png')
    embed.add_field(name="Версия", value=f'{__version__}')
    embed.add_field(name="Префикс", value=f'**{bot.command_prefix}**')
    embed.add_field(name="Справка по командам", value="**;help ;other ;voice**")
    embed.add_field(name="Автор", value="<@!440103092009304064>")
    embed.add_field(name="Пинг", value=f'{1000*round(bot.latency, 3)}')

    embed.add_field(name="Количество Серверов", value=f'{len(bot.guilds)}')
    embed.add_field(name="Дата и время запуска", value=f'{bot.startDate}')
    embed.add_field(name="Время работы", value=f'{str((datetime.datetime.now() - bot.startTime))[:-7]}')

    embed.add_field(inline=False, name="Благодарности", value="""
                                                                [Danny](https://github.com/Rapptz) за API wrapper дискорда на Python.
                                                                [EvieePy](https://github.com/EvieePy) за базовый звуковой модуль.
    
                                                                **Капитану Пирожку** за то, что он есть!
                                                                **Пироксиду** за пак с пандочками!
                                                                **Магтяну** за пейринг!""")


    embed.set_footer(text="/hug")
    await ctx.send(embed=embed)


def _is_owner():
    async def predicate(ctx):
        if not await ctx.bot.is_owner(ctx.author):
            raise await ctx.send('Вы не являетесь моим автором!')
        return True

    return commands.check(predicate)


@_is_owner()
@bot.command(hidden=True)
async def qb(ctx):
    if bot.dev:
        channel = bot.get_channel(dev_home_channel)
    else:
        channel = bot.get_channel(home_channel)

    await channel.send(f':red_circle: Время отключения - {time.strftime("%d %m %Y, %H:%M:%S")}')
    await bot.logout()
    sys.exit(0)


if __name__ == '__main__':
    bot.run(bot_token)