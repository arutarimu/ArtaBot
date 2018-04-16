import discord
import os
from discord.ext import commands

Client = discord.Client()
bot_prefix = "!"
bot = commands.Bot(command_prefix=bot_prefix)
BOT_TOKEN = ""

extensions = [
    "cmd.common",
    "cmd.reminder",
    "cmd.mirror"
]


@bot.event
async def on_ready():
    print("Online!")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name='with Arta'))


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


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
    bot.run(os.environ['BOT_TOKEN']))


if __name__ == '__main__':
    main()


