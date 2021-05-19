import discord, json, random, logging, datetime
from discord.ext import commands
from store_data import *
from miscfunc import *
from addBrewcoin import *

class brewcoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 45, commands.BucketType.guild)
    @commands.command(name = 'mine')
    async def mine(self, context):
        """
        Small chance of getting a brewcoin! 45 second cooldown.
        """
        channel = context.channel
        if channel.name != 'brewbot':
            print(f"wrong channel, user in {channel.name}")
            await context.send('Please only use this command in the correct channel')
            self.mine.reset_cooldown(context)
            return
        if random.randint(0,3) == 0:
            user = context.author.name + "#" + context.author.discriminator
            amount, userCoin, multiplyer = addbrewcoin(1, user)

            if multiplyer == 1: #message for no multiplyer
                await context.send(f'You got a brewcoin!! You now have {userCoin}')
            else: #message if they have a multiplyer
                await context.send(f'You got {amount} brewcoins because of your {"{multiplyer name}"}!! You now have {userCoin}')
        else:
            await context.send(embed=SetEmbed(title="No", description="You did not get brewcoin", img="https://thetechrobo.github.io/youtried.png", footer="no brew coin for you"))



    @commands.cooldown(1,4,commands.BucketType.guild)
    @commands.command(name='bal')
    async def bal(self, context, user=None):
        """
        Check your balance!
        """
        name = context.author.name + "#" + context.author.discriminator
        with open("scores.json") as file:
            scores = json.load(file)
        if user is None:
            try:
                Iscores = scores["scores"][name]
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
        with open("scores.json") as file:
            scores = json.load(file)
        tops = scores['scores']
        print('hi\n', tops)
        print('\tsotred')
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
            with open("scores.json") as file:
                scores = json.load(file)

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
                dailyRoll = random.randint(0, 20)#Iscores = scores["scores"][name]
                if dailyRoll in (0, 1, 2, 4, 5, 6, 7, 8, 9):
                    amount = addbrewcoin(1, name)
                    await context.send(f"You got {amount[0]} brewcoin!!")
                elif dailyRoll in (3, 10, 11, 12, 13) :
                    amount = addbrewcoin(2, name)
                    await context.send(f"You got {amount[0]} brewcoins!!")
                elif dailyRoll == 14 :
                    amount = addbrewcoin(3, name)
                    await context.send(f"You got {amount[0]} brewcoins!!")
                else:
                    amount = [0]
                    await context.send("You did not get any brewcoins... :cry:")
                print(f"{amount[0]} brewcoin for the magplar\n")
                with open("scores.json") as file:
                    scores = json.load(file)
                scores["daily"][name] = nowDate #Adds current date as last time daily was claimed
                with open('scores.json', 'w') as confs: #writes to file
                    confs.write(json.dumps(scores))
            else:
                await context.send("You have already claimed your daily today.")
            #<<<Done giving them brewcoins (or not)>>>
        except Exception as ename: #if it errors out
            print(f'ERROR: < {ename} >')
            await context.send(f'There was an unexpected error. It\'s not you, it\'s us. \nPlease contact @TheRuntingMuumuu or @TheTechRobo with this information : <<{ename}>>')
            raise

    @mine.error
    async def on_command_error(self, ctx, error):
        """
        Does some stuff in case of cooldown error.
        """
        if isinstance(error, commands.CommandOnCooldown):
            potentialMessages = [f'This command is on cooldown, please wait {int(error.retry_after)}s.', f'Searching for more coins to exvate... ({int(error.retry_after)}s)', f'The GPU overheated. Hopefully it did not die, or you may have a hard time finding a new one. {int(error.retry_after)}s.', f'You should not be greedy and mine too many brewcoins... Please try again in {int(error.retry_after )}s.', f'The drill is overheated. You cannot brewcoin yet. Please wait {int(error.retry_after)}s.', f'Bad things may happen if you do not wait {int(error.retry_after)} more seconds before mining again... :ghost:']
            await ctx.send(random.choice(potentialMessages))
            print('\nAn anonymous magcro tried to do a command that was on cooldown')
        else:
            raise(error)
def setup(bot):
    bot.add_cog(brewcoinCog(bot))
