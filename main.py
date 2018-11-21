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
from loadconfig import __blacklist__, __whitelist__

__version__ = '1.2.1'

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
#    while not discord.opus.is_loaded():
#        discord.opus.load_opus(find_library("libopus"))
    bot.startTime = datetime.datetime.now()
    bot.startDate = time.ctime()
    bot.botVersion = __version__
    bot.userAgentHeaders = {'User-Agent': f'ubuntu:talking-pineapple:v{__version__}'}
    bot.gamesLoop = asyncio.ensure_future(_randomGame())
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author.id in __blacklist__:
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
#    if 'молод' in message.content.lower():
#        await message.add_reaction('🤗')
#    if 'спас' in message.content.lower():
#        await message.add_reaction('🍍')
#    if 'токс' in message.content.lower():
#        await message.add_reaction('🍆')
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
    embed.add_field(name='changelog', value='''Некоторые команды удалены за ненадобностью.
                                                Команды **;pairing и ;random user** теперь выдают только пользователей онлайн из списка на канале вызова, не выдают Ботов (xD) и **;pairing** не может выдать одного пользователя дважды (pic).
                                                Добавлен блок команд средней бесполезности и он будет пополняться. **;other**
                                                Добавлены команды средней полезности. **;wt ;wf ;wq и ;wowlinks**
                                                Модуль боссиков переделан так, чтобы вместо простыни текста выдавать ссылки на полезные ресурсы. В том числе и на грядущие рейды(Если есть, конечно, что выдавать) 
                                                ''', inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/389595828567801869/512177709397573632/unknown.png')
    embed.set_footer(text="/t Adeek,Sui,Sprotae /hug")
    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    channel = get(member.guild.channels, name='user_count')
    await channel.send('Сдается мне, у нас новый друг! Oora!') 
            
@bot.event
async def on_member_remove(member):
    channel = get(member.guild.channels, name='user_count')
    await channel.send(f'Ананасик покинул нас, милорд! {member.mention} куда же Вы!') 
    
@bot.command(hidden=True)
async def qb(ctx):
    if await ctx.bot.is_owner(ctx.author):
        await ctx.send('Споки!')
        bot.logout()
        sys.exit(0)
    else:
        await ctx.send('Но Вы не мой Автор!')
    

if __name__ == '__main__':
    bot.run(loadconfig.__token__)