import json, time
class NiceTry(Exception):
    pass

class scores:
    class json:
        def lookUpById(self, id: str):
            id = str(id)
            return self.scores["mapping"][id]
        def setUpById(self, id: str, usernameWithDiscrim: str):
            """usernameWithDiscrim should be in the format username#disc"""
            self.scores[mapping][str(id)] = usernameWithDiscrim
        def __init__(self, filename="scores.json"):
            self.filename = filename
            self.scores = {}
        def checkMultiplyer(self, user):
            user = str(user)
            try:
                int(user)
            except Exception as ename:
                raise ValueError("You passed a Username instead of an UserID. Usernames functionality has been removed. Please update your code. Thank you!")
            try:
                self.scores['multiplyerTime'][user]
            except KeyError:
                self.scores['multiplyerTime'][user] = 1
            if time.time() > self.scores['multiplyerTime'][user]:
                self.scores['multiplyers'][user] = 1
        def read(self):
            with open(self.filename) as file:
                self.scores = json.loads(file.read())
        def write(self):
            with open(self.filename, "w+") as file:
                file.write(json.dumps(self.scores, indent=4))
        def addBrewcoin(self, amount, user, remov=False, usemultiplyer=True, checkMultiplyer=True):
            userClass = user
            user = str(userClass.id)
            usern = str(userClass.name + "#" + userClass.discriminator)
            try:
                int(user)
            except Exception as ename:
                raise ValueError("You passed a Username instead of an UserID. Usernames functionality has been removed. Please update your code. Thank you!")
            amount = float(amount)
            try:
                if not checkMultiplyer: raise KeyError
                self.checkMultiplyer(user)
            except KeyError:
                pass
            try:
                multiplyer = float(self.scores['multiplyers'][user])
            except KeyError: #if their multiplyer doesn't exist they need to be reregistered
                self.setUpById(usern)
                self.scores['multiplyers'][str(user)] = 1
                multiplyer = 1
            if not usemultiplyer:
                multiplyer = 1
            try:
                userCoin = float(self.scores['scores'][user])
                userCoin += amount * multiplyer
                if self.scores['scores'][user] - userCoin < 0 and remov is True:
                    raise ValueError("Too little funds!!")
                self.scores['scores'][user] = userCoin
            except KeyError: #if user has none they need to be registered
            #    raise NiceTry("Sus")
                userCoin = amount * multiplyer
                self.scores['scores'][user] = userCoin
            return multiplyer*amount, userCoin, multiplyer
        def remBrewcoin(self, **kwargs):
            amount = float(kwargs['amount'])
            if amount < 0:
                raise NiceTry("YOU GOT CAUGHT HAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\nYou pay the person you stole from **1** brewcoin.")
            amount = 0 - amount #https://stackoverflow.com/a/67205684/9654083, we know it's postive since, well... 1 line above
            kwargs['amount'] = amount
            return self.addBrewcoin(**kwargs, remov=True)
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
