import discord
from discord.ext import commands
import configparser
import random
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

    #@commands.event
#    async def on_command_error(self, ctx, error):
    #    """
    #    Does some stuff in case of cooldown error.
    #    """
    #    if isinstance(error, commands.CommandOnCooldown):
    #        potentialMessages = [f'This command is on cooldown, please wait {int(error.retry_after)}s.', f'Searching for more coins to excavate... ({int(error.retry_after)}s)', f'The GPU overheated. Hopefully it did not die, or you may have a hard time finding a new one... {int(error.retry_after)}s.', f'You should not be greedy and mine too many brewcoins... Please try again in {int(error.retry_after)}s.', f'The drill is overheated. You cannot brewcoin yet. Please wait {int(error.retry_after)}s.', f'Bad things may happen if you do not wait {int(error.retry_after)} more seconds before mining again... :ghost:']
    #        await ctx.send(random.choice(potentialMessages))
    #        await ctx.send(bot.command())
    #        raise error

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

    @commands.command(name='mult')
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
        for i in shopItems:
            try:
                q = 0
                await context.send(i)
                await context.send(shopItems[1])
                q = q + 1
            except BaseException as ename:
                await context.send(f"ERROR: {ename}")
def setup(bot):
    bot.add_cog(brewcoinCog(bot))
