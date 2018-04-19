import discord
from discord.ext import commands


class Wiki:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def wiki(self, ctx):
        string = ctx.message.content.split(" ")
        string.pop(0)
        message = ""
        for i in range(0, len(string)):
            message += string[0]
        embed = discord.Embed(url="https://en.wikipedia.org/wiki/{}".format(message))
        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(Wiki(bot))
