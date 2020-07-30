import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Query

import discord
from discord.ext import commands

from config.config import postgres_conn_string, whitelist
from main import prefix
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


class BaseQuery(Query):
    def count_star(self):
        count_query = (self.statement.with_only_columns([func.count()])
                       .order_by(None))
        return self.session.execute(count_query).scalar()



class DataBase(commands.Cog):

    def __init__(self, bot):
      self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith(prefix):
            timestamp = datetime.datetime.now()
            some_command = CommandsTable(id=str(message.id),
                                         server=str(message.guild.id),
                                         channel=str(message.channel.id),
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

        commands = session.query(CommandsTable).filter(CommandsTable.server == str(ctx.message.guild.id))
        # all_users = session.query(CommandsTable)(func.count(CommandsTable.author))
        all_users = BaseQuery.count_star(commands)
        most_user = commands.filter()
        embed.add_field(name='Users', value=f'{all_users}', inline=False)

        await ctx.send(embed=embed)




    @commands.command()
    async def ml(self, ctx):
        guild_myth_raiders = session.query(MythicListTable).filter(MythicListTable.server == str(ctx.message.guild.id))
        await ctx.send(guild_myth_raiders)

        for raider in guild_myth_raiders:
            await ctx.send(f'<@{raider.uid}>')


        #
        # embed = discord.Embed(title="Список записавшихся в мифический рейд:",
        #                       description=f'''Записаться можно командой **;mladd**, чтобы выбрать роль добавьте **tank heal dd** после пробела!
        #                                                                                         Отписаться можно командой **;mlrm**.
        #                                                                                         Очистить список можно командой **;mlclear** если Вы Доми, конечно
        #                                                                                     ''', color=0xa500ff)
        # embed.set_author(name='Господин Ананасик', icon_url='https://i.imgur.com/A7tQuJ1.png')
        # embed.set_thumbnail(url="https://i.imgur.com/A7tQuJ1.png")
        # embed.add_field(inline=False, name="Всего:",
        #                 value=f'''**{len(tanks) + len(healers) + len(dodos) + len(maybe)}** Ананасиков
        #                                         **{str(len(tanks))}** Танков
        #                                         **{str(len(healers))}** Лекарей
        #                                         **{str(len(dodos))}** Наносителей урона
        #                                         **{str(len(maybe))}** Неопределившихся''')
        # if tanks:
        #     embed.add_field(name="Танки", value=''.join(x + ' ' for x in tanks))
        # if healers:
        #     embed.add_field(name="Лекари", value=''.join(x + ' ' for x in healers))
        # if dodos:
        #     embed.add_field(name="Бойцы", value=''.join(x + ' ' for x in dodos))
        # if maybe:
        #     embed.add_field(inline=False, name="Ананасики без роли", value=''.join(x + ' ' for x in maybe))
        #
        # await ctx.send(embed=embed)

    @commands.command()
    async def mladd(self, ctx, *arg):
        if ctx.invoked_subcommand is None:
            if not arg:
                msg = ctx.message
                timestamp = datetime.datetime.now()
                raider = MythicListTable(id=str(msg.id),
                                             server=str(msg.guild.id),
                                             uid=str(msg.author.id),
                                             role='0',
                                             timestamp=timestamp,
                                             )

                session.add(raider)
                session.commit()
                await ctx.send(
                    f'Oora! Вы записались в мифический рейд без роли! Чтобы отписаться используйте команду **;mlrm**')
            # elif arg[0] == 'tank':
            #     t = open('lists/tanks.txt', 'a')
            #     t.writelines(name + '\n')
            #     t.close
            #     await ctx.send(
            #         f'Oora! Вы записались в мифический рейд как танк! Чтобы отписаться используйте команду **;mlrm**')
            # elif arg[0] == 'heal' or arg[0] == 'healer':
            #     t = open('lists/healers.txt', 'a')
            #     t.writelines(name + '\n')
            #     t.close
            #     await ctx.send(
            #         f'Oora! Вы записались в мифический рейд как лекарь! Чтобы отписаться используйте команду **;mlrm**')
            # elif arg[0] == 'dd' or arg[0] == 'dodo':
            #     t = open('lists/dodos.txt', 'a')
            #     t.writelines(name + '\n')
            #     t.close
            #     await ctx.send(
            #         f'Oora! Вы записались в мифический рейд как наноситель урона! Чтобы отписаться используйте команду **;mlrm**')
            # else:
            #     await ctx.send(
            #         f'Возможно что-то пошло не так и я Вас не понял. Названия ролей: **;mladd dd/dodo/heal/healer/tank**')

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

        await ctx.send(
            'Вы отписались от похода в мифический рейд! Ой-ой! Записаться вновь можно командой **;mladd**, чтобы выбрать роль добавьте **tank heal dd** после пробела!')

    @commands.command()
    async def mlclear(self, ctx):
        if ctx.author.id in whitelist:

            await ctx.send('Ой-ой! Вы очистили список мифических Ананасиков!')
        else:
            await ctx.send('Ой-ой! Вам нельзя пользоваться этой командой!')




    #
    # @commands.command()
    # async def mlassemble(self, ctx):
    #     if ctx.author.id in __whitelist__:
    #         m = open('lists/maybe.txt', 'w')
    #         m.close
    #         t = open('lists/tanks.txt', 'w')
    #         t.close
    #         h = open('lists/healers.txt', 'w')
    #         h.close
    #         h = open('lists/dodos.txt', 'w')
    #         h.close
    #         await ctx.send('Ой-ой! Вы очистили список мифических Ананасиков!')
    #     else:
    #         await ctx.send('Ой-ой! Вам нельзя пользоваться этой командой!')
    #
    #






def setup(bot):
    bot.add_cog(DataBase(bot))
