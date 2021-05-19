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
    @commands.command(name='beedle')
    async def beedle(self, context):
        ctx = context
        self.BeedleCtx = ctx
        await context.send("You have found the beedle game...")
        beedleAmount = random.randint(2, 20)
        for i in range(0, beedleAmount):
            await asyncio.sleep(random.randint(1,20))
            times = random.randint(3,12)
            beetle = await context.send(f"Oh no, there's an annoying beetle! **Swat it in the next {times} seconds!**")
            await beetle.add_reaction("🔨")
            self.beetle = beetle
            currentTime = int(time.time())
            confirmation = False
            while not confirmation:
                confirmation = await self.bot.wait_for("reaction_add",check=self.check)
            laterTime = int(time.time())
            if abs((laterTime - currentTime) - times) == (laterTime - currentTime) - times:
                await ctx.send(f"You got it by {(laterTime - currentTime) - times} seconds!")
                if (laterTime - currentTime) - times) == 0:
                    await ctx.send("In other words, you got it by the skin of your teeth! Nice job.")
            if (laterTime - currentTime) > times:
                await ctx.send(f"Missed it by {abs((laterTime - currentTime) - times)}. :("}
                confirmation = False
            if confirmation:
                await context.send("Nice, you got it!! :beetle:")
                continue
            await context.send(embed=SetEmbed(title=":(", description="You failed.", footer="Go to jail and do not collect $200"))
            raise RuntimeError("Fatal: User is a failure.")
        await context.send(embed=SetEmbed(title="YOU WIN!", description="The beetles realised that this wasn't helping them in the slightest. You Win :D", footer="Take 1 brewcoin kind stranger"))
        addbrewcoin(1, context.author)

def setup(bot):
    bot.add_cog(beeedleCog(bot))
