import discord
from discord.ext import commands


class Wiki:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def wiki(self, ctx):
        embed = discord.Embed(url="https://en.wikipedia.org/wiki/{}".format(ctx))
        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(Wiki(bot))
