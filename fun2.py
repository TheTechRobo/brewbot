import discord
from discord.ext import commands
import random

from miscfunc import *

class funCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='windows', aliases=('trash', 'rubbish','bad','absolute garbage','garbage'))
    async def windows(self, context):
        wrathText = ["Windows is the best OS ever... --TRM", "Windows is completely bloatware, spyware, and garbage and it terrible... USE ELIVE!!! --TTR", "Linux is better than windows --TRM & TTR", ":window:"]
        await context.send(random.choice(wrathText))

    @commands.command(name='wash')
    async def wash(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=ivSOrKAsPss")

    @commands.cooldown(1,30,commands.BucketType.guild)
    @commands.command(name='mount')
    async def mount(self, context):
        """
        This one is also fun!!
        """
        try: await context.send(embed = SetEmbed("WE ARE NOT MOUNTS", url="https://en.uesp.net/wiki/Online:Senche-rahts:_Not_Just_Mounts", description="WE ARE NOT MOUNTS, We are intelligent beings who are not just mounts. See more information at the link above.)", img="https://cdna.artstation.com/p/assets/covers/images/017/378/304/large/meg-steckler-shot97thumb.jpg?1555712613", footer="""Riders don't "Own" us, they are our "Partners"."""))
        except Exception as ename: await context.send(ename)

    @commands.command(name='wraith', aliases=('wrath',))
    async def wraith(self, context):
        """
        As is this one
        """
        wrathRand = random.randint(0, 2)
        wrathText = ["This is a wraith from ESO.", "This is a scary wraith", "This is wraith from Apex Legends"]
        wrathImage = ["https://th.bing.com/th/id/Rc930387dd1629d1285808a19da20c327?rik=9lR%2fB6vEbuFq3A&riu=http%3a%2f%2fvignette2.wikia.nocookie.net%2felderscrolls%2fimages%2f7%2f7c%2fWraith.png%2frevision%2flatest%3fcb%3d20160207025617&ehk=a0crJjrw3xwAap1mOQIXVJC73tfBiqhw%2fXEqvr2vJho%3d&risl=&pid=ImgRaw", "https://vignette.wikia.nocookie.net/romanticallyapocalyptic/images/7/7c/Wraith.png/revision/latest/scale-to-width-down/370?cb=20120724162754", "https://d1fs8ljxwyzba6.cloudfront.net/assets/article/2019/02/21/wraith-guide-header-apex-legends_feature.jpg"]
        await context.send(embed = SetEmbed(title="Wraith", description=wrathText[wrathRand], img=wrathImage[wrathRand]))

    @commands.command(name="tux", alias="penguin")
    async def tux(self, context):
        """
        Fun and random
        """
        penguin = ["https://th.bing.com/th/id/R7e4c84e00512f9c7fb0fd957a51c124e?rik=fxMWjFQbKozUcA&riu=http%3a%2f%2falanzeichick.com%2fwp-content%2fuploads%2fLinux-Penguin.png&ehk=fk6wjB%2bmV%2bkEVDkXRm4tGOcQKRm0RhUjEX1RwqeeQu8%3d&risl=&pid=ImgRaw", "https://youtu.be/PwnAH42gsm8"]
        await context.send(random.choice(penguin))

    @commands.cooldown(1,30,commands.BucketType.guild) #Funny senche raht thing
    @commands.command(name='senche')
    async def senche(self, context):
        """
        Try this command out!! It is fun!!
        """
        await context.send(embed=SetEmbed(title="Senche Raht", url="https://en.uesp.net/wiki/Online:Senche-raht", description=f"This is a senche raht. Not a mount. (if you are curious, enter {prefix}mount)", footer="Senche raht", img="https://th.bing.com/th/id/OIP.E_zqHOXGiW7RjFR8rLndhAHaJb?pid=ImgDet&rs=1"))
def setup(bot):
    bot.add_cog(funCog(bot))
