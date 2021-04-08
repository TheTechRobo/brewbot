import discord
from discord.ext import commands
import random
from miscfunc import *


class beeedleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='beedle')
    async def beedle(self, context):
        await context.send("You have found the beedle game...")
        beedleAmount = random.randint(2, 20)
        for i in range(2, beedleAmount):
            delay = random.randint(1,20)
            #wait delay
            await context.send
            timeToKick = random.randint(3,12)

def setup(bot):
    bot.add_cog(beeedleCog(bot))
