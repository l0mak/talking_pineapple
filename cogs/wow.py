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

from loadconfig import __wowID__, __wowSecret__, __wowLocale__, __whitelist__


class wow():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ml(self, ctx):
        with open('lists/tanks.txt', 'r') as t:
            tanks = [line.strip() for line in t]
            t.close
        with open('lists/healers.txt', 'r') as h:
            healers = [line.strip() for line in h]
            h.close
        with open('lists/dodos.txt', 'r') as d:
            dodos = [line.strip() for line in d]
            d.close
        with open('lists/maybe.txt', 'r') as m:
            maybe = [line.strip() for line in m]
            m.close
        embed = discord.Embed(title="Список записавшихся в мифический рейд:", description=f'Записаться можно командой **;mladd**, чтобы выбрать роль добавьте **tank heal dd** после пробела! Отписаться можно командой **;mlrm**. ', color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="Всего:", value=f'''**{len(tanks)+len(healers)+len(dodos)+len(maybe)}** Ананасиков
                                                **{len(tanks)}** Танков
                                                **{len(healers)}** Лекарей
                                                **{len(dodos)}** Наносителей урона
                                                **{len(maybe)}** Неопределившихся''')
        embed.add_field(name="Танки", value=tanks)
        embed.add_field(name="Лекари", value=healers)
        embed.add_field(name="Бойцы", value=dodos)
        embed.add_field(name="Ананасики без роли", value=maybe)
        await ctx.send(embed=embed)

    @commands.command()
    async def mladd(self, ctx, *arg):
        name = ctx.author.mention
        with open('lists/maybe.txt', 'r+') as m:
            mlines = m.readlines()
            m.seek(0)
            for i in mlines:
                if name not in i:
                    m.write(i)
            m.truncate()
        with open('lists/tanks.txt', 'r+') as t:
            tlines = t.readlines()
            t.seek(0)
            for i in tlines:
                if name not in i:
                    t.write(i)
            t.truncate()
        with open('lists/healers.txt', 'r+') as h:
            hlines = h.readlines()
            h.seek(0)
            for i in hlines:
                if name not in i:
                    h.write(i)
            h.truncate()
        with open('lists/dodos.txt', 'r+') as d:
            dlines = d.readlines()
            d.seek(0)
            for i in dlines:
                if name not in i:
                    d.write(i)
            d.truncate()

        if ctx.invoked_subcommand is None:
            if not arg:
                t = open('lists/maybe.txt', 'a')
                t.writelines(name+'\n')
                t.close
                await ctx.send(f'Oora! Вы записались в мифический рейд без роли! Чтобы отписаться используйте команду **;mlrm**')
            elif arg[0] == 'tank':
                t = open('lists/tanks.txt', 'a')
                t.writelines(name+'\n')
                t.close
                await ctx.send(f'Oora! Вы записались в мифический рейд как танк! Чтобы отписаться используйте команду **;mlrm**')
            elif arg[0] == 'heal' or arg[0] == 'healer':
                t = open('lists/healers.txt', 'a')
                t.writelines(name+'\n')
                t.close
                await ctx.send(f'Oora! Вы записались в мифический рейд как лекарь! Чтобы отписаться используйте команду **;mlrm**')
            elif arg[0] == 'dd' or arg[0] == 'dodo':
                t = open('lists/dodos.txt', 'a')
                t.writelines(name+'\n')
                t.close
                await ctx.send(f'Oora! Вы записались в мифический рейд как наноситель урона! Чтобы отписаться используйте команду **;mlrm**')
            else:
                await ctx.send(f'Возможно что-то пошло не так и я Вас не понял. Названия ролей: **;mladd dd/dodo/heal/healer/tank**')
    
    @commands.command()
    async def mlrm(self, ctx):
        name = ctx.author.mention
        with open('lists/maybe.txt', 'r+') as m:
            mlines = m.readlines()
            m.seek(0)
            for i in mlines:
                if name not in i:
                    m.write(i)
            m.truncate()
        with open('lists/tanks.txt', 'r+') as t:
            tlines = t.readlines()
            t.seek(0)
            for i in tlines:
                if name not in i:
                    t.write(i)
            t.truncate()
        with open('lists/healers.txt', 'r+') as h:
            hlines = h.readlines()
            h.seek(0)
            for i in hlines:
                if name not in i:
                    h.write(i)
            h.truncate()
        with open('lists/dodos.txt', 'r+') as d:
            dlines = d.readlines()
            d.seek(0)
            for i in dlines:
                if name not in i:
                    d.write(i)
            d.truncate()

        await ctx.send('Вы отписались от похода в мифический рейд! Ой-ой! Записаться вновь можно командой **;mladd**, чтобы выбрать роль добавьте **tank heal dd** после пробела!')

    @commands.command()
    async def mlclear(self, ctx):
        if ctx.author.id in __whitelist__:
            m = open('lists/maybe.txt', 'w')
            m.close
            t = open('lists/tanks.txt', 'w')
            t.close
            h = open('lists/healers.txt', 'w')
            h.close
            h = open('lists/dodos.txt', 'w')
            h.close
            await ctx.send('Ой-ой! Вы очистили список мифических Ананасиков!')
        else:
            await ctx.send('Ой-ой! Вам нельзя пользоваться этой командой!')

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
        names = re.sub("[^A-Za-z0-9'` ]+", '\n', str_names )

        embed = discord.Embed(title="Сейчас в игре:", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(name="Локальные задания", value=names)
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
        embed.add_field(name="Arathi", value=fronts)
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
                    await ctx.send(embed=embed)
                else:
                    await ctx.send('Ой-ой! Что-то пошло не так! Попробуйте еще раз, пожалуйста. Ну или вызвайте экзорциста!')

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
        embed.add_field(name="**Гайды по петикам:**", value='[PetGuide](http://www.wow-petguide.com)')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(wow(bot))
