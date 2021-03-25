"""
https://stackoverflow.com/a/65436253/9654083
https://stackoverflow.com/questions/60055037/how-make-custom-status-discord-py
This is the rewrite that is in progress for the Brew Discord bot.
It uses the bot.command rather than the client.event since it's much
easier to maintain.
"""
import configparser, logging
from discord.ext import commands
from discord.ext.commands import Bot
import random
import discord
from store_data import *

bot = Bot(command_prefix=('brew ', 'Brew ')) #makes the prefix << brew >>
scores = configparser.ConfigParser()

@bot.event #writes in terminal if the bot logs in
async def on_ready():
    print("Logged in")
    choices = ["a river","brew out of the faucet"]
    await bot.change_presence(activity=discord.Streaming(url="https://www.youtube.com/watch?v=ivSOrKAsPss", name=random.choice(choices)))

def TheColoursOfTheRainbow(): #to choose a random RGB value
    colours = []
    for i in range(0,3):
        colours.append(random.randint(0,255))
    return colours

@bot.command(name='ping', aliases=['test'])
async def test(context):
    """
    tests if the bot exists
    """
    user = context.author
    await context.send(f'Hi {user}, you are senche raht :beer:')


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

@commands.cooldown(1, 45, commands.BucketType.guild)
@bot.command(name='mine')
async def mine(context):
    """
    Small chance of getting a brewcoin! 45 second cooldown.
    """
    scores.read("brewscores.ini")
    name = context.author.name + "#" + context.author.discriminator
    name = name.lower()
    channel = context.channel
    if channel.name == 'brewcoin-mining':
        pass
    else:
        print(f"wrong channel, user in {channel.name}") #logging
        await context.send('Please only use this command in the correct channel')
        mine.reset_cooldown(context)
        return
    if random.randint(0,6) == 0:
        try:
            Iscores = int(scores["scores"][name])
            Iscores += 1
            scores["scores"][name] = str(Iscores)
        except KeyError as ename:
            logging.warning("EXCEPTION IN SCORING: %s" % ename)
            scores["scores"][str(name)] = "1"
            Iscores = 1
        with open('brewscores.ini', 'w') as confs:
            scores.write(confs)
        await context.send(f'You got a brewcoin!! You now have {Iscores}')
    else:
        cs = TheColoursOfTheRainbow()
        balEmbed = discord.Embed(title="No", description='You did not get brewcoin', color=discord.Color.from_rgb(*cs)) #todo add random colouring here
        balEmbed.set_image(url = "https://thetechrobo.github.io/youtried.png")
        balEmbed.set_footer(text="no brew coin for you")
        await context.send(embed = balEmbed)

@bot.event
async def on_command_error(ctx, error):
    """
    Does some stuff in case of cooldown error.
    """
    if isinstance(error, commands.CommandOnCooldown):
        potentialMessages = [f'This command is on cooldown, please wait {int(error.retry_after)}s.', f'Searching for more coins to excavate... ({int(error.retry_after)}s)', f'The GPU overheated. Hopefully it did not die, or you may have a hard time finding a new one... {int(error.retry_after)}s.', f'You should not be greedy and mine too many brewcoins... Please try again in {int(error.retry_after)}s.', f'The drill is overheated. You cannot brewcoin yet. Please wait {int(error.retry_after)}s.', f'Bad things may happen if you do not wait {int(error.retry_after)} more seconds before mining again... :ghost:']
        await ctx.send(random.choice(potentialMessages))
        raise error

@commands.cooldown(1,4,commands.BucketType.guild)
@bot.command(name='bal')
async def bal(context, user=None):
    """
    Check your balance!
    """
    name = context.author.name + "#" + context.author.discriminator
    name = name.lower()
    scores.read("brewscores.ini")
    if user is None:
        try:
            Iscores = int(scores["scores"][name])
        except KeyError:
            Iscores = 0
        colours = TheColoursOfTheRainbow()
        balEmbed = discord.Embed(title="Balance", description=f'Your current balance is {Iscores} brewcoins!', color=discord.Color.from_rgb(*colours))
        await context.send(embed = balEmbed)
    else:
        await context.send('Sorry, but specifying a user is not yet supported. Try again soon!')



@commands.cooldown(1,30,commands.BucketType.guild) #Funny senche raht thing
@bot.command(name='senche')
async def senche(context):
    sencheEmbed = discord.Embed(title="Senche Raht", url="https://en.uesp.net/wiki/Online:Senche-raht", description=f'This is a senche raht. Not a mount. (if you are curious, search up \"Senche Raht\'s, Not Mounts\")', color=0xffffff)
    sencheEmbed.set_image(url = "https://th.bing.com/th/id/OIP.E_zqHOXGiW7RjFR8rLndhAHaJb?pid=ImgDet&rs=1")
    sencheEmbed.set_footer(text="Senche raht",)
    await context.send(embed = sencheEmbed)

@commands.cooldown(1,30,commands.BucketType.guild)
@bot.command(name='mount')
async def mount(context):
    mountEmbed = discord.Embed(title="WE ARE NOT MOUNTS", url="https://en.uesp.net/wiki/Online:Senche-rahts:_Not_Just_Mounts", description=f'WE ARE NOT MOUNTS, We are intelligent beings who are not just mounts. See more information at the link above.)', color=0xffffff)
    mountEmbed.set_image(url = "https://cdna.artstation.com/p/assets/covers/images/017/378/304/large/meg-steckler-shot97thumb.jpg?1555712613")
    mountEmbed.set_footer(text="Riders dont \"Own\" us, they are our \"Partners\".",)
    await context.send(embed = mountEmbed)

@bot.command(name='version')
async def v(context):
    versionEmbed = discord.Embed(title="brewbot 0.1-wip", color=0xafdfff)
    versionEmbed.set_footer(text=hi)
    await context.send(embed = versionEmbed)

@bot.command(name='wash')
async def wash(context):
    await context.send("https://www.youtube.com/watch?v=ivSOrKAsPss")

@bot.command(name='sponsor')
async def sponsor(context):
    sponsor = discord.Embed(title="Sponsors", description="This bot is sponsored by TheRuntingMuumuu from trm.ddns.net, and TheTechRobo from (IDK). \nWell it is not actually sponsored by them but it is made by them, and hosted by them, and paid for by them (for the power for hosting, and time for deving) and so on.")
    await context.send(embed = sponsor)


bot.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')
