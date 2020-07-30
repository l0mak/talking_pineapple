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


# from selenium import webdriver

try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError:
    import Image
    import ImageDraw
    import ImageFont

from io import BytesIO

from bs4 import BeautifulSoup

from config.config import wow_api_id, wow_api_token, wow_locale, wow_region, whitelist


class WowRelated(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    #
    # @commands.command()
    # async def wq(self, ctx):
    #     wq_page = 'https://www.wowhead.com/world-quests/bfa/eu'
    #     page = requests.get(wq_page)
    #     soup = BeautifulSoup(page.text, 'html.parser')
    #
    #     emissary_div = soup.find(class_="world-quests-header")
    #     emissary_items = emissary_div.find_all('a')
    #
    #     all_names = []
    #     for emissary in emissary_items:
    #         all_names.append(emissary.contents)
    #
    #     str_names = "".join( repr(e) for e in all_names[:-7])
    #     names = re.sub("[^A-Za-z0-9'` ]+", '\n', str_names )
    #
    #     embed = discord.Embed(title="Сейчас в игре:", color=0xa500ff)
    #     embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
    #     embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
    #     embed.add_field(name="Локальные задания", value=names)
    #     await ctx.send(embed=embed)


    # @commands.command()
    # async def wf(self, ctx):
    #     fr_page = 'https://www.wowhead.com'
    #     page = requests.get(fr_page)
    #     soup = BeautifulSoup(page.text, 'html.parser')
    #
    #     fr_eu_div = soup.find(class_='tiw-region-EU')
    #     fr_div = fr_eu_div.find(class_='tiw-group-wrapper-warfront')
    #
    #     fr_headings = fr_div.find_all(class_='imitation-heading')
    #     fr_perc_spans = fr_div.find_all('span')
    #
    #     fr_states = []
    #     for s in fr_headings:
    #         fr_states.append(s.contents)
    #
    #     fr_perc = []
    #     for s in fr_perc_spans:
    #         fr_perc.append(s.contents)
    #
    #     arathi_wf = "".join("{0} - {1}".format(x,y) for x,y in zip(fr_states[0],fr_perc[0]))
    #     darkshore_wf= "".join("{0} - {1}".format(x,y) for x,y in zip(fr_states[1],fr_perc[1]))
    #
    #     embed = discord.Embed(title="Сейчас в игре:", color=0xa500ff)
    #     embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
    #     embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
    #     embed.add_field(name="Arathi", value=arathi_wf, inline=False )
    #     embed.add_field(name="Dark Shore", value=darkshore_wf, inline=False )
    #
    #     await ctx.send(embed=embed)
    #
    #
    #
    # @commands.command()
    # async def wowtoday(self, ctx):
    #     await ctx.send('Секундочку плюс минуточку...')
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     # driver.headless = True
    #     #
    #     # scheight = .1
    #     # while scheight < 9.9:
    #     #     fox.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    #     #     scheight += .01
    #     #
    #
    #     driver.get('https://www.wowhead.com')
    #
    #     element = driver.find_element_by_css_selector(".row-featured-content")
    #     location = element.location
    #     size = element.size
    #     # png = driver.get_screenshot_as_png()
    #     # driver.quit()
    #
    #     # img = Image.open(BytesIO(png))
    #     #
    #     # left = location['x']
    #     # top = location['y']
    #     # right = location['x'] + size['width']
    #     # bottom = location['y'] + size['height']
    #     #
    #     # img = img.crop((left, top, right, bottom))
    #
    #     # img_byte_arr = BytesIO()
    #     # img.save(img_byte_arr, 'png')
    #     # img_byte_arr.seek(0)
    #
    #     img_li = []  # to store image fragment
    #     offset = 0  # where to start
    #
    #     # js to get height
    #     height = driver.execute_script('return Math.max('
    #                                    'document.documentElement.clientHeight, window.innerHeight);')
    #
    #     # js to get the maximum scroll height
    #     # Ref--> https://stackoverflow.com/questions/17688595/finding-the-maximum-scroll-position-of-a-page
    #     max_window_height = driver.execute_script('return Math.max('
    #                                               'document.body.scrollHeight, '
    #                                               'document.body.offsetHeight, '
    #                                               'document.documentElement.clientHeight, '
    #                                               'document.documentElement.scrollHeight, '
    #                                               'document.documentElement.offsetHeight);')
    #
    #     # looping from top to bottom, append to img list
    #     # Ref--> https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
    #     while offset < max_window_height:
    #         # Scroll to height
    #         driver.execute_script(f'window.scrollTo(0, {offset});')
    #         img = Image.open(BytesIO((driver.get_screenshot_as_png())))
    #         img_li.append(img)
    #         offset += height
    #
    #     # Stitch image into one
    #     # Set up the full screen frame
    #     img_frame_height = sum([img_frag.size[1] for img_frag in img_li])
    #     img_frame = Image.new('RGB', (img_li[0].size[0], img_frame_height))
    #     offset = 0
    #     for img_frag in img_li:
    #         img_frame.paste(img_frag, (0, offset))
    #         offset += img_frag.size[1]
    #
    #
    #
    #     left = location['x']+160
    #     top = location['y']+1500
    #     right = left + size['width']
    #     bottom = top + size['height']
    #
    #     img_frame = img_frame.crop((left, top, right, bottom))
    #
    #
    #
    #
    #     img_byte_arr = BytesIO()
    #     img_frame.save(img_byte_arr, 'png')
    #     img_byte_arr.seek(0)
    #
    #
    #     await ctx.send('Спасибо WoWHead за это:')
    #
    #     await ctx.send(file=discord.File(img_byte_arr, 'pic.png'))

    @commands.command()
    async def wt(self, ctx):
        auth_path = 'https://eu.battle.net/oauth/token'
        auth_credentials = aiohttp.BasicAuth(login=wow_api_id, password=wow_api_token)
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
        embed.add_field(inline=False, name="**Базы данных, гайдов, новостей etc:**", value='[Wowhead](http://wowhead.com/)|[Icy-Veins](https://www.icy-veins.com/)|[NoobClub](https://noob-club.ru/)|[mmo-champion](https://mmo-champion.com/content/)|[mmoboom](http://mmoboom.ru/)|[mmohelper](http://www.mmohelper.ru/)')
        embed.add_field(inline=False, name="**Пве ладдер гильдий и персонажей:**", value='[WoWprogress](https://www.wowprogress.com/)|[RaiderIO](https://raider.io/)')
        embed.add_field(inline=False, name="**Логи и их анализаторы:**", value='[WarcraftLogs](https://www.warcraftlogs.com/)|[WoWanalyzer](https://wowanalyzer.com/)|[WipeFest](https://www.wipefest.net/)')
        embed.add_field(inline=False, name="**Симкрафт:**", value='[SimulationCraft](http://simulationcraft.org/)|[Noxxic](http://www.noxxic.com/wow/dps|rankings/)|[AskMrRobot](https://www.askmrrobot.com/)|[RaidBots](https://www.raidbots.com/simbot)')
        embed.add_field(inline=False, name="**Сравнения тринкетов, трейтов etc:**", value='[Bloodmallet](https://bloodmallet.com/index.html)|[HeroDamage](https://www.herodamage.com/)')
        embed.add_field(inline=False, name="**Аддоны, викауры, профили ElvUI etc:**", value='[Curse](https://wow.curseforge.com/addons)|[TwitchClient](https://app.twitch.tv/download)|[TukUI&ElvUI](https://www.tukui.org/)|[WagoIO](https://wago.io)|[WoWinterface](http://wowinterface.com/addons.php)')
        embed.add_field(inline=False, name="**Гайды по петикам:**", value='[PetGuide](http://www.wow-petguide.com)')
        await ctx.send(embed=embed)

    @commands.command(aliases=['classsites'])
    async def wowclasses(self, ctx):
        embed = discord.Embed(title="**Классовые сообщества**", description="Различные классовые сайты/форумы/дискорды/баттлнет группы.", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.add_field(inline=False, name="**Охотник:**", value='[Discord](https://discordapp.com/invite/gjvNbyj)|[Petopia](http://wow-petopia.com/)|[Eyes Of The Beast](http://eyesofthebeast.com/)')
        embed.add_field(inline=False, name="**Воин:**", value='[Discord](https://discord.gg/xmcWP5b)|[Fury Warrior](https://www.furywarrior.com/)')
        embed.add_field(inline=False, name="**Паладин:**", value='[Discord](https://discord.gg/GaCDfUY)|[The Silver Hand](https://www.thesilverhand.net/)|[Sacred Shielding](https://sacredshielding.wordpress.com/)|[MainTankadin](http://maintankadin.failsafedesign.com/forum/)')
        embed.add_field(inline=False, name="**Разбойник:**", value='[Discord](https://discord.gg/4G5bKKD)|[Battle.net](https://blizzard.com/invite/MEkKnOsznZ)|[Raven Hold](http://www.ravenholdt.net/)| [Shadow Craft](http://shadowcraft.mmo-mumble.com/)')
        embed.add_field(inline=False, name="**Жрец:**", value='[Discord](https://discord.gg/jc68yjX)|[Warcraft Priests](https://warcraftpriests.com/)|[Mechanical Priset](https://mechanicalpriest.com/)|[Focused Will](http://focusedwill.com/)|[Automatic Jak](https://www.automaticjak.com/)')
        embed.add_field(inline=False, name="**Шаман:**", value='[Discrod](https://discordapp.com/invite/zTQhBn8)|[Battle.net](https://blizzard.com/invite/44WxmZcEVG)|[Storm Earth and Lava](http://stormearthandlava.com/)|[Chain Heal](https://chainheal.com/)')
        embed.add_field(inline=False, name="**Маг:**", value='[Altered Time](https://www.altered-time.com/)')
        embed.add_field(inline=False, name="**Чернокнижник:**", value='[Lock One Stop Shop](https://lockonestopshop.com/)')
        embed.add_field(inline=False, name="**Монах:**", value='[Peak of Serenity](https://peakofserenity.com/)|[Misty Tea House](http://www.mistyteahouse.com/)')
        embed.add_field(inline=False, name="**Друид:**", value='[Discord](https://discord.gg/ykHSMF8)')
        embed.add_field(inline=False, name="**Охотник На Демонов:**", value='[Discord](https://discord.gg/bc73aVW)|[Battle.net](https://blizzard.com/invite/7GWEWiaVN)')
        embed.add_field(inline=False, name="**Рыцарь Смерти:**", value='[Discord](https://discordapp.com/invite/EsY2jHe)|[Battle.net](https://blizzard.com/invite/O29pAnIONE)')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(WowRelated(bot))
