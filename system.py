import discord
from discord.ext import commands
import random


class systemCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    @commands.cooldown(1,1,commands.BucketType.user)
    async def test(self, context):
        """
        tests if the bot exists
        """
        print(f'Console got the message')
        user = context.author
        await context.send(f'Hi {user}, you are senche raht :beer:\nAnd btw, I exist.\n\n*devs note - Yes it went through*')

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
        if int(END) <= 15:
            for i in range(0, int(END)):
                await context.send('Brew!! :beer:')
                del i
        else:
            await context.send(f'I don\'t want to block this, but it will probably really lag the server... So please limit auto spamming brew to 15...')


    @commands.command(name='version')
    async def v(self, context):
        versionEmbed = discord.Embed(title="brewbot 0.1-wip", color=0x00abf3)
        versionEmbed.set_footer(text="brewbot is closed source because of the rat TheRuntingMuumuu. Ping him a million times to get his attention!")
        await context.send(embed = versionEmbed)


    @commands.command(name='sponsor')
    async def sponsor(self, context):
        sponsor = discord.Embed(title="Sponsors", description="This bot is sponsored by TheRuntingMuumuu from trm.ddns.net, and TheTechRobo from thetechrobo.github.io. \nWell it is not actually sponsored by them but it is made by them, and hosted by them, and paid for by them (for the power for hosting, and time for deving) and so on.")
        await context.send(embed = sponsor)

def setup(bot):
    bot.add_cog(systemCog(bot))
