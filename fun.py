import configparser, logging
from discord.ext import commands
from discord.ext.commands import Bot
import random
import discord

print("MagDK")

bot = Bot(command_prefix=('brew ', 'Brew ')) #needs to also be here so that these commands know what to listen for

@bot.command(name='wash')
async def wash(context):
    print("Stamden")
    await context.send("https://www.youtube.com/watch?v=ivSOrKAsPss")
print("Magplar")

@commands.cooldown(1,30,commands.BucketType.guild) #Funny senche raht thing
@bot.command(name='senche')
async def senche(context):
    sencheEmbed = discord.Embed(title="Senche Raht", url="https://en.uesp.net/wiki/Online:Senche-raht", description=f'This is a senche raht. Not a mount. (if you are curious, search up \"Senche Raht\'s, Not Mounts\")', color=0xffffff)
    sencheEmbed.set_image(url = "https://th.bing.com/th/id/OIP.E_zqHOXGiW7RjFR8rLndhAHaJb?pid=ImgDet&rs=1")
    sencheEmbed.set_footer(text="Senche raht",)
    await context.send(embed = sencheEmbed)

@commands.cooldown(1,30,commands.BucketType.guild)
@bot.command(name='mount')
async def mount(context):
    mountEmbed = discord.Embed(title="WE ARE NOT MOUNTS", url="https://en.uesp.net/wiki/Online:Senche-rahts:_Not_Just_Mounts", description=f'WE ARE NOT MOUNTS, We are intelligent beings who are not just mounts. See more information at the link above.)', color=0xffffff)
    mountEmbed.set_image(url = "https://cdna.artstation.com/p/assets/covers/images/017/378/304/large/meg-steckler-shot97thumb.jpg?1555712613")
    mountEmbed.set_footer(text="Riders dont \"Own\" us, they are our \"Partners\".",)
    await context.send(embed = mountEmbed)

@bot.command(name='wraith', aliases=['wrath'])
async def wraith(context):
    wrathRand = random.randint(0, 2)
    wrathText = ["This is a wraith from ESO.", "This is a scary wraith", "This is wraith from Apex Legends"]
    wrathImage = ["https://th.bing.com/th/id/Rc930387dd1629d1285808a19da20c327?rik=9lR%2fB6vEbuFq3A&riu=http%3a%2f%2fvignette2.wikia.nocookie.net%2felderscrolls%2fimages%2f7%2f7c%2fWraith.png%2frevision%2flatest%3fcb%3d20160207025617&ehk=a0crJjrw3xwAap1mOQIXVJC73tfBiqhw%2fXEqvr2vJho%3d&risl=&pid=ImgRaw", "https://vignette.wikia.nocookie.net/romanticallyapocalyptic/images/7/7c/Wraith.png/revision/latest/scale-to-width-down/370?cb=20120724162754", "https://d1fs8ljxwyzba6.cloudfront.net/assets/article/2019/02/21/wraith-guide-header-apex-legends_feature.jpg"]
    wrathEmbed = discord.Embed(title="Wraith", description=wrathText[wrathRand], color=0xffffff)
    wrathEmbed.set_image(url=wrathImage[wrathRand])
    await context.send(embed = wrathEmbed)
