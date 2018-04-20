import discord
import wikipedia
from discord.ext import commands
from util import exception_handler


def replace_char(string):
    s = list(string)
    for i in range(0, len(s)):
        if s[i] == " ":
            s[i] = "_"
    return "".join(s)


class Wiki:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def wiki(self, ctx):
        string = ctx.message.content.split(" ")
        string.pop(0)
        if len(string) == 0:
            await self.bot.say(embed=exception_handler.help_handler("!wiki word\nThis command only works in English at the moment!"))
        else:
            message = ""
            for i in range(0, len(string)):
                message += string[i] + " "
            try:
                wiki_page = wikipedia.page(title=message, auto_suggest=True, redirect=True)
                title = wiki_page.title
                url_title = replace_char(title)
                url = "https://en.wikipedia.org/wiki/"+url_title
                description = wiki_page.summary[:2000]
                embed = discord.Embed(title=title,
                                      description=description,
                                      url=url,
                                      colour=discord.Colour.blue())
                await self.bot.say(embed=embed)
            except wikipedia.DisambiguationError as e:
                string = ""
                for i in range(0, 20):
                    string += "* " + e.options[i] + '\n'
                await self.bot.say(embed=exception_handler.error_handler("Disambiguation. Try to be more specific!\n"+string))
            except wikipedia.PageError:
                await self.bot.say(embed=exception_handler.error_handler("The page does not exist."))


def setup(bot):
    bot.add_cog(Wiki(bot))
