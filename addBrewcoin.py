import json, time
class NiceTry(Exception):
    pass

class scores:
    class json:
        def __init__(self, filename="scores.json"):
            self.filename = filename
            self.scores = {}
        def checkMultiplyer(self, user):
            if time.time() > self.scores['multiplyerTime'][user]:
                self.scores['multiplyers'][user] = 1
        def read(self):
            with open(self.filename) as file:
                self.scores = json.loads(file.read())
        def write(self):
            with open(self.filename, "w+") as file:
                file.write(json.dumps(self.scores, indent=4))
        def addBrewcoin(self, amount, user, usemultiplyer=True):
            amount = float(amount)
            try:
                multiplyer = float(self.scores['multiplyers'][user])
            except KeyError: #if their multiplyer doesn't exist they need to be reregistered
                self.scores['multiplyers'][str(user)] = 1
                multiplyer = 1
            if not usemultiplyer:
                multiplyer = 1
            try:
                userCoin = float(self.scores['scores'][user])
                userCoin += (amount * multiplyer)
                self.scores['scores'][user] = userCoin
            except KeyError: #if user has none they need to be registered
                userCoin = multiplyer * amount
                self.scores['scores'][user] = userCoin
            return multiplyer*amount, userCoin, multiplyer
        def remBrewcoin(self, **kwargs):
            amount = float(kwargs['amount'])
            if amount < 0 and random.randint(1,1000) != 1: #1 IN 1000 CHANCE!!! NOT CLICKBAIT!!! 4K!!!!! (ENDING WILL SHOCK YOU) (GONE WRONG)
                raise NiceTry("YOU GOT CAUGHT HAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\nYou pay the person you stole from **1** brewcoin.")
            amount = 0 - amount #https://stackoverflow.com/a/67205684/9654083, we know it's postive since, well... 1 line above
            kwargs['amount'] = amount
            return self.addBrewcoin(**kwargs)
def addbrewcoin(**kwargs):
    obj = scores.json()
    obj.read()
    try:
        obj.checkMultiplyer(kwargs['user'])
    except KeyError:
        pass
    a = obj.addBrewcoin(*args, **kwargs)
    obj.write()
    return a
def rembrewcoin(**kwargs):
    obj = scores.json()
    obj.read()
    try:
        obj.checkMultiplyer(kwargs['user'])
    except KeyError:
        pass
    a = obj.remBrewcoin(**kwargs)
    obj.write()
    return a
