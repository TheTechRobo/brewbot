import discord, brewscores

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message.channel)
    if message.author == client.user:
        return
    if message.content == "use for future":
        try:
            brewscores.scores[message.author] += 1
        except:
            brewscores.scores[message.author] = 1
    if message.content.startswith('brew'):
        if message.content.startswith('brew bal'):
            await message.channel.send('BALANCE: 0 because this bot isnt finished!!!!!!!111111')
            return
        elif message.content.startswith('brew spam'):
            if message.channel.name != "brew-spamming":
                await message.channel.send('Please only spam brews in the #brew-spamming channel :beer:')
                return
            numberOfTimes = int(str(message.content).split()[2])
            print(numberOfTimes)
            for i in range(0, numberOfTimes): #sends it 9 times
                await message.channel.send('brew :beer:')
            return
        elif message.content.startswith('brew'):
            await message.channel.send('Brew!! :beer: :beer:')

client.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')
