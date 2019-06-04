import discord
from discord.ext import commands


class encounters(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['bossiques', 'listboss'])
	async def bosslist(self, ctx):
		embed = discord.Embed(title="Список рейдовых подземелий и боссов про которые я могу дать справочную информацию:", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url='https://i.imgur.com/A7tQuJ1.png')

		embed.add_field(name="**Мифические подземелья:**", value='''**;mythicplus ;плюсы** - Общая информация по М+
																	**;ataldazar ;аталдазар** - Атал'Дазар
																	**;motherlode ;жила** - ЗОЛОТАЯ ЖИЛА!!!
																	**;sethraliss  ;tos ;сетралисс** - Храм Сетралисс
																	**;kingsrest ;гробница** - Гробница королей
																	**;toldagor ;толдагор** - Тол Дагор
																	**;boralus ;sob ;боралус** - Осада Боралуса
																	**;underrot ;подгнилье** - Подгнилье
																	**;freehold ;гавань** - Вольная гавань
																	**;waycrest ;manor ;усадьба** - Усадьба Уэйкрестов
																	**;shrine ;storm ;святилище** - Святилище штормов
																	''')
		embed.add_field(name="**Ульдир, Чертоги Управления:**", value='''**;taloc ;талок** - Талок
																		**;mother ;матриарх** - МАТРИАРХ
																		**;fetid ;пожиратель** - Зловонный пожиратель
																		**;zekvoz ;зеквоз** - Зек'воз, глашатай Н'Зота
																		**;vectis ;вектис** - Вектис
																		**;zul ;зул** - Зул
																		**;mythrax ;митракс** - Митракс Развоплотитель
																		**;ghuun ;гахун ;гуун** - Г'уун
																		''')
		embed.add_field(name="**Горнило бурь:**", value='''**;crucible ;cos  ;горнило** - Горнило бурь
																	''', inline=False)
		embed.add_field(name="**Битва за Дазар'алор:**", value='''**;dazaralor ;bod ;дазаралор** - Битва за Дазар'алор
																	''',inline=False)
		await ctx.send(embed=embed)

	@commands.command(aliases=['плюсы'])
	async def mythicplus(self, ctx):
		embed = discord.Embed(title="Общая информация по М+", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQphTFhRv7K17fWZiL6YkIPHwFVLdBgEvVQrpHtJb6xKrRcjf7Cg")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/mythic-keystones-and-dungeons-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/mythic-guides)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49227.0)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['аталдазар'])
	async def ataldazar(self, ctx):
		embed = discord.Embed(title="Атал'Дазар", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-yazma.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/ataldazar-dungeon-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=48894.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=QmZqfPkYxKU)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['жила'])
	async def motherlode(self, ctx):
		embed = discord.Embed(title="ЗОЛОТАЯ ЖИЛА!!!", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-mogulrazdunk.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/motherlode-dungeon-ability-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=48926.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=MDNwapFUH8U)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['сетралисс', 'tos'])
	async def sethraliss(self, ctx):
		embed = discord.Embed(title="Храм Сетралисс", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-avatarofsethraliss.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/temple-of-sethraliss-dungeon-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49155.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=8yFEoGPo37M)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['гробница'])
	async def kingsrest(self, ctx):
		embed = discord.Embed(title="Гробница королей", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-dazarthefirstking.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/kings-rest-dungeon-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49010.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=Wgv6BaT0zPQ)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['толдагор'])
	async def toldagor(self, ctx):
		embed = discord.Embed(title="Тол Дагор", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-overseerkorgus.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/tol-dagor-dungeon-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=48954.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=NA217FsaWCQ)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['боралус', 'sob'])
	async def boralus(self, ctx):
		embed = discord.Embed(title="Талок", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-viqgoth.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/siege-of-boralus-dungeon-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49178.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=AA4jD4gllSw)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['подгнилье'])
	async def underrot(self, ctx):
		embed = discord.Embed(title="Подгнилье", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-unboundabomination.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/underrot-dungeon-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49021.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=Eu-fVQychkU)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['усадьба', 'manor'])
	async def waycrest(self, ctx):
		embed = discord.Embed(title="Усадьба Уэйкрестов", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-goraktul.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/waycrest-manor-dungeon-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=48998.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=XvdWNmxtsAk)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['гавань'])
	async def freehold(self, ctx):
		embed = discord.Embed(title="Вольная гавань", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-harlan-sweete.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/freehold-dungeon-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=48902.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=ydXF-Fj8msw)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['святилище', 'storm'])
	async def shrine(self, ctx):
		embed = discord.Embed(title="Святилище штормов", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-volziththewhisperer.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/shrine-of-the-storm-dungeon-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49142.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=pvSFZjjAOV0)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['талок'])
	async def taloc(self, ctx):
		embed = discord.Embed(title="Талок", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-taloc.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/taloc-uldir-raid-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/taloc-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49185.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=CRR9glyQYUg)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['матриарх'])
	async def mother(self, ctx):
		embed = discord.Embed(title="МАТРИАРХ", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-mother.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/mother-uldir-raid-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/mother-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49193.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=d3Et9e8OYMI)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['пожиратель'])
	async def fetid(self, ctx):
		embed = discord.Embed(title="Зловонный пожиратель", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-fetiddevourer.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/fetid-devourer-uldir-raid-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/fetid-devourer-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49194.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=H-8LizAiKbw)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['зеквоз'])
	async def zekvoz(self, ctx):
		embed = discord.Embed(title="Зек'воз, глашатай Н'Зота", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-zekvozheraldofnzoth.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/zekvoz-herald-of-nzoth-uldir-raid-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/zek-voz-herald-of-n-zoth-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49235.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=8uPeKRXuiTQ)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['вектис'])
	async def vectis(self, ctx):
		embed = discord.Embed(title="Вектис", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-vectis.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/vectis-uldir-raid-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/vectis-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49268.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=oJK7an7qlmA)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['зул'])
	async def zul(self, ctx):
		embed = discord.Embed(title="Зул", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-zulreborn.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/zul-reborn-uldir-raid-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/zul-reborn-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49315.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=VpeAfPT51oQ)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['митракс'])
	async def mythrax(self, ctx):
		embed = discord.Embed(title="Митракс Развоплотитель", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-mythraxtheunraveler.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/mythrax-the-unraveler-uldir-raid-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/mythrax-the-unraveler-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49297.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=OKz4tnYNvs8)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['гахун','гуун'])
	async def ghuun(self, ctx):
		embed = discord.Embed(title="Г'уун", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/journal/ui-ej-boss-ghuun.png")

		embed.add_field(name='Wowhead', value='[Link](https://www.wowhead.com/guides/ghuun-uldir-raid-strategy-guide)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/g-huun-guide-for-uldir)')
		embed.add_field(name='NoobClub', value='[Link](https://www.noob-club.ru/index.php?topic=49310.0)')
		embed.add_field(name='FatbossTV', value='[Link](https://www.youtube.com/watch?v=fxMamsFlplk)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['cos', 'горнило'])
	async def crucible(self, ctx):
		embed = discord.Embed(title="Горнило бурь", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://www.paymentscardsandmobile.com/wp-content/uploads/2016/09/World-of-Warcraft.png")

		embed.add_field(name='Wowhead', value='[Link](https://ptr.wowhead.com/guides/crucible-of-storms-raid-overview)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/crucible-of-storms-raid-guides-for-battle-for-azeroth)')
		await ctx.send(embed=embed)

	@commands.command(aliases=['bod','дазаралор'])
	async def dazaralor(self, ctx):
		embed = discord.Embed(title="Битва за Дазар'алор", color=0xa500ff)
		embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
		embed.set_thumbnail(url="https://www.paymentscardsandmobile.com/wp-content/uploads/2016/09/World-of-Warcraft.png")

		embed.add_field(name='Wowhead', value='[Link](https://ptr.wowhead.com/guides/battle-of-dazaralor-raid-overview)')
		embed.add_field(name='IcyVeins', value='[Link](https://www.icy-veins.com/wow/battle-of-dazar-alor-raid-guides-for-battle-for-azeroth)')
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(encounters(bot))