import discord


def error_handler(message):
    embed = discord.Embed(title="Error",
                          description=message,
                          colour=discord.Colour.red())
    return embed


def help_handler(message):
    embed = discord.Embed(title="Command Help",
                          description=message,
                          colour=discord.Colour.purple())
    return embed
