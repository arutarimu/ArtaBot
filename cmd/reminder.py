import discord
import asyncio
from discord.ext import commands
from util import exception_handler


class Reminder:
    def __init__(self, bot):
        self.bot = bot

    async def reminder_message(self, string):
        await self.bot.say(string)

    @commands.command(pass_context=True)
    async def remind(self, string):
        args = string.message.content.split(" ")
        message = ""
        for i in range(2, len(args)):
            message += args[i] + " "
        if len(args) < 3:
            await self.bot.say(embed=exception_handler.help_handler("!remind minutes message"))
        else:
            if int(args[1]) > 0:
                await self.bot.say("I will remind you in {} minutes to do that :ballot_box_with_check:".format(args[1]))
                await asyncio.sleep(int(args[1])*60)
                embed = discord.Embed(title="Beep Boop, this is a reminder you set earlier :timer:",
                                      description=message,
                                      colour=discord.Colour.green())
                await self.bot.send_message(string.message.author, embed=embed)
            else:
                await self.bot.say(embed=exception_handler.error_handler("Invalid Minutes"))


def setup(bot):
    bot.add_cog(Reminder(bot))
