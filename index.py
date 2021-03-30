"""
https://stackoverflow.com/questions/66820971/collections-counter-most-common-stops-working-correctly-in-3-digit-numbers/66821488#66821488 for brew top
https://stackoverflow.com/a/59555898/9654083
https://stackoverflow.com/a/65436253/9654083
https://stackoverflow.com/questions/60055037/how-make-custom-status-discord-py
This is the rewrite that is in progress for the Brew Discord bot.
It uses cogs instead of imports to fix a few bugs and to make 
it easier to maintain.
"""
from discord.ext import commands
from discord.ext.commands import Bot
from store_data import *
import asyncio, heapq, configparser, logging, discord, random
async def Stuff():
    print("Changing the status")
    choices = ["a river","brew out of the faucet"]
    await bot.change_presence(activity=discord.Streaming(url="https://www.youtube.com/watch?v=ivSOrKAsPss", name=random.choice(choices)))

bot = Bot(command_prefix=('brew ', 'Brew ')) #makes the prefix << brew >>

from miscfunc import *

async def Stuff():
    print("doing the thing")
    choices = ["a river","brew out of the faucet"]
    await bot.change_presence(activity=discord.Streaming(url="https://www.youtube.com/watch?v=ivSOrKAsPss", name=random.choice(choices)))

bot.load_extension("brewcoin2")
bot.load_extension("fun2")

#--ON LOAD--
@bot.event
async def on_ready():
    print("Logged in")
    while True:
        await Stuff()
        await asyncio.sleep(20)

#--ON COOLDOWN--
@bot.event
async def on_command_error(ctx, error):
    """
    Does some stuff in case of cooldown error.
    """
    if isinstance(error, commands.CommandOnCooldown):
        potentialMessages = [f'This command is on cooldown, please wait {int(error.retry_after)}s.', f'Searching for more coins to excavate... ({int(error.retry_after)}s)', f'The GPU overheated. Hopefully it did not die, or you may have a hard time finding a new one... {int(error.retry_after)}s.', f'You should not be greedy and mine too many brewcoins... Please try again in {int(error.retry_after)}s.', f'The drill is overheated. You cannot brewcoin yet. Please wait {int(error.retry_after)}s.', f'Bad things may happen if you do not wait {int(error.retry_after)} more seconds before mining again... :ghost:']
        await ctx.send(random.choice(potentialMessages))
        await ctx.send(bot.command())
        raise error

#--ON COMMANDS--
@bot.command(name='ping')
@commands.cooldown(1,1,commands.BucketType.user)
async def test(context):
    """
    tests if the bot exists
    """
    print(f'Console got the message')
    user = context.author
    await context.send(f'Hi {user}, you are senche raht :beer:\nAnd btw, I exist.\n\n*devs note - Yes it went through*')

@commands.cooldown(1,2,commands.BucketType.user)
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
    versionEmbed = discord.Embed(title="brewbot 0.1-wip", color=0x00abf3)
    versionEmbed.set_footer(text="brewbot is closed source because of the rat TheRuntingMuumuu. Ping him a million times to get his attention!")
    await context.send(embed = versionEmbed)


@bot.command(name='sponsor')
async def sponsor(context):
    sponsor = discord.Embed(title="Sponsors", description="This bot is sponsored by TheRuntingMuumuu from trm.ddns.net, and TheTechRobo from thetechrobo.github.io. \nWell it is not actually sponsored by them but it is made by them, and hosted by them, and paid for by them (for the power for hosting, and time for deving) and so on.")
    await context.send(embed = sponsor)

#--ACTUALLY RUN THIS--
bot.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')
