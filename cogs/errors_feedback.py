from discord.ext import commands


class errors_feedback:
    def __init__(self, bot):
        self.bot = bot
        
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        
        error = getattr(error, 'original', error)
        
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.send('Простите, но я не знаю такой команды! Попробуйте **;help**')
            return

        if isinstance(error, commands.UserInputError):
            await ctx.channel.send('Простите, но Вы допустили ошибку! Попробуйте ввести данные еще раз или посмотрите команду **;help**')
            return

def setup(bot):
    bot.add_cog(errors_feedback(bot))