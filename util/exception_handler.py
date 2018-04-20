import discord


def error(message):
    embed = discord.Embed(title="Error",
                          description=message,
                          colour=discord.Colour.red())
    return embed


def help(message):
    embed = discord.Embed(title="Command Help",
                          description=message,
                          colour=discord.Colour.purple())
    return embed


def embed(title, message):
    embed = discord.Embed(title=title,
                          description=message,
                          colour=discord.Colour.green())
    return embed


def approve(message):
    embed = discord.Embed(description=message,
                          colour=discord.Colour.green())
    return embed
