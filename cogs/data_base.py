import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import discord
from discord.ext import commands

from config.config import postgres_conn_string

connection = postgres_conn_string

db = create_engine(connection)
base = declarative_base()


class CommandsTable(base):
    __tablename__ = 'commands'

    id = Column(String, primary_key=True)
    server = Column(String)
    channel = Column(String)
    author = Column(String)
    command = Column(String)
    timestamp = Column(DateTime)


class MythicListTable(base):
    __tablename__ = 'mythiclist'

    id = Column(String, primary_key=True)
    server = Column(String)
    uid = Column(String)
    role = Column(String)
    timestamp = Column(DateTime)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# session.add()
#
# session.query()
#
# session.delete()
#
# session.commit()


class DataBase(commands.Cog):

    def __init__(self, bot):
      self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith(';'):
            timestamp = datetime.datetime.now()
            some_command = CommandsTable(id=str(message.id),
                                         server=str(message.guild.name),
                                         channel=str(message.channel.name),
                                         author=str(message.author.id),
                                         command=f'{message.content[1:]}',
                                         timestamp=timestamp,
                                         )

            session.add(some_command)
            session.commit()



    @commands.command()
    async def stats(self,ctx):
        embed = discord.Embed(title="", color=0xa500ff)
        embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        embed.set_footer(text="")

        commands = session.query(CommandsTable)
        for command in commands:
            embed.add_field(name=f'{command.command}', value=f'server-{command.server}, channel-{command.channel}, author-<@{command.author}>, time-{command.timestamp}', inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(DataBase(bot))
