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

    async def fail(self, context, scores):
        yay = ":D" if scores > 5 else ":)"
        feet = f"But do collect {scores} brewcoin. {yay}" if scores > 0 else "You didn't get any brewcoin either. Sucks to be you ig"
        await context.send(embed=SetEmbed(title="You failed.", description="The beetle has already eaten you.\nGo to jail and do not collect $200.", footer=feet))

    @commands.command(name='beedle')
    async def beedle(self, context):
        """Type brew help beedle for more information!
        When you run this command, it waits a few seconds. Then,
        a beetle will appear! You must STOP! Hammertime in a few
        seconds. This will destroy the beetle. Sorry, animal
        rights activists."""
        ctx = context
        self.BeedleCtx = ctx
        await context.send("You have found the beedle game...")
        score, current = 0,0
        #                 v
        while True:
            await asyncio.sleep(random.randint(5,13))
            times = random.randint(3,7)
            beetle = await context.send(f"Oh no, there's an annoying beetle! **Swat it in the next {times} seconds!**")
            await beetle.add_reaction("🔨")
            self.beetle = beetle
            currentTime = round(time.time(), 1)
            sus = False # sus = False neva changes...nah that not as catchy
            try:
                red = await self.bot.wait_for("reaction_add",check=self.check, timeout=times)
                if red is sus:
                    raise UnreachableCodeError("I THINK this code is unreachable...but I guess if you're seeing this I'm wrong.")
            except asyncio.TimeoutError:
                await self.fail(ctx, score)
                addbrewcoin(score, context.author)
                return "Awwww.... I'm a failure!"
            finally:
                try:
                    del red
                    del sus
                    del beetle
                except NameError: pass
            exacterTime = round(time.time(), 1)
            laterTime = int(exacterTime)
            await ctx.send(f"You got it by {abs((int(laterTime - currentTime)) - times)} seconds! :beetle:")
            if abs((laterTime - currentTime) - times) == 0:
                await ctx.send("In other words, you got it by the skin of your teeth! Nice job.\n"
                f"(To be exact, though, you got it by {exacterTime} seconds.)")
                score += 0.5
            current += 1
            if (current % 3 == 0): score += 1
        raise UnreachableCodeError("Unreachable code in beedle function!")
        await context.send(embed=SetEmbed(title="YOU WIN!", description="The beetles realised that this wasn't helping them in the slightest. You Win :D", footer=f"Take {score} brewcoin kind stranger"))

def setup(bot):
    bot.add_cog(beeedleCog(bot))
