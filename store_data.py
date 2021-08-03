from addBrewcoin import scores

def SetupStoreItemsVar(thing):
    return {
        "Brew": {"id": "role:brew", "type": "role", "price": 50},
        "Giant Brew": {"id": "role:giantBrew", "type": "role", "price": 50},
        "Brewcoin Doubler (2h)": {"id": "multiplyer:double2", "type": "multiplyer", "price": 11, "time": 7200, "times": 2},
        "Brewcoin Doubler (4h)": {"id": "mutliplyer:double4", "type": "multiplyer", "price": 21, "time": 14400, "times": 2},
        "Make Brewbot Open Source": {"id": "open", "type": "dm", "price": 1500, "to": thing}}

hi = '''Brewbot is unfortunately currently closed source because of the rat TheRuntingMuumuu. Together we can stop this!!! Save up 1500 brewcoin for the perk!!!! Help me other people. YOu're my only hope.'''

def addMult(user, val, time):
    data = scores.json()
    data.read()
    data.checkMultiplyers(user)
    try:
        if data.scores['multiplyers'][user] != 1:
            return "ALREADY"
    except KeyError:
        pass
    data.scores['multiplyers'][user] = val
    data.scores['multiplyerTime'][user] = time

