"""
This is the rewrite that is in progress for the Brew Discord bot. It uses the bot.command rather than the client.event since I think that it is better maybe??? I really dont know.
"""
import discord, configparser
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix='brew ') #makes the prefix << brew >>



@bot.command(name='test')
async def test(context): #needs the context - Context means that it will send it in the channel that the message was sent in.
    user = context.author
    await context.send(f'Hi {user}, you are senche raht :beer:')

@bot.command(name='spam')
async def spam(context, END): #context is the content, end is the last thing
    channel = context.channel
    print(channel.name)
    if channel.name == 'brew-spamming':
        pass
    else:
        print(channel.name == "brew-spamming") #logging
        await context.send(f'Please only use this command in the correct channel') #cant figure this out. it does equal brew-spamming and it still does this...g
        return
    for i in range(0, int(END)):
        await context.send(f'Brew!! :beer:')

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command(name='mine')
async def test(context): #needs the context - Context means that it will send it in the channel that the message was sent in.
    user=context.author
    await context.send(f'Hi {user}, this is testing')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'The drill is overheated. You cannot brewcoin yet. Please wait {int(error.retry_after)}s.')
    raise error

bot.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')
