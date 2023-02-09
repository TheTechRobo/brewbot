"""
FILE: BrewBot
VERSION: v.0.2-wip
AUTHORS: TheRuntingMuumuu, TheTechRobo
LICENSE: Proprietary
SOURCE STATUS: Closed Source
ABOUT: This is the random brewbot that TTR and TRM are making. It serves absolutely no purpose but it helps me learn about python, coding, and using APIs.
SOURCES: in the comments or in sources.txt
"""


def _(s):
    return s  # futureproofing


PREFIX = "brew "


class No(Exception):
    pass


# --Lots of module imports--
from discord.ext import commands
import asyncio
import logging
import random
from store_data import *
import discord
from miscfunc import *

# --LOGGING TO SHOW ERRORS--
ErrorsOn = True
if ErrorsOn:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s @ %(asctime)s: %(message)s; Lineno %(lineno)d, func %(funcName)s, file %(filename)s.",
        datefmt="%d/%m/%Y %H:%M:%S",
    )

# --The prefix for the bot--
bot = commands.Bot(command_prefix=prefix)

print("\nLoading extensions...")

# --Loads all the additional files using cogs--
for extension in (
    "fun2",
    "system",
    "brewcoin2",
    "beedle",
):  # runs the amount of times of files to load
    bot.load_extension(extension)  # loads
    print(f"{extension} has loaded")
print()


async def status(msg=None):  # function for changing the status
    print(f"\nSomeone changed the bot status to {msg}")
    if msg is not None:
        import requests

        for url in (
            "https://github.com/RobertJGabriel/Google-profanity-words/raw/master/list.txt",
            "http://www.bannedwordlist.com/lists/swearWords.txt",
        ):
            blockedWords = requests.get(url).text.split("\n")
            for item in blockedWords:
                item = item.strip()
                if (
                    item in msg and item != "" and item != "hell"
                ):  # hell can destroy "hello" and it's not that bad of a word
                    if (
                        "ass" in msg
                        and item == "ass"
                        and "ass" not in msg.replace("grass", "")
                    ):
                        continue  # failsafe for "grass"
                    print(item)
                    raise No([item, msg])
        await bot.change_presence(
            activity=discord.Streaming(
                url="https://www.youtube.com/watch?v=ivSOrKAsPss", name=msg
            )
        )
        return
    choices = (
        "a river",
        "brew out of the faucet",
        "your webcam to 3000 people",
    )  # what is can be changed to
    await bot.change_presence(
        activity=discord.Streaming(
            url="https://www.youtube.com/watch?v=ivSOrKAsPss",
            name=random.choice(choices),
        )
    )  # changes it, link required for streaming status to work


# --When the bot loads--
@bot.event
async def on_ready():
    print(
        "\n-----------------------------------------------\n<----Hits-Head-on-Cabinet has logged in...---->\n-----------------------------------------------"
    )  # tell console bot is logged in
    await bot.change_presence(activity=discord.Game(name="Bot has Started"))
    await asyncio.sleep(5)
    while True:  # repeat forever
        await status()
        await asyncio.sleep(45)


@bot.event
async def on_command_error(ctx, error):
    """
    Does some stuff in case of cooldown error.
    """
    if hasattr(
        ctx.command, "on_error"
    ):  # https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612
        return
    if isinstance(error, commands.CommandOnCooldown):
        potentialMessages = [
            f"This command is on cooldown, please wait {int(error.retry_after)}s."
        ]
        await ctx.send(random.choice(potentialMessages))
        print("\nAn anonymous magcro tried to do a command that was on cooldown")
    if isinstance(error, KeyboardInterrupt):
        await status("Bot offline...")
        await ctx.send("Code 882")
        raise (error)
    else:
        raise (error)


# cog._get_overridden_method(cog.cog_command_error) is not None:
# return


@bot.command("status")
async def setstats(ctx, *args):
    print(f"{ctx.author.name + ctx.author.discriminator} requested a status change.")
    thingy = ""
    for item in args:
        thingy += item
        thingy += " "
    if args == () or args == []:
        thingy = None
    try:
        await status(thingy)
        await thumbsup(ctx)
    except No as ename:
        await ctx.message.delete()
        await ctx.author.send(
            f"Your status change was blocked due to the presence of the following word:\n  {ename}"
        )
        raise Exception("*** BLOCKED STATUS CHANGE.")
    except Exception as ename:
        print(f"{ctx.author.name + ctx.author.discriminator}'s new status ERRORED OUT!")
        await thumbsdown(ctx)  # https://stackoverflow.com/a/62856886/9654083
        await ctx.send(ename)
    await asyncio.sleep(5)
    await status()


@bot.command("fff")
async def Clearchat(ctx):
    user = ctx.author
    role = discord.utils.find(lambda r: r.name == "Mega Brew", ctx.message.guild.roles)
    print(role)
    print(user.roles)
    if role in user.roles:
        string = ""
        for i in range(0, 51):  # repeat 50 times
            string += "\u200b\n"  # add zero width space to string
    else:
        string = "Permission denied."
    print(string)
    await ctx.send(string)


@bot.event
async def on_command_error(ctx, error):
    """
    Does some stuff in case of cooldown error.
    Stolen from hypixel-stats-bot, where it was stolen from brewbot :thinking:
    """
    if hasattr(
        ctx.command, "on_error"
    ):  # https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612
        return
    error = getattr(error, "original", error)
    if isinstance(error, UnreachableCodeError):
        message = _("Unreachable code was run. Contact TheTechRobo for help.")
    elif isinstance(error, commands.CommandOnCooldown):
        potentialMessages = [
            f"This command is on cooldown, please wait {int(error.retry_after)}s."
        ]
        message = random.choice(potentialMessages)
        print("\nSomeone tried to do a command that was on cooldown")
    elif isinstance(error, commands.MissingRequiredArgument):
        strerror = str(error).split(" ")[0]
        message = _(
            'You seem to be missing a required argument "{strerror}". Run `{PREFIX}help [command]` for more information.'
        ).format(PREFIX=PREFIX, strerror=strerror)
    elif isinstance(error, commands.errors.CommandNotFound):
        message = _("Unknown command. Try {PREFIX}help for a list!").format(
            PREFIX=PREFIX
        )
    elif isinstance(error, KeyError):
        message = _("Dubious error checking. Contact TheTechRobo for help.")
    else:
        message = "Unknown error !"
    em = discord.Embed(title=_("⚠️ Oops! ⚠️"), description=message)
    em.set_footer(text=error)
    await ctx.send(embed=em)
    raise (error)


try:
    bot.run("ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20")
except KeyboardInterrupt:
    print("Caught KeyboardInterrupt")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.change_presence(status=discord.Status.offline))
