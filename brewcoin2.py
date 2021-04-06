import discord
from discord.ext import commands
import configparser
import random
from store_data import *
from miscfunc import *
import logging
import datetime

scores = configparser.ConfigParser()

class brewcoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 45, commands.BucketType.guild)
    @commands.command(name='mine')
    async def mine(self, context):
        """
        Small chance of getting a brewcoin! 45 second cooldown.
        """
        scores.read("brewscores.ini")
        name = context.author.name + "#" + context.author.discriminator
        name = name.lower()
        channel = context.channel
        if channel.name == 'brewcoin-mining':
            pass
        else:
            print(f"wrong channel, user in {channel.name}") #logging
            await context.send('Please only use this command in the correct channel')
            mine.reset_cooldown(context)
            return
        if random.randint(0,4) == 0:
            try: #tries to find their multiplyer
                BCmultiplyer = int(scores["multiplyers"][name])
            except KeyError as ename: #if they do not have a multiplyer, set one
                scores["multiplyers"][str(name)] = "1"
                BCmultiplyer = 1
            try: #assignes 1 brewcoin UNLESS the user has none to begin with
                Iscores = int(scores["scores"][name])
                Iscores += (1 * BCmultiplyer)
                scores["scores"][name] = str(Iscores)
            except KeyError as ename: #if the user has no brewcoins, they will get 1
                print(f'A stamblade assigned the value {BCmultiplyer*1} to {context.author.name}.')
                scores["scores"][str(name)] = str(BCmultiplyer*1)
                Iscores = BCmultiplyer*1
            with open('brewscores.ini', 'w') as confs: #writes to file
                scores.write(confs)
                print("stamplar")
            if BCmultiplyer == 1: #message for no multiplyer
                await context.send(f'You got a brewcoin!! You now have {Iscores}')
            else: #message if they have a multiplyer
                await context.send(f'You got {1*BCmultiplyer} brewcoins because of your {"{multiplyer name}"}!! You now have {Iscores}')
        else:
            try:
              cs = TheColoursOfTheRainbow()
              balEmbed = discord.Embed(title="No", description='You did not get brewcoin', color=discord.Color.from_rgb(*cs))
              balEmbed.set_image(url = "https://thetechrobo.github.io/youtried.png")
              balEmbed.set_footer(text="no brew coin for you")
              await context.send(embed = balEmbed)
            except Exception as ename:
                await context.send(str(ename))

    @commands.cooldown(1,4,commands.BucketType.guild)
    @commands.command(name='bal')
    async def bal(self, context, user=None):
        """
        Check your balance!
        """
        name = context.author.name + "#" + context.author.discriminator
        name = name.lower()
        scores.read("brewscores.ini")
        if user is None:
            try:
                Iscores = int(scores["scores"][name])
            except KeyError:
                Iscores = 0
            colours = TheColoursOfTheRainbow()
            balEmbed = discord.Embed(title="Balance", description=f'{context.author.mention}\'s current balance is {Iscores} brewcoins!', color=discord.Color.from_rgb(*colours))
            await context.send(embed = balEmbed)
        else:
            await context.send('Sorry, but specifying a user is not yet supported. Try again soon!')

    @commands.command(name='mult', aliases=("multiplier",))
    async def multiplyer(self, context):
        print('stamplar')
        """
        Check your BrewCoin multiplyer
        """
        name = context.author.name + "#" + context.author.discriminator
        name = name.lower()
        print('magplar')
        scores.read("brewscores.ini")
        try:
            multiplyerBal = int(scores["multiplyers"][name])
            print('stamdk')
        except KeyError:
            multiplyerBal = 1
        colours = TheColoursOfTheRainbow()
        multEmbed = discord.Embed(title="Multiplyer", description=f'{context.author.mention} \nYour multipluer is {multiplyerBal} \nIt will last for {"{multiplyerTime}"}', color=discord.Color.from_rgb(*colours))
        await context.send(embed = multEmbed)

    @commands.command(name='top')
    async def top(self, context):
        scores.read("brewscores.ini")
        tops = scores['scores']
        print('hi\n', tops)
        print('sotred')
        colours = TheColoursOfTheRainbow()
        a = sorted(tops, key=lambda k: int(tops[k]), reverse=True)
        string = """"""
        await context.send("Loading balancers...")
        for item in a:
            print(item)
            g = item
            string += (f"{g}: {tops[g]}\n")
        em = discord.Embed(title="Top 5 Balancers", description=f'The top 5 contestants are!:\n{string}', color=discord.Color.from_rgb(*colours))
        await context.send(embed=em)

    @commands.command(name="shop")
    async def shop(self, context):
        shopItems = StoreItemsVar
        print(shopItems)
        q = 0
        string = ""
        colours = TheColoursOfTheRainbow()
        em = discord.Embed(title="Shop", description=f'The items availible at the shop are:\n', color=discord.Color.from_rgb(*colours))
        for i in shopItems:
            price = shopItems[list(shopItems)[q]]
            item = list(shopItems)[q]
            em.add_field(name = item, value= price, inline = False)
            #string += f"**{q+1}.** {item} \t\t--> {price} Brewcoins.\n"
            q += 1
        #em = discord.Embed(title="Shop", description=f'The items availible at the shop are:\n{string}', color=discord.Color.from_rgb(*colours))
        await context.send(embed=em)

    @commands.command(name="daily") #wow this is a big one...
    async def daily(self, context):
        try:
            nowDate = datetime.datetime.now() #nowdate is the date right now
            nowDate = nowDate.strftime("%Y%m%d") #formats nowDate into proper date
            name = context.author.name + "#" + context.author.discriminator
            name = name.lower() #lowercases the name
            scores.read("brewscores.ini")

            #<<<MULTIPLYER>>>
            try: #tries to find their multiplyer
                print('stamden')
                BCmultiplyer = int(scores["multiplyers"][name])
                print('stamcro')
            except KeyError as ename: #if they do not have a multiplyer, set one
                print('stamsorc')
                scores["multiplyers"][str(name)] = "1"
                BCmultiplyer = 1
                print('stamblade')
            #<<<MULTIPLYER>>>

            #<<<GETS DATE>>>
            try: #tries to find their last date
                dailyDate = scores["daily"][name] #gets what their last sent date was
                print(f'Last daily was claimed on {dailyDate}')
            except KeyError as ename:
                print('magsorc')
                scores["daily"][str(name)] = str(nowDate) #saves the current date as their date
                dailyDate = scores["daily"][name] #Then defines daily date
                dailyDate -= 1 #removes 1 from it so that it is a different date from today
                print('magDK')
            #<<<GETS DATE>>>

            #<<<Actually gives them the brewcoins if they are deserving :evillaugh:>>>
            if dailyDate != nowDate: #if it is not the same date as their last daily claim
                dailyDate = scores["daily"][name]
                dailyRoll = random.randint(0, 20)
                Iscores = scores["scores"][name]
                try:
                    if dailyRoll in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) :
                        print("1 brewcoin for the magplar\n")
                        Iscores = int(Iscores) #sets Iscores as ints rather than strings
                        BCmultiplyer = int(BCmultiplyer)  #sets BCmultiplyer as int rather than string
                        Iscores = Iscores + (int(1) * BCmultiplyer)
                        await context.send(f"You got {1 * BCmultiplyer} brewcoin!!")
                    elif dailyRoll in (10, 11, 12, 13) :
                        print("2 brewcoin for the magplar\n")
                        Iscores = int(Iscores)
                        BCmultiplyer = int(BCmultiplyer)
                        Iscores += (2 * BCmultiplyer)
                        await context.send(f"You got {2 * BCmultiplyer} brewcoins!!")
                    elif dailyRoll == 14 :
                        print("3 brewcoin for the magplar\n")
                        Iscores = int(Iscores)
                        BCmultiplyer = int(BCmultiplyer)
                        Iscores += (3 * BCmultiplyer)
                        await context.send(f"You got {3 * BCmultiplyer} brewcoins!!")
                    elif dailyRoll in (15, 16, 17, 18, 19, 20):
                        print("0 brewcoin for the magplar\n")
                        Iscores = int(Iscores)
                        BCmultiplyer = int(BCmultiplyer)
                        Iscores += (0 * BCmultiplyer)
                        await context.send("You did not get any brewcoins... :cry:")
                    scores["scores"][name] = str(Iscores) #Adds their scores to the brewscores.ini
                    scores["daily"][name] = nowDate #Adds current date as last time daily was claimed
                except KeyError as ename: #if the user has no brewcoins, they will need to mine to get one
                    await context.send("You need to mine before claiming a daily...\nPlease use the command `brew mine` before you claim a daily.")
                with open('brewscores.ini', 'w') as confs: #writes to file
                    scores.write(confs)
                    print("stamplar")
            else:
                await context.send("You have already claimed your daily today.")
            #<<<Done giving them brewcoins (or not)>>>
        except Exception as ename: #if it errors out
            print(f'ERROR: < {ename} >')
            await context.send('There was an unexpected error. It\'s not you, it\'s us.')
def setup(bot):
    bot.add_cog(brewcoinCog(bot))
