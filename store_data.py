from addBrewcoin import scores
StoreItemsVar = {"Brew": 30, "Giant Brew": 50, "Brewcoin Doubler (2h)": 12, "Make Brewbot Open Source": 1500, "x2 multiplyer (4h)": 20}
StoreItemsVar = {"Brew": {"id": "role:brew", "type": "role", "price": 50}, "Giant Brew": {"id": "role:giantBrew", "type": "role", "price": 50}, "Brewcoin Doubler (2h)": {"id": "multiplyer:double2", "type": "multiplyer", "price": 11}}
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
    data.scores['multiplyerTime'][user] = time

TypeMap = {"x2 multiplyer (4h)": "multiplyer"}
