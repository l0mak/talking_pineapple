import discord
from discord.ext import commands
import random
import asyncio

class bmain():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def author(self, ctx):
        await ctx.send("https://imgur.com/gallery/jH1LRM0")
    
    @commands.command()
    async def help(self, ctx):    
        embed = discord.Embed(title="Привет!", description="Я Говорящий Ананасик! На самом деле пока я не умею говорить! Надеюсь скоро™ смогу. Сейчас я умею:", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png')
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png")
        embed.add_field(name="**%add X Y**", value="Сложение **X** и **Y**.", inline=False)
        embed.add_field(name="**%multiply X Y**", value="Умножение **X** и **Y**.", inline=False)
#        embed.add_field(name="**%ping**", value="Ping urself!", inline=False)
        embed.add_field(name="**%bosslist**", value="Список имен боссов по которым можно получить тактику.", inline=False)
        embed.add_field(name="**%<boss_name>**", value="Тактика на босса.", inline=False)
        embed.add_field(name="**%random**", value="Ананасиковый рандом. (**%roll 22**, **%random flip**, **%random user**)", inline=False)
        embed.add_field(name="**%countdown**", value="РЧ на пулл!", inline=False)
        embed.add_field(name="**%author**", value="Дает Вам представление о человеке, пишущем Бота.", inline=False)
        embed.add_field(name="**%info**", value="Вызов справки по Боту.", inline=False)
        embed.add_field(name="**%help**", value="Вызов этого сообщения.", inline=False)
#        embed.add_field(name="Список будущих возможностей/команд", value="Вызов бота в голосовй канал вызывающего. Переключение модуля прослушивания голосового канала. ")
        embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд [discord.gg/XJVagge]")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a+b)

    @commands.command()
    async def multiply(self, ctx, a: int, b: int):
        await ctx.send(a*b)        

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
                members = ctx.message.guild.members
                randomuser = random.choice(members)
                if ctx.channel.permissions_for(ctx.author).mention_everyone:
                    user = randomuser.mention
                else:
                    user = randomuser.display_name
                await ctx.send(f'{user}! RNG избрал Вас!')
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
        countdown = ['Пять!', 'Четыре!', 'Три!', 'Два!', 'Один!']
        for num in countdown:
            await ctx.send('**{0}**'.format(num))
            await asyncio.sleep(1)
        await ctx.send('**За Орду! За Ананасиков!**')
            
            
#    @commands.command()
#    async def serverinfo(self, ctx):
#        embed = discord.Embed(title='Информация о сервере', type='rich', color=0xa500ff)
#        embed.set_thumbnail(url=discord.server.icon_url)
#        embed.add_field(name='Имя', value=discord.server.name, inline=True)
#        embed.add_field(name='ID', value=discord.server.id, inline=True)
#        embed.add_field(name='Владелец', value=f'{discord.server.owner} ({discord.server.owner.id})', inline=True)
#        embed.add_field(name='Регион', value=discord.server.region, inline=True)
#        embed.add_field(name='Количество участников', value=discord.server.member_count, inline=True)
#        embed.add_field(name='Дата создания', value=discord.server.created_at, inline=True)
#        await ctx.send(embed=embed)

 
#ne ponial komandi mogoo vot tak  
#     if message.author.id is '@440103092009304064' or '440103092009304064':
#        await message.channel.send('Простите, но мне не разрешили с Вами разговаривать. Возможно Вы слишком токсичны...')
#        return

#@commands.errors
#async def CommandNotFound(ctx):
#    await ctx.channel.send('Простите, я не знаю такой команды. Попробуйте **%help**.')
   
def setup(bot):
    bot.add_cog(bmain(bot))
