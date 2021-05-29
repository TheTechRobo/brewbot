import json
class NiceTry(Exception):
    pass
def addbrewcoin(amount, user):
    amount = int(amount)

    with open("scores.json","r") as file:
        scores = json.load(file)

    try: #gets the multiplyer
        multiplyer = float(scores["multiplyers"][user])
    except KeyError: #if none, assigns 0
        scores["multiplyers"][str(user)] = 1
        multiplyer = 1

    try: #assigns the brewcoins
        userCoin = float(scores["scores"][user])
        userCoin += (amount * multiplyer)
        scores["scores"][user] = userCoin
    except KeyError: #if user has none, assigns the amount
        scores[scores][user] = multiplyer * amount

    with open('scores.json', 'w+') as confs:
        confs.write(json.dumps(scores))
    return multiplyer*amount, userCoin, multiplyer

def rembrewcoin(amount, user, usemultiplyer=True):
    amount = int(amount)

    with open("scores.json","r") as file:
        scores = json.load(file)
    if amount < 0:
        raise NiceTry("YOU GOT CAUGHT HAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\nYou pay the person you stole from **1** brewcoin.")
    try: #gets the multiplyer
        multiplyer = float(scores["multiplyers"][user])
    except KeyError: #if none, assigns 0
        scores["multiplyers"][str(user)] = 1
        multiplyer = 1
    if not usemultiplyer:
        multiplyer = 1
    try: #assigns the brewcoins
        userCoin = float(scores["scores"][user])
        userCoin -= (amount * multiplyer)
        scores["scores"][user] = userCoin
    except KeyError: #if user has none, assigns the amount
        scores[scores][user] = multiplyer * amount

    with open('scores.json', 'w+') as confs:
        confs.write(json.dumps(scores))
    return multiplyer*amount, userCoin, multiplyer
