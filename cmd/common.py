import discord
from discord.ext import commands


class Common:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self):
        await self.bot.say("Pong!")

    @commands.command(pass_context=True)
    async def say(self, string):
        new_string = string.message.content.split(" ")
        saying = ""
        for i in range(1, (len(new_string))):
            saying = saying + new_string[i] + " "
        await self.bot.say(string.message.author + "says : " + saying)
        await self.bot.delete_message(string.message)

    @commands.command(pass_context=True)
    async def av(self, user_name):
        mention = user_name.message.mentions
        if mention:
            string = user_name.message.mentions
            for i in range(0, len(string)):
                av_desire = string[i]
                av_url = av_desire.avatar_url
                url_embed = discord.Embed()
                url_embed.set_image(url=av_url)
                await self.bot.say(embed=url_embed)
        else:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_image(url=user_name.message.author.avatar_url)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def dm(self, string):
        args = string.message.content.split(" ")
        message = " "
        for i in range(1, len(args)):
            message += args[i] + " "
        await self.bot.send_message(string.message.author, message)


def setup(bot):
    bot.add_cog(Common(bot))
