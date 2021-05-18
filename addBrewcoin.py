import configparser
def addbrewcoin(amount, user):
    amount = int(amount)
    scores = configparser.ConfigParser()

    scores.read("brewscores.ini") #reads the file
    try: #gets the multiplyer
        multiplyer = int(scores["multiplyers"][user])
    except KeyError: #if none, assigns 0
        scores["multiplyers"][str(user)] = "1"
        multiplyer = 1

    try: #assigns the brewcoins
        userCoin = int(scores["scores"][user])
        userCoin += (amount * multiplyer)
        scores["scores"][user] = str(userCoin)
    except KeyError: #if user has none, assigns 1
        scores[scores][user] = str(multiplyer*1)

    with open('brewscores.ini', 'w') as confs:
        scores.write(confs)
    return multiplyer*amount, userCoin, multiplyer
