import discord
from discord.ext import commands
import asyncio
import time
import datetime
import random
import sqlite3
#import traceback
#import os
#import sys
#import hashlib
#import aiohttp
import logging
from logging.handlers import RotatingFileHandler
#from collections import Counter
#from pytz import timezone
import botconfig

__version__ = '0.2'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.WARNING)
handler = RotatingFileHandler(filename='discordbot.log', maxBytes=1024*5, backupCount=2, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = '''Talking Pineapple Project is a bot for Discord Voice Chat. 
                It can recognise user's voice commands and use text-to-speech by itself.'''

bot = commands.Bot(command_prefix=botconfig.__prefix__, description=description)

def _setupDatabase(db):
    with sqlite3.connect(db) as con:
        c = con.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS `reactions` (
                        `id`    INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        `command`   TEXT NOT NULL,
                        `url`   TEXT NOT NULL UNIQUE,
                        `author`    TEXT
                    );''')
        con.commit()
        c.close()

def _currenttime():
    return datetime.datetime.now(timezone('Europe/Moscow')).strftime('%H:%M:%S')

async def _randomGame():
    while True:
        guildCount = len(bot.guilds)
        memberCount = len(list(bot.get_all_members()))
        randomGame = random.choice(botconfig.__games__)
        await bot.change_presence(activity=discord.Activity(type=randomGame[0], name=randomGame[1].format(guilds = guildCount, members = memberCount)))
        await asyncio.sleep(botconfig.__gamesTimer__)

@bot.event
async def on_ready():
    if bot.user.id == 85098986842619904:
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
    for cog in botconfig.__cogs__:
        try:
            bot.load_extension(cog)
        except Exception:
            print(f'Couldn\'t load cog {cog}')
    bot.commands_used = Counter()
    bot.startTime = time.time()
    bot.botVersion = __version__
    bot.userAgentHeaders = {'User-Agent': f'ubuntu:talking_pineapple:v{__version__}'}
    bot.gamesLoop = asyncio.ensure_future(_randomGame())
    _setupDatabase('reaction.db')

@bot.event
async def on_command(ctx):
    bot.commands_used[ctx.command.name] += 1
    msg = ctx.message

@bot.event
async def on_message(message):
    if message.author.bot or message.author.id in loadconfig.__blacklist__:
        return
    if isinstance(message.channel, discord.DMChannel):
        await message.author.send(':hugging: Простите, я пока не очень умный, как и мой автор, поэтому пока могу отвечать только в текстовых каналах! На самом деле это ограничение обусловленно тестовыми соображениями!')
        return
    if bot.dev and not await bot.is_owner(message.author):
        return
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'help' or 'info' or 'test' or 'who' in message.content.lower():
            await message.channel.send('Вы можете начать общение со мной командой **__prefix__help** или **__prefix__info')
        else:
            await message.add_reaction(':ananasique:')
    if 'флаттер' or 'флатер' or 'суигинтырно' in message.clean_content.lower():
        await message.add_reaction(':ananasique:')
    if message.author.id is '258299583698829317':
        await message.add_reaction(':ananasique:')
    await bot.process_commands(message)

@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title='Oora! Новые друзья!', type='rich', color=0xa500ff)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name='Имя', value=guild.name, inline=True)
    embed.add_field(name='ID', value=guild.id, inline=True)
    embed.add_field(name='Владелец', value=f'{guild.owner} ({guild.owner.id})', inline=True)
    embed.add_field(name='Регион', value=guild.region, inline=True)
    embed.add_field(name='Количество участников', value=guild.member_count, inline=True)
    embed.add_field(name='Дата создания', value=guild.created_at, inline=True)
    await bot.owner.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
    embed = discord.Embed(title='Теряю друзей...', type='rich', color=0xa500ff)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name='Имя', value=guild.name, inline=True)
    embed.add_field(name='ID', value=guild.id, inline=True)
    embed.add_field(name='Владелец', value=f'{guild.owner} ({guild.owner.id})', inline=True)
    embed.add_field(name='Регион', value=guild.region, inline=True)
    embed.add_field(name='Количество участников', value=guild.member_count, inline=True)
    embed.add_field(name='Дата создания', value=guild.created_at, inline=True)
    await bot.owner.send(embed=embed)

@bot.event
async def on_error(event, *args, **kwargs):
    if bot.dev:
        traceback.print_exc()
    else:
        embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
        embed.add_field(name='Event', value=event)
        embed.description = '```py\n%s\n```' % traceback.format_exc()
        embed.timestamp = datetime.datetime.utcnow()
        try:
            await bot.owner.send(embed=embed)
        except:
            pass

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.author.send('Простите! Эта команда не может быть вызвана из личных сообщений!')
    elif isinstance(error, commands.DisabledCommand):
        await ctx.channel.send(':x: Простите! Эта команда пока недоступна!')
    elif isinstance(error, commands.CommandInvokeError):
        if bot.dev:
            raise error
        else:
            embed = discord.Embed(title=':x: Command Error', colour=0x992d22) #Dark Red
            embed.add_field(name='Error', value=error)
            embed.add_field(name='Guild', value=ctx.guild)
            embed.add_field(name='Channel', value=ctx.channel)
            embed.add_field(name='User', value=ctx.author)
            embed.add_field(name='Message', value=ctx.message.clean_content)
            embed.timestamp = datetime.datetime.utcnow()
            try:
                await bot.owner.send(embed=embed)
            except:
                pass
                
bot.run(botconfig.__token__)
