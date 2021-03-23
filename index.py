"""
This is the rewrite that is in progress for the Brew Discord bot. It uses the bot.command rather than the client.event since I think that it is better maybe??? I really dont know.
"""
import discord, configparser
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix='brew ') #makes the prefix << brew >>

@bot.command(name='test')
async def test(context): #needs the context - Context means that it will send it in the channel that the message was sent in.
    user=context.author
    await context.send(f'Hi {user}, you are senche raht :beer:')

@bot.command(name='spam')
async def spam(context): #needs the context - Context means that it will send it in the channel that the message was sent in.
    await context.send(f'Magden')
    range = 4
    channel = context.channel
    if channel != 'brew-spamming':
        await context.send(f'Please only use this command in the correct channel')
        return
    await context.send(f'Stamden')
    for i in range(0, range):
        await context.send(f'Brew!! :beer:')

bot.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')
