import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('brew'):
        await message.channel.send('brew!')

client.run('ODIzNzIwNjY5MjgzMzUyNjI3.YFk7pw.jgUCv0ig0_oc2u4H5rQ16dXyhaQ')

