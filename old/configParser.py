FILE = "brewscores.ini"

import json, configparser

scores = configparser.ConfigParser()
scores.read(FILE)

with open("scores.json", "w+") as file:
    hi = {}
    for item in scores["scores"]:
        hi[item] = scores["scores"][item]
    stuff = scores["scores"]
    file.write(json.dumps(hi))
