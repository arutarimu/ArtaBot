import discord
from discord.ext import commands


def get_votes(message_id):
    message = discord.Message(id=message_id)
    count = 0
    for reaction in message.reactions:
        count += reaction.count
        print(count)
    return count


class Vote:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def set_vote(self, message_id, req_votes):
        vote_count = get_votes(message_id)
        if vote_count == req_votes:
            await self.bot.say("Vote count has been reached.")


def setup(bot):
    bot.add_cog(Vote(bot))
