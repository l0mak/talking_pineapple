import discord
from discord.ext import ActivityType

__games__ = [
    (discord.ActivityType.playing, 'с Друзьями'),
    (discord.ActivityType.playing, 'c Фералами'),
    (discord.ActivityType.playing, 'попробуйте %help'),
    (discord.ActivityType.playing, 'попробуйте %info'),
    (discord.ActivityType.playing, 'в Черепаха Дошла До Воды'),
    (discord.ActivityType.playing, 'с Капитаном Пирожком'),
    (discord.ActivityType.watching, 'за Ордорейдом'),
    (discord.ActivityType.watching, 'на {members} Ананасиков'),
    (discord.ActivityType.watching, 'за {guilds} Серверами'),
    (discord.ActivityType.watching, "стрим Джин'Зиггоря"),
    (discord.ActivityType.listening, 'чарующий голос Господина Флаттера')
]
__gamesTimer__ = 2 * 60
