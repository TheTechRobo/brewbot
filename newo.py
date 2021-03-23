"""
BrewBot
NOTE TO TRM : REMEMBER TO USE RETURN TO END THINGS
"""

import discord, configparser

scores = configparser.ConfigParser()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("\n\nMessage sent in ", message.channel)
    print(message.author, "sent the message <<", message.content, ">>")
    if message.author == client.user:
        return
    if message.content == "brew":
        scores.read("brewscores.ini")
        try:
            scores["scores"][message.author]
            Iscores = int(scores["scores"][message.author])
            Iscores += 1
            scores["scores"][message.author] = str(Iscores)
        except:
            scores["scores"][str(message.author)] = "1"
        with open('brewscores.ini', 'w') as confs:
            scores.write(confs)
    if message.content.startswith('brew'):
        if message.content.startswith('brew bal'):
            await message.channel.send('BALANCE: 0 because this bot isnt finished!!!!!!!111111')
            return
        elif message.content.startswith('brew spam'):
            if message.channel.name != "brew-spamming":
                await message.channel.send('Please only spam brews in the #brew-spamming channel :beer:')
                return #exits the elif statement, does not execute the brew spam
            try:
                numberOfTimes = int(str(message.content).split()[2])
                print(numberOfTimes)
                if numberOfTimes <= 15: #limits spamming to 15
                    for i in range(0, numberOfTimes): #sends it 9 times
                        await message.channel.send('brew :beer:')
                    return
                else:
                    await message.channel.send("I don't want to block this, but it will probably really lag the server... So please limit auto spamming brew to 15...")
                    return
            except Exception:
                await message.channel.send('brew :beer:')
                return
        await message.channel.send('Brew!! :beer: :beer:')

client.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')
