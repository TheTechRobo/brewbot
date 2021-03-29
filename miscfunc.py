import random
def TheColoursOfTheRainbow(): #to choose a random RGB value
    colours = []
    for i in range(0,3):
        colours.append(random.randint(0,255))
    return colours
