import asyncio

import discord
from discord.ext import commands

from discord.voice_client import VoiceClient

from gtts import gTTS


from collections import deque
import os

class voice(commands.Cog):

    def __init__(self, ctx):
        self.bot = ctx.bot

        self.guild = ctx.guild

        self.message_queue = deque()
        self.max_messages_count = 10
        self.playing_message = None


    def tts_done(self):
        os.remove('voice/' + self.playing_message + '.mp3')
        self.playing_message = None

        if len(self.message_queue) > 0:
            self.next_message()


    def next_message(self):
        message = self.message_queue.pop()

        path = 'voice/' + str(message.id) + '.mp3'

        tts = gTTS(text=message.clean_content[5::], lang='ru', slow=False)
        tts.save(path)


        player = self.guild.voice_client.play(path, after=self.tts_done)
        self.playing_message = message.id
        player.start()


    def queue_tts(self, message : discord.Message):
        if len(self.message_queue) < self.max_messages_count:
            self.message_queue.appendleft(message)

            if len(self.message_queue) == 1 and not self.playing_message:
                self.next_message()
        else:
            await self.bot.send('Не получается сказать "' + message.clean_content + '". Слишком много еще не сказано.')


    @commands.command(aliases=['сэй'])
    async def say(self, ctx):
        message = ctx.message
        if len(message.clean_content) <= 4:
            await ctx.send('Но тут же не о чем говорить.')
        else:
            await self.queue_tts(message)

            await ctx.message.delete()


    @commands.command()
    async def voice(self, ctx):
        embed = discord.Embed(title="Я говорилка!", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png')
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/449543738486816769/536e8a791db747e20ace0d0a3df6e070.png")
        embed.add_field(name='**;join ;connect**', value='Вызвать бота в голосовй канал. Если после команды указать ID голосового канала, бот подключится к нему.', inline=False)
        embed.add_field(name="**;channels**", value="Получить список каналов и их ID для этого сервера", inline=False)
        embed.add_field(name="**;meow**", value="Получить лишнее доказательство уровня IQ человека, пишущего бота", inline=False)
        embed.add_field(name="**;say ;сэй <сообщение>**", value="Произнести <сообщение>", inline=False)
        embed.set_footer(text="Болтушка я, да...")
        await ctx.send(embed=embed)


    @commands.command()
    async def meow(self, ctx):
        ctx.voice_client.play(discord.FFmpegPCMAudio('voice/meow01.ogg'))


def setup(bot):
    bot.add_cog(voice(bot))