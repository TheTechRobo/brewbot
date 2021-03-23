"""
BrewBot
NOTE TO TRM : REMEMBER TO USE RETURN TO END THINGS A
TODO: Gettext
TODO: Fix scoring system
TODO: Add more features
"""

import discord, configparser, logging, random, time

logging.basicConfig(level=logging.INFO, format='%(levelname)s @ %(asctime)s: %(message)s; Lineno %(lineno)d, func %(funcName)s, file %(filename)s.', datefmt='%d/%m/%Y %H:%M:%S')
# Logging format:
# LEVEL @ DAY/MO/YEAR HOUR:MINUTE:SECOND: MESSAGE; Lineno LINENUMBER, func FUNCTION, file FILE.
# Example:
# INFO @ 23/03/2021 09:58:44: Cleaning up after 1 tasks; Lineno 71, func _cancel_tasks, file client.py.

scores = configparser.ConfigParser()
client = discord.Client()

def getScore(message):
        scores.read("brewscores.ini")
        name = message.author.name + "#" + message.author.discriminator
        scores["scores"][name]
        Iscores = int(scores["scores"][name])
        return Iscores

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    logging.info(f"\n\nMessage sent in {message.channel}")
    logging.info(f"{message.author} sent the message << {message.content} >>")
    if message.author == client.user:
        return
    if message.content.startswith('brew'):
        if message.content.startswith('brew bal'):
            await message.channel.send(f'Your brewcoin balance is {getScore(message)} @{message.author}')
            return
        elif message.content.startswith('brew spam'):
            if message.channel.name != "brew-spamming":
                await message.channel.send('Please only spam brews in the #brew-spamming channel :beer:')
                return #exits the elif statement, does not execute the brew spam
            try:
                numberOfTimes = int(str(message.content).split()[2])
                print(numberOfTimes)
                if numberOfTimes <= 16:
                    for i in range(0, numberOfTimes):
                        await message.channel.send('brew :beer:')
                    return
                else:
                    logging.info(f"Blocked message (metadata: {message})")
                    await message.channel.send("I don't want to block this, but it will probably really lag the server... So please limit auto spamming brew to 15...")
                    return
            except Exception:
                await message.channel.send('brew :beer:')
                return
        elif message.content == "brew mine":
            await BrewCoinMine(message)
            return
        await message.channel.send('Brew!! :beer: :beer:')

async def BrewCoinMine(message):
    scores.read("brewscores.ini")
    name = message.author.name + "#" + message.author.discriminator
    try:
       if (scores["cooldown"][name] + 5) >= int(time.time()):
           await message.channel.send("cooldown")
           return
       else:
           await message.channel.send("pass")
    except KeyError: pass
    if random.randint(0,4) == 2 and message.channel.name == "brewcoin-mining":
        try:
            scores["scores"][name]
            Iscores = int(scores["scores"][name])
            Iscores += 1
            scores["scores"][name] = str(Iscores)
        except KeyError:
            logging.warning("EXCEPTION IN SCORING: %s" % ename)
            scores["scores"][str(name)] = "1"
        print('hi')
        print(scores["cooldown"])
        scores["cooldown"][str(name)] = str(int(time.time()))

        with open('brewscores.ini', 'w') as confs:
            scores.write(confs)
        await message.channel.send(f'You got a brewcoin!! You now have {Iscores}')
        return
    else:
        await message.channel.send('Sorry, No luck...')
        return

client.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')
