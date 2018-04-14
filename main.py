import discord
from discord.ext import commands
import sys
import subprocess

Client = discord.Client()
bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix)
file_o  = open("discord_token.txt", "r")
bot_token = file_o.readline()
file_o.close()

extensions = [
    "cmd.common"
]


@bot.event
async def on_ready():
    print("Online!")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name='with Arta'))


@bot.event
async def on_resume():
    print("Resuming")


def main():
    bot.load_extension('cmd.ArtaBot')
    for ext in extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            print("Failed to load Extension : {}\n {}: {}".format(ext, type(e).__name__, e))
    bot.run(bot_token)


if __name__ == '__main__':
    main()


