"""
FILE: BrewBot
VERSION: v.0.2-wip
AUTHORS: TheRuntingMuumuu, TheTechRobo
LICENSE: Proprietary
SOURCE STATUS: Closed Source
ABOUT: This is the random brewbot that TTR and TRM are making. It serves absolutely no purpose but it helps me learn about python, coding, and using APIs.
SOURCES: in the comments or in sources.txt
"""

#--Lots of module imports--
from discord.ext import commands
import sys, traceback
from discord.ext.commands import Bot
from store_data import *
import asyncio, configparser, logging, discord, random
from miscfunc import *

#--LOGGING TO SHOW ERRORS--
ErrorsOn = True #CHANGE THAT TO FALSE TO ENABLE USER FRIENDLY ERRORS
if ErrorsOn:
    logging.basicConfig(level=logging.INFO, format='%(levelname)s @ %(asctime)s: %(message)s; Lineno %(lineno)d, func %(funcName)s, file %(filename)s.', datefmt='%d/%m/%Y %H:%M:%S')

#--The prefix for the bot--
bot = commands.Bot(command_prefix=prefix)

#--Loads all the additional files using cogs--
for extension in ('fun2', 'system', 'brewcoin2', 'beedle'): #runs the amount of times of files to load
    bot.load_extension(extension) #loads
    print(f'\n{extension} has loaded')

async def status(msg=None): #function for changing the status
    print(f"\nSomeone changed the bot status to {msg}")
    if msg is not None:
        import requests
        for url in ("https://github.com/RobertJGabriel/Google-profanity-words/raw/master/list.txt", "http://www.bannedwordlist.com/lists/swearWords.txt"):
            blockedWords = requests.get(url).text.split("\n")
            for item in blockedWords:
                if item in msg:
                    raise Exception("*** BLOCKED STATUS CHANGE.")
        await bot.change_presence(activity=discord.Streaming(url="https://www.youtube.com/watch?v=ivSOrKAsPss", name=msg))
        return
    choices = ("a river","brew out of the faucet", "your webcam to 3000 people") #what is can be changed to
    await bot.change_presence(activity=discord.Streaming(url="https://www.youtube.com/watch?v=ivSOrKAsPss", name=random.choice(choices))) #changes it, link required for streaming status to work

#--When the bot loads--
@bot.event
async def on_ready():
    print("\n-----------------------------------------------\n<----Hits-Head-on-Cabinet has logged in...---->\n-----------------------------------------------") #tell console bot is logged in
    await bot.change_presence(activity=discord.Game(name="Bot has Started"))
    await asyncio.sleep(5)
    while True: #repeat forever
        await status()
        await asyncio.sleep(15)

@bot.event
async def on_command_error(ctx, error):
    """
    Does some stuff in case of cooldown error.
    """
    if hasattr(ctx.command, 'on_error'): #https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612
        return
    if isinstance(error, commands.CommandOnCooldown):
        potentialMessages = [f'This command is on cooldown, please wait {int(error.retry_after)}s.']
        await ctx.send(random.choice(potentialMessages))
        print('\nAn anonymous magcro tried to do a command that was on cooldown')
    else:
        raise(error)

#cog._get_overridden_method(cog.cog_command_error) is not None:
#return

@bot.command("status")
async def setstats(ctx, msg=None):
    print(f"{ctx.author.name + ctx.author.discriminator} requested a status change.")
    try:
        await status(msg)
        await thumbsup(ctx)
    except Exception as ename:
        print(f"{ctx.author.name + ctx.author.discriminator}'s new status ERRORED OUT!")
        await thumbsdown(ctx) #https://stackoverflow.com/a/62856886/9654083
        await ctx.send(ename)
    await asyncio.sleep(5)
    await status()

@bot.command("fff")
async def Clearchat(ctx):
    user = ctx.author
    role = discord.utils.find(lambda r: r.name == 'Mega Brew', ctx.message.guild.roles)
    print(role)
    print(user.roles)
    if role in user.roles:
        string = ""
        for i in range(0,51):#repeat 50 times
            string += "\u200b\n" #add zero width space to string
    else:
        string = "Permission denied."
    print(string)
    await ctx.send(string)

bot.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')
