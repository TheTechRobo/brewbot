import discord
from discord.ext import commands
import random
from miscfunc import *
from addBrewcoin import scores

class systemCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def map(self, ctx, user: discord.Member):
        """
        Command is DISABLED. Do not use.
        """
        raise Exception("CommandDisabled")
        e = await ctx.send("Mapping Commenced")
        a = scores.json()
        a.read()
        try:
            a.scores['mapping']
            await e.edit(content="Checked for Mapping Dict")
        except KeyError:
            await e.edit(content="Creating Mapping Dict")
            a.scores['mapping'] = {}
        a.scores['mapping'][user.id] = user.name + "#" + user.discriminator
        a.write()
        await e.edit(content="Mapped Successful")
    @commands.command(name='ping')
    @commands.cooldown(1,1,commands.BucketType.user)
    async def test(self, context):
        """
        tests if the bot exists
        """
        print(f'Console got the message')
        user = context.author
        await context.send(f'Hi {user}, you are senche raht :beer:\nAnd btw, I exist.\n\n\n\u200b')

    @commands.cooldown(1,2,commands.BucketType.user)
    @commands.command(name='spam')
    async def spam(self, context, END): #context is the content, end is the last thing

        """
        Takes one parameter: how many times to spam.
        """
        channel = context.channel
        if channel.name == 'brew-spamming':
            pass
        else:
            print(f"wrong channel, they in {channel.name}") #logging
            await context.send('Please only use this command in the correct channel')
            return
        if int(END) <= 16:
            for i in range(0, int(END)):
                await context.send('Brew!! :beer:')
            #To assign the Mini Brew role to people who write brew spam for the first time
            user = context.author
            role = discord.utils.find(lambda r: r.name == 'Mini Brew', context.message.guild.roles)
            if not role in user.roles:
                await user.add_roles(role)
        else:
            await context.send(f'I don\'t want to block this, but it will probably really lag the server... So please limit auto spamming brew to 15...')

    @commands.command(name='version')
    async def v(self, context):
        try:await context.send(embed=SetEmbed(title="brewbot 0.2-wip",footer="brewbot is closed source because of the rat TheRuntingMuumuu. Ping him a million times to get his attention! Or save up 1500 brewcoins and buy the perk! Whatever floats your boat!", description="0.2 is in progress! It's about two thirds done!"))
        except Exception as ename:await context.send(ename)
    @commands.command(name='sponsor')
    async def sponsor(self, context):
        await context.send(embed=SetEmbed(title="Sponsors", description="This bot is sponsored by TheRuntingMuumuu from trm.ddns.net, and TheTechRobo from thetechrobo.github.io. \nWell it is not actually sponsored by them but it is made by them, and hosted by them, and paid for by them (for the power for hosting, and time for deving) and so on."))

def setup(bot):
    bot.add_cog(systemCog(bot))
