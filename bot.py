import discord
from discord.ext import commands
import asyncio
import logging
from logging.handlers import RotatingFileHandler
import botconfig

__version__ = '0.2'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.WARNING)
handler = RotatingFileHandler(filename='discordbot.log', maxBytes=1024*5, backupCount=2, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = '''Talking Pineapple (Господин Ананасик) is a bot for Discord Voice Chat. 
                It can recognise user's voice commands and use text-to-speech by itself.'''

bot = commands.Bot(command_prefix=botconfig.__prefix__, description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(f'Bot-Name: {bot.user.name}')
    print(f'Bot-ID: {bot.user.id}')
    print(f'Dev Mode: {bot.dev}')
    print(f'Discord Version: {discord.__version__}')
    print(f'Bot Version: {__version__}')
    print('------')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if isinstance(message.channel, discord.DMChannel):
        await message.author.send(':hugging: Простите, я пока не очень умный, как и мой автор, поэтому пока могу отвечать только в текстовых каналах!')
        return
    if bot.dev and not await bot.is_owner(message.author):
        return
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'help' in message.content.lower():
            await message.channel.send('Вы можете вызвать описание всего, что я умею командой **%help**')
        else:
            await message.add_reaction(':ananasique:')
    if 'ломак' or 'l0mak' in message.clean_content.lower():
        await message.add_reaction(':hugging:') 
    if 'флаттер' or 'флатер' or 'суигинтырно' in message.clean_content.lower():
        await message.add_reaction(':ananasique:')
    if message.author.id is '258299583698829317':
        await message.add_reaction(':ananasique:')
    await bot.process_commands(message)
    
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(" Howdy Ho! :hugging: ")

@bot.command()
async def author(ctx):
    await ctx.send("https://imgur.com/gallery/jH1LRM0")

@bot.command()
async def info(ctx):
    # name and description of the the bot
    embed = discord.Embed(title="Talking Pineapple", description="Talking Pineapple is a bot for Discord Voice Chat. It can recognise user's voice commands and use text-to-speech by itself.", color=0xa500ff)
    
    # give info about you here
    embed.add_field(name="Author", value="<l0mak>")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="[Invite link](<no link till in test mode /hug>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Talking Pineapple", description="I'm Talking Pineapple. But now i can't talk, soon maybe. Now i can:", color=0xa500ff)

    embed.add_field(name="%add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="%multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="%greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="%author", value="Gives an idea of the person who creating me.", inline=False)
    embed.add_field(name="%info", value="Gives a little info about me", inline=False)
    embed.add_field(name="%help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run(botconfig.__token__)
