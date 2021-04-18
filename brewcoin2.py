import discord, configparser, random, logging, datetime
from discord.ext import commands
from store_data import *
from miscfunc import *

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
        if channel.name != 'brewbot':
            print(f"wrong channel, user in {channel.name}") #logging
            await context.send('Please only use this command in the correct channel')
            mine.reset_cooldown(context)
            return
        if random.randint(0,3) == 0:
            try: #tries to find their multiplyer
                BCmultiplyer = int(scores["multiplyers"][name])
            except KeyError as ename: #if they do not have a multiplyer, set one
                scores["multiplyers"][str(name)] = "1"
                BCmultiplyer = 1
            try: #assigns 1 brewcoin UNLESS the user has none to begin with
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
                scores["scores"][name]
            except KeyError:
                scores["scores"][name] = "0"
            try:
                await context.send(embed=SetEmbed(title="No", description="You did not get brewcoin", img="https://thetechrobo.github.io/youtried.png", footer="no brew coin for you"))
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
        """
        Check your BrewCoin multiplyer
        """
        name = context.author.name + "#" + context.author.discriminator
        name = name.lower()
        scores.read("brewscores.ini")
        try:
            multiplyerBal = int(scores["multiplyers"][name])
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
        a = sorted(tops, key=lambda k: int(tops[k]), reverse=True)
        string = ""
        await context.send("Loading balancers...")
        pos = 1
        for item in a:
            if pos > 5:
                break
            print(item)
            g = item
            string += (f"{pos}. **{g}**: {tops[g]}\n")
            pos += 1
        await context.send(embed=SetEmbed(title=f"Top {pos - 1} Balancers", description=f'The top {pos - 1} contestants are!:\n{string}', footer=random.choice(("Powered by TheTechRobo, not hanks to TheRuntingMuumuu", "balance on my head", "Rats are better than people. **Change my mind.**"))))

    @commands.command(name="shop")
    async def shop(self, context):
        shopItems = StoreItemsVar
        print(shopItems)
        q = 0
        colours = TheColoursOfTheRainbow()
        em = discord.Embed(title="Shop", description=f'The items availible at the shop are:\n', color=discord.Color.from_rgb(*colours))
        for i in shopItems:
            price = shopItems[list(shopItems)[q]]
            item = list(shopItems)[q]
            em.add_field(name = item, value= price, inline = False)
            q += 1
        await context.send(embed=em)

    @commands.command(name="daily") #wow this is a big one...
    async def daily(self, context):
        try:
            nowDate = datetime.datetime.now().strftime("%Y%m%d") #nowdate is the date right now
            name = context.author.name + "#" + context.author.discriminator
            name = name.lower() #lowercases the name
            scores.read("brewscores.ini") #reads the ini file into ram

            #<<<MULTIPLYER>>>
            try: #tries to find their multiplyer
                BCmultiplyer = int(scores["multiplyers"][name])
            except KeyError as ename: #if they do not have a multiplyer, set one
                scores["multiplyers"][str(name)] = "1"
                BCmultiplyer = 1
            #<<<MULTIPLYER>>>

            #<<<GETS DATE>>>
            try: #tries to find their last date
                dailyDate = scores["daily"][name] #gets what their last sent date was
                print(f'Last daily was claimed on {dailyDate}')
            except KeyError as ename:
                scores["daily"][str(name)] = str(nowDate) #saves the current date as their date
                dailyDate = scores["daily"][name] #Then defines daily date
                dailyDate = str(int(dailyDate) - 1) #removes 1 from it so that it is a different date from today
            #<<<GETS DATE>>>

            #<<<Actually gives them the brewcoins if they are deserving :smiling_imp:>>>
            if dailyDate != nowDate: #if it is not the same date as their last daily claim
                try:
                    dailyDate = scores["daily"][name]
                    Iscores = scores["scores"][name]
                except KeyError:
                    await context.send("You need to run `brew mine' before you claim a daily. This is a recording.")
                    scores["daily"][name] = "0"
                    return
                dailyRoll = random.randint(0, 20)#Iscores = scores["scores"][name]
                try: #todo: use floats instead of ints so that multiplyer 1.1, 0.9, etc work
                    Iscores = int(Iscores) #sets Iscores as ints rather than strings
                    BCmultiplyer = int(BCmultiplyer)
                    if dailyRoll in (0, 1, 2, 4, 5, 6, 7, 8, 9):
                        bc2Get = 1
                        await context.send(f"You got {1 * BCmultiplyer} brewcoin!!")
                    elif dailyRoll in (3, 10, 11, 12, 13) :
                        bc2Get = 2
                        await context.send(f"You got {2 * BCmultiplyer} brewcoins!!")
                    elif dailyRoll == 14 :
                        bc2Get = 3
                        await context.send(f"You got {3 * BCmultiplyer} brewcoins!!")
                    else:
                        bc2Get = 0
                        await context.send("You did not get any brewcoins... :cry:")
                    Iscores += (int(bc2Get) * BCmultiplyer)
                    print(f"{bc2Get} brewcoin for the magplar\n")
                    scores["scores"][name] = str(Iscores) #Adds their scores to the brewscores.ini
                    scores["daily"][name] = nowDate #Adds current date as last time daily was claimed
                except KeyError as ename: #if the user has no brewcoins, they will need to mine to get one
                    await context.send("You need to mine before claiming a daily...\nPlease use the command `brew mine' before you claim a daily.")
                with open('brewscores.ini', 'w') as confs: #writes to file
                    scores.write(confs)
            else:
                await context.send("You have already claimed your daily today.")
            #<<<Done giving them brewcoins (or not)>>>
        except Exception as ename: #if it errors out
            print(f'ERROR: < {ename} >')
            await context.send(f'There was an unexpected error. It\'s not you, it\'s us. ({ename})')
            raise
def setup(bot):
    bot.add_cog(brewcoinCog(bot))
