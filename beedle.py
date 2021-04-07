import discord
from discord.ext import commands
import random
from miscfunc import *


class beeedleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='beedle')
    async def wash(self, context):
        await context.send("You have found the beedle game...")
        beedleAmount = random.randint(2, 20)
        for i in range(2, beedleAmount):
            pass

def setup(bot):
    bot.add_cog(beeedleCog(bot))
