import asyncio
import random
import logging
from logging.handlers import RotatingFileHandler
import datetime
import time
import sys

import discord
from discord.ext import commands
from discord.utils import get

import loadconfig

__version__ = '1.2.2'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.WARNING)
handler = RotatingFileHandler(filename='discordbot.log', maxBytes=1024*100, backupCount=2, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

extensions = ['cogs.bmain', 'cogs.wow', 'cogs.test', 'cogs.encounters', 'cogs.errors_feedback', 'cogs.voice', 'cogs.other']

description = "Talking Pineapple Project is a Bot for Discord Voice Chat. It can recognise user's voice commands and use text-to-speech by itself. Soon..."

bot = commands.Bot(command_prefix=';', description=description)

bot.remove_command('help')

async def _randomGame():
    while True:
        guildCount = len(bot.guilds)
        memberCount = len(list(bot.get_all_members()))
        randomGame = random.choice(loadconfig.__games__)
        await bot.change_presence(activity=discord.Activity(type=randomGame[0], name=randomGame[1].format(guilds = guildCount, members = memberCount)))
        await asyncio.sleep(loadconfig.__gamesTimer__)

@bot.event
async def on_ready():
    if bot.user.id == 449543738486816769:
        bot.dev = True
    else:
        bot.dev = False
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
        except Exception:
            print(f'Couldn\'t load cog {cog}')
    while not discord.opus.is_loaded():
        discord.opus.load_opus('libopus')
    bot.startTime = datetime.datetime.now()
    bot.startDate = time.ctime()
    bot.botVersion = __version__
    bot.userAgentHeaders = {'User-Agent': f'ubuntu:talking-pineapple:v{__version__}'}
    bot.gamesLoop = asyncio.ensure_future(_randomGame())
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author.id in loadconfig.__blacklist__:
        return
#    if message.author.id in huglist:
#        await message.add_reaction('🤗')
    if isinstance(message.channel, discord.DMChannel):
        await message.author.send('Простите, я пока не очень умный, поэтому могу отвечать только в текстовых каналах! На самом деле это ограничение обусловленно тестовыми соображениями! :hugging: ')
        return
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'привет' in message.content.lower():
            await message.channel.send('Здравствуйте!')
        else:
            await message.channel.send('Простите, не понимаю Вас! Вы можете использовать комнады **;info** и **;help**, чтобы больше узнать обо мне и моих возможностях! :hugging:')
#    if 'когда рейд' in message.content.lower():
#        channel = discord.utils.get(bot.get_all_channels(), guild__name='Ордорейд', name='info')
#        await message.channel.send(f'Вся информация о рейдах в канале {channel.mention} ')
    else:
        await bot.process_commands(message)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title='Да-да, я 🍍', description='''Бот для дискорда, созданный исключительно в целях самообучения человеком очень далеким от программирования.
                                                            Любые комментарии и предложения приветствуются. В особенности по функционалу.
                                                            ''', color=0xa500ff)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png")
    embed.set_author(name=f'{bot.user.name}', icon_url='https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png')
    embed.add_field(name="Версия", value=f'{__version__}')
    embed.add_field(name="Префикс", value=f'**{bot.command_prefix}**')
    embed.add_field(name="Автор", value="<@!440103092009304064>")
    embed.add_field(name="Количество Серверов", value=f'{len(bot.guilds)}')
    embed.add_field(name="Дата и время запуска", value=f'{bot.startDate}')
    embed.add_field(name="Время работы", value=f'{(datetime.datetime.now() - bot.startTime)}')
    embed.add_field(name="Пинг", value=f'{1000*round(bot.latency, 3)}')
    embed.add_field(name="Справка по командам", value="**;help**")
    embed.add_field(name='Changelog', value='''Разблокировал **;echo** для всех. Делайте с этим что хотите.
                                            Снял Mention с пейринга.
                                            Бот умеет коннектиться к войсу, молчать в нем и не только. **;voice**
                                            Сделал список мифических рейдеров как у Мистера Ордорейда. **Пользоваться им не надо! Он просто есть.**
                                            ''', inline=False) 
    embed.set_image(url='https://i.gifer.com/ZQ6E.gif') 
#    embed.set_image(url='http://s011.radikal.ru/i318/1611/88/10a8427ad95f.gif')
    embed.set_footer(text="/hug")
    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    channel = get(member.guild.channels, name='user_count')
    await channel.send(f'Сдается мне, у нас новый друг! {member.mention} Oora!') 
            
@bot.event
async def on_member_remove(member):
    channel = get(member.guild.channels, name='user_count')
    await channel.send(f'Ананасик покинул наc! {member.mention} куда же Вы!') 
    
@bot.command(hidden=True)
async def qb(ctx):
    if await ctx.bot.is_owner(ctx.author):
#    if ctx.author.id in loadconfig.__whitelist__:
        await ctx.send('Спокойной ночи!')
        bot.logout()
        sys.exit(0)
    else:
        await ctx.send('Вам нельзя укладывать меня спать!')
    

if __name__ == '__main__':
    bot.run(loadconfig.__token__)