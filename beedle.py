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

def setup(bot):
    bot.add_cog(beeedleCog(bot))
