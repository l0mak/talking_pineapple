import discord
import asyncio
from discord.ext import commands

bot_token = 'NDQ5NTQzNzM4NDg2ODE2NzY5.DqEtYQ.xsdznvBYV-drBvgd3LWhHXCvO-g'
bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send("Hello, there! :hugging: ")

@bot.command()
async def author(ctx):
    await ctx.send("https://izismile.com/img/img5/20120417/640/i_have_no_idea_what_im_doing_meme_640_07.jpg")

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

bot.run(bot_token)
