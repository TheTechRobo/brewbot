"""
This is the rewrite that is in progress for the Brew Discord bot.
It uses the bot.command rather than the client.event since it's much
easier to maintain.
"""
import configparser
from discord.ext import commands
from discord.ext.commands import Bot
import random
import discord

bot = Bot(command_prefix=('brew ', 'Brew ')) #makes the prefix << brew >>
scores = configparser.ConfigParser()

@bot.command(name='test')
async def test(context): #needs the context - Context means that it will send it in the channel that the message was sent in.
    user = context.author
    await context.send(f'Hi {user}, you are senche raht :beer:')

@bot.command(name='spam')
async def spam(context, END): #context is the content, end is the last thing
    """
    Takes one parameter: how many times to spam.
    """
    channel = context.channel
    print(channel.name)
    if channel.name == 'brew-spamming':
        pass
    else:
        print(channel.name == "brew-spamming") #logging
        await context.send('Please only use this command in the correct channel')
        return
    if int(END) <=30:
        for i in range(0, int(END) + 1):
            await context.send('Brew!! :beer:')
            del i
    else:
        await context.send(f'I don\'t want to block this, but it will probably really lag the server... So please limit auto spamming brew to 15...')

@commands.cooldown(1, 50, commands.BucketType.guild)
@bot.command(name='mine')
async def mine(context):
    """
    Brewcoin Mining
    """
    scores.read("brewscores.ini")
    name = context.author.name + "#" + context.author.discriminator
    if random.randint(0,4) == 0:
        try:
            scores["scores"][name]
            Iscores = int(scores["scores"][name])
            Iscores += 1
            scores["scores"][name] = str(Iscores)
        except KeyError:
            logging.warning("EXCEPTION IN SCORING: %s" % ename)
            scores["scores"][str(name)] = "1"
            Iscores = 1
        with open('brewscores.ini', 'w') as confs:
            scores.write(confs)
        await context.send(f'You got a brewcoin!! You now have {Iscores}')
    else:
        await context.send(f'Sorry, you have rotten luck... You did not get a brewcoin... :cry:')

@bot.event
async def on_command_error(ctx, error):
    """
    Does some stuff in case of cooldown error.
    """
    if isinstance(error, commands.CommandOnCooldown):
        potentialMessages = [f'This command is on cooldown, please wait {int(error.retry_after)}s.', 'Searching for more coins to excavate...', f'The GPU overheated. Hopefully it did not die, or you may have a hard time finding a new one... {int(error.retry_after)}s.', f'You should not be greedy and mine too many brewcoins... Please try again in {int(error.retry_after)}s.', f'The drill is overheated. You cannot brewcoin yet. Please wait {int(error.retry_after)}s.', f'Bad things may happen if you do not wait {int(error.retry_after)} more seconds before mining again... :ghost:']
        await ctx.send(random.choice(potentialMessages))
    raise error

bot.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')