import datetime
import time
import random
import sqlite3
import asyncio
import discord
from discord.ext import commands
import botconfig

class bmain():
	#db = 'reaction.db'

	#bot.remove_command('help')

	def __init__(self, bot):
		self.bot = bot

	def _currenttime(self):
        return datetime.datetime.now(timezone('Europe/Moscow')).strftime("%H:%M:%S")

    	def userOnline(self, memberList):
        	online = []
        	for i in memberList:
            	if i.status == discord.Status.online and i.bot == False:
                	online.append(i)
        	return online

	@commands.command(aliases=['инфо', 'status'])
	async def info(self, ctx):

    	embed = discord.Embed(title="Господин Ананасик", description="Господин Ананасик - БОТ для дискорда, который в обозримом будущем подружится с Yandex SpeechKit и сможет общаться со своими друзьями!", color=0xa500ff)

	    embed.add_field(name="Версия", value="__version__")
    	embed.add_field(name="Автор", value="Тайное общество Ананасиков с сервера [Ордорейд] <https://discord.gg/XJVagge>")
    	embed.add_field(name="Колличество Серверов", value=f"{len(bot.guilds)}")
    	embed.add_field(name="Ссылка для добавления", value="До окончания тестирования ссылка недоступна. Хотя, скорее всего, ее не будет и после. :hugging: ")
    	embed.add_field(name="Вызов справки по командам", value="__prefix__help")

    		await ctx.send(embed=embed)

	@commands.command()
	async def help(self, ctx):

    	embed = discord.Embed(title="Господин Ананасик", description="Я Говорящий Ананасик! На самом деле пока я не умею говорить! Надеюсь скоро™ смогу. Сейчас я умею:", color=0xa500ff)

	    embed.add_field(name="__prefix__add X Y", value="Сложение **X** и **Y**.", inline=False)
	    embed.add_field(name="__prefix__multiply X Y", value="Умножение **X** и **Y**.", inline=False)
	    embed.add_field(name="__prefix__ping", value="Pong!", inline=False)
	    embed.add_field(name="__prefix__bosslist", value="Список имен боссов по которым можно получить тактику.", inline=False)
	    embed.add_field(name="__prefix__tact<boss_name>", value="Тактика на босса.", inline=False)
	    embed.add_field(name="__prefix__random", value="Ананасиковый рандом. (roll, rand)", inline=False)
	    embed.add_field(name="__prefix__author", value="Дает Вам представление о человеке, пишущем Бота.", inline=False)
	    embed.add_field(name="__prefix__info", value="Вызов справки по Боту.", inline=False)
	    embed.add_field(name="__prefix__help", value="Вызов этого сообщения.", inline=False)
	    #embed.add_field(name="Список будущих возможностей/команд", value="Вызов бота в голосовй канал вызывающего. Переключение модуля прослушивания голосового канала. ")

		    await ctx.send(embed=embed)

#	@commands.command()
#	async def add(self, ctx, a: int, b: int):
#    	await ctx.send(a+b)

#	@bot.command()
#	async def multiply(self, ctx, a: int, b: int):
#	    await ctx.send(a*b)

#	@bot.command()
#	async def ping(self, ctx):
#	    await ctx.send(" Pong! ")

	@commands.command()
	async def author(self, ctx):
    	await ctx.send("https://imgur.com/gallery/jH1LRM0")

 	@commands.command(aliases=['rand', 'roll'])
	async def random(self, ctx, *arg):
        '''
        :Варианты
        -----------

        :random
        :random coin
        :random user
        '''
        if ctx.invoked_subcommand is None:
            if not arg:
                start = 1
                end = 100
            elif arg[0] == 'flip' or arg[0] == 'coin':
                coin = ['Альянс', 'Орда']
                await ctx.send(f':thinking: {random.choice(coin)}')
                return
            elif arg[0] == 'user':
                online = self.userOnline(ctx.guild.members)
                randomuser = random.choice(online)
                if ctx.channel.permissions_for(ctx.author).mention_everyone:
                    user = randomuser.mention
                else:
                    user = randomuser.display_name
                await ctx.send(f'Поздравляю Вас, {user}')
                return
            elif len(arg) == 1:
                start = 1
                end = int(arg[0])
            elif len(arg) > 1:
                start = int(arg[0])
                end = int(arg[1])
            await ctx.send(f':thinking: Случайное число ({start} - {end}): {random.randint(start, end)}')

    	@commands.command()
   	 async def countdown(self, ctx):
    	    '''РЧ НА ПУЛЛ!'''
        	countdown = ['Пять!', 'Четыре!', 'Три!', 'Два!', 'Один!']
        	for num in countdown:
            	await ctx.send('**:{0}:**'.format(num))
            	await asyncio.sleep(1)
       	 await ctx.send('Ты приемный!')


def setup(bot):
    bot.add_cog(bmain(bot))
