import discord
import asyncio

import pyttsx3

from discord.ext import commands
from discord.voice_client import VoiceClient


class VoiceConnectionError(commands.CommandError):
    """VoiceConnectionError"""


class InvalidVoiceChannel(VoiceConnectionError):
    """InvalidVoiceChannel"""


class Voice(commands.Cog):
    """Voice"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['join'])
    async def connect(self, ctx, *, channel: discord.VoiceChannel=None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise InvalidVoiceChannel('Нет голосового канала. Дайте мне ID канала или зайдите в него сами и позовите меня.')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Переезд в <{channel}> - время вышло.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Подключаюсь к <{channel}> - время вышло.')

        await ctx.send(f'Подключился к: **{channel}**')

    @commands.command(aliases=['сэй'])
    async def say(self, ctx):
        message = ctx.message
        if len(message.clean_content) <= 4:
            await ctx.send('Но тут же не о чем говорить.')
        else:
            # path = 'voice/' + str(message.id)# + '.mp3'
            engine = pyttsx3.init()
            text = message.clean_content[5:]
            tts = engine.say(text)
            engine.runAndWait()

            ctx.guild.voice_client.play(discord.FFmpegPCMAudio())

        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Voice(bot))