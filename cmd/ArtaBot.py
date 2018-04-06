import discord
import sys
import subprocess
from discord.ext import commands


class ArtaBot:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def set_status(self, status):
        desired = status.message.content.split(" ")
        game = ""
        for i in range(1, len(desired)):
            game = game + desired[i] + " "
        await self.bot.change_presence(game=discord.Game(name=game))

    @commands.command(pass_context=True)
    async def set_nickname(self, ctx):
        try:
            desired = ctx.message.content.split(" ")
            nickname = ""
            for i in range(2, len(desired)):
                nickname = nickname + desired[i] + " "
            user = ctx.message.mentions[0]
            await self.bot.change_nickname(user, nickname)
            await self.bot.say("User {}'s nickname has been change to {} . ".format(user.name, nickname))
        except discord.Forbidden:
            await self.bot.say("You don't have the permission!")
        except IndexError:
            await self.bot.say("You must provide the nickname to set!")

    @commands.command(pass_context=True)
    async def shutdown(self):
        await self.bot.say("Good bye.")
        await self.bot.logout()

    @commands.command(pass_context=True)
    async def restart(self):
        await self.bot.say("```Restarting . . .```")
        await self.bot.logout()
        subprocess.call([sys.executable, sys.argv[0]])

    @commands.command(pass_context=True)
    async def reset_name(self, ctx):
        try:
            user = ctx.message.mentions[0]
            await self.bot.change_nickname(user, None)
            await self.bot.say("User name for {} has been reset.".format(user))
        except discord.Forbidden:
            await self.bot.say("You don't have the permission!")


def setup(bot):
    bot.add_cog(ArtaBot(bot))
