from discord.ext import commands
import random, discord, asyncio, time
from miscfunc import *
from addBrewcoin import addbrewcoin
import logging

class beeedleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    def check(self, reaction, user): #https://stackoverflow.com/questions/63171531/how-do-you-check-if-a-specific-user-reacts-to-a-specific-message-discord-py
        return user == self.BeedleCtx.author and str(reaction.emoji) in ["🔨"] and reaction.message == self.beetle
    async def fail(self, context, laterTime, currentTime, times):
        await context.send(embed=SetEmbed(title="You failed.", description="The beetle has already eaten you.\nGo to jail and do not collect $200.", footer=f"Missed it by {abs((laterTime - currentTime) - times)}. :("))
        raise RuntimeError("Fatal: User is a failure.")

    @commands.command(name='beedle')
    async def beedle(self, context):
        ctx = context
        self.BeedleCtx = ctx
        await context.send("You have found the beedle game...")
        beedleAmount = random.randint(10,30)
        for i in range(0, beedleAmount):
            await asyncio.sleep(random.randint(10,20))
            times = random.randint(3,6)
            beetle = await context.send(f"Oh no, there's an annoying beetle! **Swat it in the next {times} seconds!**")
            await beetle.add_reaction("🔨")
            self.beetle = beetle
            currentTime = int(time.time())
            confirmation = False
            while not confirmation:
                try:
                    confirmation = await self.bot.wait_for("reaction_add",check=self.check, timeout=times)
                except asyncio.TimeoutError:
                    await self.fail(ctx, currentTime, int(time.time()), times)
            laterTime = int(time.time())
            if (laterTime - currentTime) <= times and confirmation:
                await ctx.send(f"You got it by {abs((laterTime - currentTime) - times)} seconds! :beetle:")
                if abs((laterTime - currentTime) - times) == 0:
                    await ctx.send("In other words, you got it by the skin of your teeth! Nice job.")
                continue
            if (laterTime - currentTime) > times:
                confirmation = False
            await self.fail(ctx)
        await context.send(embed=SetEmbed(title="YOU WIN!", description="The beetles realised that this wasn't helping them in the slightest. You Win :D", footer="Take 1 brewcoin kind stranger"))
        addbrewcoin(1, context.author.name + "#" + context.author.discriminator)

def setup(bot):
    bot.add_cog(beeedleCog(bot))
