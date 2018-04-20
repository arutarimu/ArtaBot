import discord
import wikipedia
from discord.ext import commands


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
            help_embed = discord.Embed(title="Command Help",
                                       description="!wiki word\n"
                                             "This command only works in English at the moment!",
                                       colour=discord.Colour.purple())
            await self.bot.say(embed=help_embed)
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
                exception_embed = discord.Embed(title="Disambiguation. Try to be more specific!",
                                                description=string,
                                                colour=discord.Colour.red())
                await self.bot.say(embed=exception_embed)
            except wikipedia.PageError:
                error_embed = discord.Embed(title="Error",
                                            description="The page does not exist.",
                                            colour=discord.Colour.red())
                await self.bot.say(embed=error_embed)


def setup(bot):
    bot.add_cog(Wiki(bot))
