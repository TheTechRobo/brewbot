import json
class NiceTry(Exception):
    pass

class scores:
    pass
class json:
    def __init__(self, filename="scores.json"):
        self.filename = filename
        self.scores = {}
    def read(self):
        with open(self.filename) as file:
            self.scores = file.read()
    def write(self):
        with open(self.filename, "w+") as file:
            file.write(json.dumps(self.scores, indent=4))
    def addBrewcoin(amountount, user, usemultiplyer=True):
        amount = float(amount)
        try:
            multiplyer = float(scores['multiplyers'][user])
        except KeyError: #if their multiplyer doesn't exist they need to be reregistered
            scores['multiplyers'][str(user)] = 1
            multiplyer = 1
        if not usemultiplyer:
            multiplyer = 1
        try:
            userCoin = float(scores['scores'][user])
            userCoin += (amount * multiplyer)
            scores['scores'][user] = userCoin
        except KeyError: #if user has none they need to be registered
            userCoin = multiplyer * amount
            scores['scores'][user] = userCoin
        return multiplyer*amount, userCoin, multiplyer
    def remBrewcoin(**kwargs):
        amount = float(kwargs['amount'])
        if amount < 0:
            raise NiceTry("YOU GOT CAUGHT HAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\nYou pay the person you stole from **1** brewcoin.")
        amount = 0 - amount ##https://stackoverflow.com/a/67205684/9654083, we know it's postive since, well... 1 line above
        kwargs['amount'] = amount
        return self.addBrewcoin(**kwargs)
def addbrewcoin(*args, **kwargs):
    obj = scores.json()
    obj.read()
    a = obj.addBrewcoin(*args, **kwargs)
    obj.write()
    return a
def rembrewcoin(*args, **kwargs):
    obj = scores.json()
    obj.read()
    a = obj.remBrewcoin(*args, **kwargs)
    obj.write()
    return a
