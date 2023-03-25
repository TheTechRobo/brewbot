"""
FILE: Brewbot 2
VERSION: v.2.0.1 WIP
AUTHORS: TheRuntingMuumuu, TheTechRobo
LICENSE: Proprietary
SOURCE STATUS: Closed Source
ABOUT: This is version 2 of the brewbot that I am making. It is mostly remember how to write code and stuff. The bot itself will serve absolutely no purpose, but it will be fun!!! 😀
SOURCES: in the comments or in sources.txt
"""

#--- → Imports ← ---
import os

import arrow
import discord

#--- → Modifying Variables ← ---
# This is the token used for linking the bot

TOKEN = os.getenv('TOKEN')
if not TOKEN: # if TOKEN is None or empty
    raise ValueError('Missing environment variable TOKEN for Discord token!')

#--- → Setting up the bot ← ---
#Intents, this is the connection to discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#--- → When the bot loads ← ---
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#--- → When any message is sent ← ---
@client.event
async def on_message(message):
    timestamp = arrow.get(message.created_at).replace(tzinfo='local') \
            .format('YYYY-MM-DD HH:mm:ss ZZ')
    print(f'<{message.author}>\t@ [{timestamp}]:\t{message.content}')

    #checks if it is the bot sending the message
    if message.author == client.user:
        return

    #if the message is brew, reply
    if message.content.startswith('brew'):
        await message.channel.send('brew')


#-- → Runs the bot with the token ← ---
client.run(TOKEN)
