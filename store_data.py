from addBrewcoin import scores
import time
class Multiplyer:
    def __init__(self, name, price, time, val):
        self.price = price
        self.name = name
        self.time = time
        self.val = val
    def run(self, user):
        data = scores.json()
        data.read()
        data.checkMultiplyer(user)
        try:
            data.scores['multiplyers'][user]
            if data.scores['multiplyers'][user] != 1:
                return "ALREADY"
        except KeyError:
            return "UNINIT"
        data.scores['multiplyers'][user] = self.val
        data.scores['multiplyerTime'][user] = int(time.time()) + 1  + self.time
        data.write()
StoreItems = [Multiplyer("Brewcoin Doubler (2h)", 12, 7200, 2)]
StoreItemsVar = {"Brew": {'price': 30, 'type': 'multiplyer'}, "Giant Brew": 50, "Brewcoin Doubler (2h)": 12, "Make Brewbot Open Source": 1500, "x2 multiplyer (4h)": 20}
hi = '''Brewbot is unfortunately currently closed source because of the rat TheRuntingMuumuu. Together we can stop this!!! Save up 1500 brewcoin for the perk!!!! Help me other people. YOu're my only hope.'''

def addMult(user, val, time):
    data = scores.json()
    data.read()
    data.checkMultiplyers(user)
    try:
        data.scores['multiplyers'][user]
        if data.scores['multiplyers'][user] != 1:
            raise KeyError
    except KeyError:
        return "ALREADY"
    data.scores['multiplyers'][user] = val
    data.scores['multiplyerTime'][user] = int(time.time()) + 1  + time
