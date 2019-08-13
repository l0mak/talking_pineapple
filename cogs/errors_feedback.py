from discord.ext import commands


class ErrorsFeedback(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        error = getattr(error, 'original', error)
        
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.send('Простите, но я не знаю такой команды! Попробуйте **;help**')
            return
        
        if isinstance(error, commands.UserInputError):
            await ctx.channel.send('''Простите, но Вы допустили ошибку при вводе параметров! Попробуйте ввести данные еще раз или посмотрите команду **;help**''')
            return
        
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.channel.send(f'Простите, эту команду нельзя использовать так часто! Попробуйте еще раз через примерно {int(error.retry_after)//60} минут.')
            return
        
        else:
            await ctx.channel.send(f'Ой-ой! Что-то пошло не так! Возможно это как-то Вам поможет: {error}')
            
def setup(bot):
    bot.add_cog(ErrorsFeedback(bot))