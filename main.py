import discord
from discord.ext import commands
import asyncio
import random
import sqlite3
import logging
from logging.handlers import RotatingFileHandler
import datetime
import time
from pytz import timezone
import sys
import loadconfig

__version__ = '1.1.7'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.WARNING)
handler = RotatingFileHandler(filename='discordbot.log', maxBytes=1024*10, backupCount=2, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = "Talking Pineapple Project is a Bot for Discord Voice Chat. It can recognise user's voice commands and use text-to-speech by itself."

bot = commands.Bot(command_prefix='%', description=description)

extensions = ['cogs.bmain', 'cogs.test', 'cogs.encounters']

bot.remove_command('help')

def _currenttime():
    return datetime.datetime.now(timezone('Europe/Moscow')).strftime('%H:%M:%S')

async def _randomGame():
    while True:
        guildCount = len(bot.guilds)
        memberCount = len(list(bot.get_all_members()))
        randomGame = random.choice(loadconfig.__games__)
        await bot.change_presence(activity=discord.Activity(type=randomGame[0], name=randomGame[1].format(guilds = guildCount, members = memberCount)))
        await asyncio.sleep(loadconfig.__gamesTimer__)

def _setupDatabase(db):
    with sqlite3.connect(db) as con:
        c = con.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS `reactions` (
                        `id`    INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        `command`    TEXT NOT NULL,
                        `url`    TEXT NOT NULL UNIQUE,
                        `author`    TEXT
                    );''')
        con.commit()
        c.close()
        
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
    print('------')
    for cog in extensions:
        try:
            bot.load_extension(cog)
        except Exception:
            print(f'Couldn\'t load cog {cog}')
    bot.startTime = datetime.datetime.now()
    bot.startDate = time.ctime()
    bot.botVersion = __version__
    bot.userAgentHeaders = {'User-Agent': f'ubuntu:talking_pineapple:v{__version__}'}
    bot.gamesLoop = asyncio.ensure_future(_randomGame())
    _setupDatabase('reaction.db')
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return 
    if isinstance(message.channel, discord.DMChannel):
        await message.author.send('Простите, я пока не очень умный, как и мой автор, поэтому пока могу отвечать только в текстовых каналах! На самом деле это ограничение обусловленно тестовыми соображениями! :hugging: ')
        return
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'привет' in message.content.lower():
            await message.channel.send('Здравствуйте!')
        elif 'q' in message.content.lower():
            await message.channel.send('q')
        elif '?' in message.content.lower():
            await message.channel.send('?')
        else:
            await message.channel.send('Здравствуйте! Вы можете использовать комнады **%info** и **%help**, чтобы больше узнать обо мне и моих возможностях! :hugging:')
    await bot.process_commands(message)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title='Да-да, я!', description="БОТ для дискорда, который в обозримом будущем подружится с Yandex SpeechKit и сможет общаться со своими друзьями! Или нет...", color=0xa500ff)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png")
    embed.set_author(name=f'{bot.user.name}', icon_url='https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png')
    embed.add_field(name="Версия", value=__version__)
    embed.add_field(name="Автор", value="<@!440103092009304064>")
    embed.add_field(name="Количество Серверов", value=f'{len(bot.guilds)}')
    embed.add_field(name="Дата и время запуска", value=f'{bot.startDate}')
    embed.add_field(name="Время работы бота", value=f'{datetime.datetime.now() - bot.startTime}')
    embed.add_field(name="Ссылка для добавления", value="До окончания тестирования ссылка недоступна. Хотя, скорее всего, ее не будет и после.")
    embed.add_field(name="Незыблемая истина", value="Катер - моторная лодка!")
    embed.add_field(name="Вызов справки по командам", value="%help")
    embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд [discord.gg/XJVagge]")
    await ctx.send(embed=embed)
            
@bot.command(hidden=True)
async def qb(ctx):
    if await ctx.bot.is_owner(ctx.author):
        await ctx.send('Ладно! Выключаюсь.')
        bot.logout()
        sys.exit(0)
    else:
        await ctx.send('Но Вы не мой Автор!')
                               
if __name__ == '__main__':
    bot.run(loadconfig.__token__)