@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def ping(ctx):
    await ctx.send(" Pong! ")

@bot.command()
async def author(ctx):
    await ctx.send("https://imgur.com/gallery/jH1LRM0")

@bot.command()
async def info(ctx):

    embed = discord.Embed(title="Господин Ананасик", description="Господин Ананасик - БОТ для дискорда, который в обозримом будущем подружится с Yandex SpeechKit и сможет общаться со своими друзьями!", color=0xa500ff)

    embed.add_field(name="Версия", value="__version__")
    embed.add_field(name="Авторы", value="Тайное общество Ананасиков с сервера [Ордорейд] <https://discord.gg/XJVagge>")
    embed.add_field(name="Колличество Серверов", value=f"{len(bot.guilds)}")
    embed.add_field(name="Ссылка для добавления", value="До окончания тестирования ссылка недоступна. Хотя, скорее всего, ее не будет и после. :hugging: ")
    embed.add_field(name="Вызов справки по командам", value="__prefix__help")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Господин Ананасик", description="Я Говорящий Ананасик! На самом деле пока я не умею говорить! Надеюсь скоро™ смогу. Сейчас я умею:", color=0xa500ff)

    embed.add_field(name="__prefix__add X Y", value="Сложение **X** и **Y**.", inline=False)
    embed.add_field(name="__prefix__multiply X Y", value="Умножение **X** и **Y**.", inline=False)
    embed.add_field(name="__prefix__ping", value="Pong!", inline=False)
    embed.add_field(name="__prefix__bosslist", value="Список имен боссов по которым можно получить тактику.", inline=False)
    embed.add_field(name="__prefix__tact<boss_name>", value="Тактика на босса.", inline=False)
    embed.add_field(name="__prefix__roll", value="Ананасиковый рандом.", inline=False)
    embed.add_field(name="__prefix__author", value="Дает Вам представление о человеке, пишущем Бота.", inline=False)
    embed.add_field(name="__prefix__info", value="Вызов справки по Боту.", inline=False)
    embed.add_field(name="__prefix__help", value="Вызов этого сообщения.", inline=False)
    #embed.add_field(name="Список будущих возможностей/команд", value="Вызов бота в голосовй канал вызывающего. Переключение модуля прослушивания голосового канала. ")

    await ctx.send(embed=embed)
