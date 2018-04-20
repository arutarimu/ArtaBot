import discord
from util import exception_handler
from discord.ext import commands


class Mirror:
    def __init__(self, bot):
        self.bot = bot
        self.mapping = {}

    async def on_message(self, message):
        try:
            destination = self.mapping[message.channel.id]
            say = "[{}#{}] {}: {}".format(message.server.name,
                                          message.channel.name,
                                          message.author.name,
                                          message.clean_content)
            await self.bot.send_message(self.bot.get_channel(destination), say)
        except KeyError:
            pass
        except TypeError:
            pass

    @commands.command(pass_context=True)
    async def map(self, string):
        try:
            args = string.message.content.split(" ")
            source = args[1]
            destination = args[2]
            if len(args) != 3:
                await self.bot.say(embed=exception_handler.help("!map source_id destination_id"))
            elif source == destination:
                return
            source_id = self.bot.get_channel(source)
            destination_id = self.bot.get_channel(destination)
            if source_id and destination_id:
                self.mapping[source] = destination
                map_embed = discord.Embed(title="Mapping Channels",
                                          description="Mapped {}#{}  :arrow_right:  {}#{}.".format(source_id.name,
                                                                                                   source_id.server.name,
                                                                                                   destination_id.name,
                                                                                                   destination_id.server.name),
                                          colour=discord.Colour.green())
                await self.bot.say(embed=map_embed)
            else:
                await self.bot.say(embed=exception_handler.error("Invalid ID's."))
        except IndexError:
            await self.bot.say(embed=exception_handler.help("!map source_id destination_id"))

    @commands.command(pass_context=True)
    async def unmap(self, string):
        args = string.message.content.split(" ")
        source = args[1]
        if len(args) != 2:
            await self.bot.say(embed=exception_handler.help("!unmap source_id"))
        try:
            self.mapping.pop(source)
            unmap_embed = discord.Embed(title="Unmapping Channels",
                                        description="Unmapped {}.".format(source))
            await self.bot.say(embed=unmap_embed)
        except KeyError:
            await self.bot.say(embed=exception_handler.help("{} is not mapped yet.".format(source)))


def setup(bot):
    bot.add_cog(Mirror(bot))
