import discord
from discord.ext import commands
import asyncio
from asyncio.tasks import sleep
import aiohttp
import io
import json
import datetime
import requests
import re

from bs4 import BeautifulSoup

from loadconfig import __wowID__, __wowSecret__, __wowLocale__

class wow():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def wq(self, ctx):
        wq_page = 'https://www.wowhead.com/world-quests/bfa/eu'        
        page = requests.get(wq_page)
        soup = BeautifulSoup(page.text, 'html.parser')

        emissary_div = soup.find(class_="world-quests-header")
        emissary_items = emissary_div.find_all('a')

        all_names = []
        for emissary in emissary_items:
            all_names.append(emissary.contents)

        str_names = "".join( repr(e) for e in all_names[:-7])
        names = re.sub('[^A-Za-z0-9 ]+', '\n', str_names )

        embed = discord.Embed(title="Сейчас в игре:", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="Локальные задания", value=names)
        embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд")
        await ctx.send(embed=embed)


    @commands.command()
    async def wf(self, ctx):
        f_page = 'https://www.wowhead.com'
        page = requests.get(f_page)
        soup = BeautifulSoup(page.text, 'html.parser')

        f_eu_div = soup.find(class_='tiw-region-EU')
        f_div = f_eu_div.find(class_='tiw-blocks-warfront')
        f_items = f_div.find_all(class_='imitation-heading')
        f_perc = f_div.find(class_='tiw-blocks-status-progress')

        f_names = []
        for t in f_items:
            f_names.append(t.contents)
        for d in f_perc:
            f_names.append(d.contents)

        str_f_names = "".join( repr(e) for e in f_names)
        fronts = re.sub('[^A-Za-z0-9 %]+', '\n', str_f_names )

        embed = discord.Embed(title="Сейчас в игре:", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="Фронты", value=fronts)
        embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд")
        await ctx.send(embed=embed)


    @commands.command()
    async def wt(self, ctx):
        auth_path = 'https://eu.battle.net/oauth/token'
        auth_credentials = aiohttp.BasicAuth(login=__wowID__, password=__wowSecret__)
        async with aiohttp.ClientSession(auth=auth_credentials) as client:
            async with client.get(auth_path, params={'grant_type': 'client_credentials'}) as auth_response:
                assert auth_response.status == 200
                auth_json = await auth_response.json()
                access_token =  auth_json['access_token']
        async with aiohttp.ClientSession() as client:
            api_path = 'https://eu.api.blizzard.com/data/wow/token/?namespace=dynamic-eu&access_token=%s' % (access_token)
            async with client.get(api_path, headers={'Authorization': 'Bearer %s' % (access_token)}) as api_response:
                if api_response.status == 200:
                    api_json = await api_response.json()
                    jtime = api_json['last_updated_timestamp'] /1000
                    timestmp = datetime.datetime.fromtimestamp(jtime).strftime('%Y-%m-%d %H:%M:%S')
                    embed = discord.Embed(title="**WoWToken**", color=0xa500ff)
                    embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
                    embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
                    embed.add_field(name="**Цена**", value=('{:,}'.format(api_json['price'] / 10000)[:-1]))
                    embed.add_field(name="**Последнее обновление API**", value=f'{timestmp}')
                    embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд")
                    await ctx.send(embed=embed)

    @commands.command(aliases=['guild'])
    async def thot(self, ctx):    
        embed = discord.Embed(title="**Two Healers One Tank**", description="Два Лекаря Один Танк - гильдия Ананасиков с различных имиджборд.", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="**Фракция**", value="Орда", inline=False)
        embed.add_field(name="**Сервер**", value="Twisting Nether", inline=False)
        embed.add_field(name="**РТ**", value="Каждую пятницу, субботу и воскресенье в вечернее время. Подробнее в #info в дискорде ", inline=False)
        embed.add_field(name="**WoWprogress**", value='[Link](https://www.wowprogress.com/guild/eu/twisting-nether/Two+Healers+One+Tank)', inline=False)
        embed.add_field(name="**Информация**", value='''Мы ходим вместе в рейды и ключики, делаем ачивки и просто весело проводим время в игре.
                                                    Рады всем ананасикам независимо от уровня игры. С нами играют и ньюфаги, и хардкорные рейдеры, и поехавшие сычи-солоплееры и казуальные битурды. Всех нас объединяет желание рейдить с анонами.
                                                    Из-за того что модератор удаляет наши посты в треде, мы перенесли всю кооперацию в дискорд:
                                                    https://discord.io/Ordoraid - обязательно заходите, мы рады всем.''', inline=False)
        embed.add_field(name="**Правила**", value='''**Быть аноном**
                                                **Не обижать других ананасиков**
                                                **Посещение рейдов полностью свободное, но в рейд нужно приходить готовыми и стараться, а не надеяться, что тебя протащат и подарят лутеш.**
                                                ***В обычную сложность необходим 335 илвл, в героическую - 350***''', inline=False)
        embed.add_field(name="**Как попасть**", value='''Чтобы попасть в рейд, зайдите в «Заранее собранные группы - Другое – Ордорейд» в назначенное время. Пароль – название борды.
                                                    В нормал, героик и ключи вы можете ходить персонажами с любого сервера.
                                                    В рейды эпохальной сложности – только персонажем с сервера Twisting Nether или ждать межсерверные мифики.
                                                    Изменения в расписании и анонсы дополнительных рейдов в #info и #lfg дискорда.''', inline=False)
        embed.add_field(name="**Battle.tag для связи**", value='''Sprotae#2918
                                                            Fluttershy#2165
                                                            ''', inline=False)
        embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд")
        await ctx.send(embed=embed)

    @commands.command(aliases=['uselesslinks'])
    async def wowlinks(self, ctx):    
        embed = discord.Embed(title="**Информация средней степени бесполезности**", description="Не расстраивайте друзей Ананасиков, читайте гайды.", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="**Базы данных, гайдов, новостей etc:**", value='[Wowhead](http://wowhead.com/)|[Icy-Veins](https://www.icy-veins.com/)|[NoobClub](https://noob-club.ru/)|[mmo-champion](https://mmo-champion.com/content/)|[mmoboom](http://mmoboom.ru/)|[mmohelper](http://www.mmohelper.ru/)')
        embed.add_field(name="**Пве ладдер гильдий и персонажей:**", value='[WoWprogress](https://www.wowprogress.com/)|[RaiderIO](https://raider.io/)')
        embed.add_field(name="**Логи и их анализаторы:**", value='[WarcraftLogs](https://www.warcraftlogs.com/)|[WoWanalyzer](https://wowanalyzer.com/)|[WipeFest](https://www.wipefest.net/)')
        embed.add_field(name="**Симкрафт:**", value='[SimulationCraft](http://simulationcraft.org/)|[Noxxic](http://www.noxxic.com/wow/dps|rankings/)|[AskMrRobot](https://www.askmrrobot.com/)|[RaidBots](https://www.raidbots.com/simbot)')
        embed.add_field(name="**Сравнения тринкетов, трейтов etc:**", value='[Bloodmallet](https://bloodmallet.com/index.html)|[HeroDamage](https://www.herodamage.com/)')
        embed.add_field(name="**Аддоны, викауры, профили ElvUI etc:**", value='[Curse](https://wow.curseforge.com/addons)|[TwitchClient](https://app.twitch.tv/download)|[TukUI&ElvUI](https://www.tukui.org/)|[WagoIO](https://wago.io)|[WoWinterface](http://wowinterface.com/addons.php)')
        embed.add_field(name="**Гайды по петикам:**", value='[PetGuide](http://www.en.wow|petguide.com)')
        embed.set_footer(text="Заранее собранные группы - Другое - Ордорейд")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(wow(bot))
