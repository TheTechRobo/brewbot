import random, discord
def TheColoursOfTheRainbow(): #to choose a random RGB value
    colours = []
    for i in range(0,3):
        colours.append(random.randint(0,255))
    return colours

def SetEmbed(title, url=False, description, colour=False, img=False, footer=False):
    """
    params are self explanatory.
    returns the embed.
    """
    if not colour:
        colour = TheColoursOfTheRainbow()
        colour = discord.Color.from_rgb(*colour)
    mountEmbed = discord.Embed(title=title, description=description, color=colour)
    if not img: pass
    else:  mountEmbed.set_image(url=img)
    if not footer: pass
    else: mountEmbed.set_footer(text=footer)
    if not url: pass
    else: mountEmbed.set_url(url=url)
    return mountEmbed
