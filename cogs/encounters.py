import discord
from discord.ext import commands


class Encounters(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['bossiques', 'listboss'])
	async def bosslist(self, ctx):
		embed = discord.Embed(title="Список рейдовых подземелий про которые я могу дать справочную информацию:", color=0xa500ff)
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
		embed.add_field(name="**Рейды:**", value='''Полезную информацию по рейдам Вы всегда можете найти на:
												[Wowhead](http://wowhead.com/)
												[Icy-Veins](https://www.icy-veins.com/)
												[NoobClub](https://noob-club.ru/)
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
		embed = discord.Embed(title="Боралус", color=0xa500ff)
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


def setup(bot):
	bot.add_cog(Encounters(bot))
