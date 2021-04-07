import discord
from discord.ext import commands
import random
from miscfunc import *
import asyncio


class beeedleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='beedle')
    async def wash(self, context):
        await context.send("You have found the beedle game...")
        beedleAmount = random.randint(2, 20)
        for i in range(0, beedleAmount):
            await context.send("Beedle!")
            await asyncio.sleep(random.randint(10,40))

def setup(bot):
    bot.add_cog(beeedleCog(bot))
