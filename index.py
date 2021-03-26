"""
https://stackoverflow.com/questions/66820971/collections-counter-most-common-stops-working-correctly-in-3-digit-numbers/66821488#66821488 for brew top
https://stackoverflow.com/a/59555898/9654083
https://stackoverflow.com/a/65436253/9654083
https://stackoverflow.com/questions/60055037/how-make-custom-status-discord-py
This is the rewrite that is in progress for the Brew Discord bot.
It uses the bot.command rather than the client.event since it's much
easier to maintain.
"""
from discord.ext import commands
from discord.ext.commands import Bot
from store_data import *
import asyncio, heapq, configparser, logging, discord, random
async def Stuff():
    print("doing the thing")
    choices = ["a river","brew out of the faucet"]
    await bot.change_presence(activity=discord.Streaming(url="https://www.youtube.com/watch?v=ivSOrKAsPss", name=random.choice(choices)))

bot = Bot(command_prefix=('brew ', 'Brew ')) #makes the prefix << brew >>

#--The other files with @bot.event need to be HERE not at the start or they wont work.--
from fun import *
from brewcoin import *

#--FUNCTIONS--
def TheColoursOfTheRainbow(): #to choose a random RGB value
    colours = []
    for i in range(0,3):
        colours.append(random.randint(0,255))
    return colours

setup(TheColoursOfTheRainbow) #allows this function to be used in other documents


#--ON LOAD--
@bot.event #writes in terminal if the bot logs in
async def on_ready():
    print("Logged in")
    while True:
        await Stuff()
        await asyncio.sleep(10)


#--ON COMMANDS--
@bot.command(name='ping', aliases=['test'])
async def test(context):
    """
    tests if the bot exists
    """
    user = context.author
    await context.send(f'Hi {user}, you are senche raht :beer:\nAnd btw, I exist.')

@commands.cooldown(1,1,commands.BucketType.user)
@bot.command(name='spam')
async def spam(context, END): #context is the content, end is the last thing
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


@bot.command(name='version')
async def v(context):
    versionEmbed = discord.Embed(title="brewbot 0.1-wip", color=0xafdfff)
    versionEmbed.set_footer(text="brewbot is closed source because of the rat TheRuntingMuumuu. Ping him a million times to get his attention!")
    await context.send(embed = versionEmbed)


@bot.command(name='sponsor')
async def sponsor(context):
    sponsor = discord.Embed(title="Sponsors", description="This bot is sponsored by TheRuntingMuumuu from trm.ddns.net, and TheTechRobo from thetechrobo.github.io. \nWell it is not actually sponsored by them but it is made by them, and hosted by them, and paid for by them (for the power for hosting, and time for deving) and so on.")
    await context.send(embed = sponsor)

#--ACTUALLY RUN THIS--
bot.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')
