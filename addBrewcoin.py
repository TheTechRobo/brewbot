import json
def addbrewcoin(amount, user):
    amount = int(amount)

    scores = json.load("scores.json")
    try: #gets the multiplyer
        multiplyer = int(scores["multiplyers"][user])
    except KeyError: #if none, assigns 0
        scores["multiplyers"][str(user)] = 1
        multiplyer = 1

    try: #assigns the brewcoins
        userCoin = scores["scores"][user]
        userCoin += (amount * multiplyer)
        scores["scores"][user] = userCoin
    except KeyError: #if user has none, assigns the amount
        scores[scores][user] = multiplyer * amount

    with open('scores.json', 'w+') as confs:
        confs.write(json.dumps(scores))
    return multiplyer*amount, userCoin, multiplyer
