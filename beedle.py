import discord
from discord.ext import commands
import random
from miscfunc import *
import asyncio


class beeedleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='beedle')
    async def beedle(self, context):
        await context.send("You have found the beedle game...")
        beedleAmount = random.randint(2, 20)
        for i in range(0, beedleAmount):
            await asyncio.sleep(random.randint(1,20))
            beetle = await context.send("Oh no, there's an annoying beetle! **Swat it in the next few seconds!**")
            await beetle.add_reaction("🔨")
            await asyncio.sleep(random.randint(3,12))
            if True: #here check if user responded
                await context.send("wip")

def setup(bot):
    bot.add_cog(beeedleCog(bot))
