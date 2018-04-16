import discord
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
                error_embed = discord.Embed(title="Command Help",
                                            description="!map source_id destination_id",
                                            colour=discord.Colour.purple())
                await self.bot.say(embed=error_embed)
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
                error_embed = discord.Embed(title="Error Message",
                                            description="Invalid ID's.",
                                            colour=discord.Colour.red())
                await self.bot.say(embed=error_embed)
        except IndexError:
            error_embed = discord.Embed(title="Command Help",
                                        description="!map source_id destination_id",
                                        colour=discord.Colour.purple())
            await self.bot.say(embed=error_embed)

    @commands.command(pass_context=True)
    async def unmap(self, string):
        args = string.message.content.split(" ")
        source = args[1]
        if len(args) != 2:
            error_embed = discord.Embed(title="Command Help",
                                        description="!unmap source_id",
                                        colour=discord.Colour.purple())
            await self.bot.say(embed=error_embed)
        try:
            self.mapping.pop(source)
            unmap_embed = discord.Embed(title="Unmapping Channels",
                                        description="Unmapped {}.".format(source))
            await self.bot.say(embed=unmap_embed)
        except KeyError:
            error_embed = discord.Embed(title="Error Message",
                                        description="{} is not mapped yet.".format(source),
                                        colour=discord.Colour.red())
            await self.bot.say(embed=error_embed)


def setup(bot):
    bot.add_cog(Mirror(bot))
