import json
class NiceTry(Exception):
    pass
def addbrewcoin(amount, user, usemultiplyer=True):
    amount = float(amount)

    with open("scores.json","r") as file:
        scores = json.load(file)

    try: #gets the multiplyer
        multiplyer = float(scores["multiplyers"][user])
    except KeyError: #if none, assigns 0
        scores["multiplyers"][str(user)] = 1
        multiplyer = 1
    if not usemultiplyer:
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

def rembrewcoin(**kwargs):
    amount = float(kwargs['amount'])
    if amount < 0:
        raise NiceTry("YOU GOT CAUGHT HAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\nYou pay the person you stole from **1** brewcoin.")
    amount = 0 - amount #https://stackoverflow.com/a/67205684/9654083, we know it's postive since, well... 1 line above
    kwargs['amount'] = amount
    addbrewcoin(**kwargs)
