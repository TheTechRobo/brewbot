import discord, json, random, logging, datetime, datetime
from discord.ext import commands
from store_data import *
from miscfunc import *
from addBrewcoin import *


class brewcoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 45, commands.BucketType.guild)
    @commands.command(name="mine")
    async def mine(self, context):
        """
        Small chance of getting a brewcoin! 45 second cooldown.
        """
        channel = context.channel
        if channel.name != "brewbot":
            print(f"wrong channel, user in {channel.name}")
            await context.send("Please only use this command in the correct channel")
            self.mine.reset_cooldown(context)
            return
        if random.randint(0, 3) == 0:
            user = context.author
            amount, userCoin, multiplyer = addbrewcoin(1, user)

            if multiplyer == 1:  # message for no multiplyer
                await context.send(f"You got a brewcoin!! You now have {userCoin}")
            else:  # message if they have a multiplyer
                await context.send(
                    f'You got {amount} brewcoins because of your {"{multiplyer name}"}!! You now have {userCoin}'
                )
        else:
            await context.send(
                embed=SetEmbed(
                    title="No",
                    description="You did not get brewcoin",
                    img="https://thetechrobo.github.io/youtried.png",
                    footer="no brew coin for you",
                )
            )

    @commands.cooldown(1, 4, commands.BucketType.guild)
    @commands.command(name="bal")
    async def bal(self, context, user: discord.Member = None):
        """
        Check your balance!
        """
        if user is None:
            user = context.author
        name = user.id
        with open("scores.json") as file:
            scores = json.load(file)
        try:
            scores["config"][name]["ShowBal"]
        except KeyError:
            scores["config"][name] = {
                "ShowBal": True
            }  # won't be saved but that's fine, since this is just a default setting
        if scores["config"][name]["ShowBal"] or user == context.author:
            try:
                print(name)
                Iscores = scores["scores"][str(name)]
            except KeyError:
                Iscores = 0
            colours = TheColoursOfTheRainbow()
            balEmbed = discord.Embed(
                title="Balance",
                description=f"{user.mention}'s current balance is {Iscores} brewcoins!",
                color=discord.Color.from_rgb(*colours),
            )
            await context.send(embed=balEmbed)
        else:
            await context.send(
                embed=SetEmbed(
                    title="403 Forbidden",
                    description="This user has disabled API access. You cannot view their balance.",
                    footer="Want your API access to be disabled? Contact TheTechRobo or TheRuntingMuumuu! Configuration tool coming soon™",
                )
            )

    @commands.command(name="mult", aliases=("multiplyer",))
    async def multiplyer(self, context):
        """
        Check your BrewCoin multiplyer.
        """
        name = context.author.id
        data = scores.json()
        data.read()
        try:
            multiplyerBal = float(data.scores["multiplyers"][name])
            multiplyerTime = int(data.scores["multiplyerTime"][name])
        except KeyError:
            multiplyerBal = 1
        colours = TheColoursOfTheRainbow()
        multEmbed = discord.Embed(
            title="Multiplyer",
            description=f"{context.author.mention} \nYour multiplyer is {multiplyerBal} \nIt will last until {datetime.datetime.fromtimestamp(multiplyerTime)}",
            color=discord.Color.from_rgb(*colours),
        )
        await context.send(embed=multEmbed)

    @commands.command(name="top")
    async def top(self, context):
        s = scores.json()
        s.read()
        scoress = s.scores
        tops = scoress["scores"]
        print("hi\n", tops)
        print("\tsotred")
        a = sorted(tops, key=lambda k: int(tops[k]), reverse=True)
        string = ""
        load = await context.send("Loading balancers...")
        pos = 1
        for item in a:
            if pos > 5:
                break
            ga = item
            try:
                g = s.lookUpById(ga)
            except KeyError:
                continue
            try:
                scoress["config"][g]["ShowBal"]
            except KeyError:
                scoress["config"][g] = {
                    "ShowBal": True
                }  # default value; not saved to the file
            if not scoress["config"][g]["ShowBal"]:
                continue
            print(item)
            string += f"{pos}. **{g}**: {tops[ga]}\n"
            pos += 1
        await load.edit(
            embed=SetEmbed(
                title=f"Top {pos - 1} Balancers",
                description=f"The top {pos - 1} contestants are!:\n{string}",
                footer=random.choice(
                    (
                        "Powered by TheTechRobo, not hanks to TheRuntingMuumuu",
                        "balance on my head",
                        "Rats are better than people. **Change my mind.**",
                    )
                ),
            )
        )

    @commands.command(name="shop")
    async def shop(self, context):
        print(StoreItems)
        q = 0
        colours = TheColoursOfTheRainbow()
        em = discord.Embed(
            title="Shop",
            description=f"The items availible at the shop are:\n",
            color=discord.Color.from_rgb(*colours),
        )
        for i in StoreItems:
            price = i.price
            name = i.name
            # item = list(shopItems)[q]
            em.add_field(name=name, value=price, inline=False)
            q += 1
        await context.send(embed=em)

    @commands.command(name="buy")
    async def purchase(self, ctx, item):
        print(item)
        for (
            i
        ) in (
            StoreItems
        ):  # im sure there's a better way to do this but im too lazy to implement one
            if i.name == item:
                status = await ctx.send("Purchasing Item...")
                data = scores.json()  # TODO: switch to remBrewcoin
                data.read()
                data.scores["scores"][ctx.author.id] -= i.price
                await status.edit(content="Subtracted coins. Running command...")
                i.run(ctx.author.id)
                await status.delete()

    @commands.command(name="daily")  # wow this is a big one...
    async def daily(self, context):
        try:
            nowDate = datetime.datetime.now().strftime(
                "%Y%m%d"
            )  # nowdate is the date right now
            name = str(context.author.id)
            namea = context.author
            with open("scores.json") as file:
                scores = json.load(file)

            # <<<GETS DATE>>>
            try:  # tries to find their last date
                dailyDate = scores["daily"][name]  # gets what their last sent date was
                print(f"Last daily was claimed on {dailyDate}")
            except KeyError as ename:
                scores["daily"][str(name)] = str(
                    nowDate
                )  # saves the current date as their date
                dailyDate = scores["daily"][name]  # Then defines daily date
                dailyDate = str(
                    int(dailyDate) - 1
                )  # removes 1 from it so that it is a different date from today
            # <<<GETS DATE>>>

            # <<<Actually gives them the brewcoins if they are deserving :smiling_imp:>>>
            if (
                dailyDate != nowDate
            ):  # if it is not the same date as their last daily claim
                dailyRoll = random.randint(0, 20)  # Iscores = scores["scores"][name]
                if dailyRoll in (0, 1, 2, 4, 5, 6, 7, 8, 9):
                    amount = addbrewcoin(1, namea)
                    await context.send(f"You got {amount[0]} brewcoin!!")
                elif dailyRoll in (3, 10, 11, 12, 13):
                    amount = addbrewcoin(2, namea)
                    await context.send(f"You got {amount[0]} brewcoins!!")
                elif dailyRoll == 14:
                    amount = addbrewcoin(3, namea)
                    await context.send(f"You got {amount[0]} brewcoins!!")
                else:
                    amount = [0]
                    await context.send("You did not get any brewcoins... :cry:")
                print(f"{amount[0]} brewcoin for the magplar\n")
                with open("scores.json") as file:
                    scores = json.load(file)
                scores["daily"][
                    name
                ] = nowDate  # Adds current date as last time daily was claimed
                with open("scores.json", "w") as confs:  # writes to file
                    confs.write(json.dumps(scores, indent=4))
            else:
                last_date = scores["daily"]["serverwide"]
                if last_date != nowDate and int(last_date) + 1 != nowDate:
                    amount = addbrewcoin(5, namea)
                    with open("scores.json") as file:
                        scores = json.load(file)
                    scores["daily"]["serverwide"] = nowDate
                    with open("scores.json", "w") as confs:  # writes to file
                        confs.write(json.dumps(scores, indent=4))
                    await context.send(
                        f"{context.author.mention} you just got a bunch of brewcoins by claiming the serverwide 48h daily thing!!"
                    )
                else:
                    await context.send(
                        "You have already claimed your daily today.\nThe serverwide daily has been claimed within the last 48 hours."
                    )
            # <<<Done giving them brewcoins (or not)>>>
        except Exception as ename:  # if it errors out
            # print(f'ERROR: < {ename} >')
            # await context.send(f'There was an unexpected error. It\'s not you, it\'s us. \nPlease contact @TheRuntingMuumuu or @TheTechRobo with this information : <<{ename}>>')
            raise

    @commands.command(name="give")
    async def give(self, ctx, user: discord.Member, amount: float):
        msg = await ctx.send(
            "REMOVING BREWCOIN... If this message doesn't go away, CONTACT @TheRuntingMuumuu and @TheTechRobo to get your coins back!"
        )
        try:
            if ctx.author == user:
                rembrewcoin(
                    user=(ctx.author.name + "#" + ctx.author.discriminator), amount=0.1
                )
                raise NiceTry(
                    f"As you hand the money to {ctx.author.mention}, you realise that you are handing it to yourself.\nIn shock, You accidentally drop 0.1 brewcoin!"
                )
            rembrewcoin(user=ctx.author, amount=amount)
        except NiceTry as ename:
            await ctx.send(ename)
            rembrewcoin(user=(ctx.author), amount=1)
            addbrewcoin(user=user, amount=1)
            await msg.delete()
            raise
        await msg.delete()
        msg = await ctx.send(
            "ADDING BREWCOIN... If this message doesn't go away, CONTACT @TheRuntingMuumuu and @TheTechRobo to get your coins back!"
        )
        addbrewcoin(user=user, amount=amount)
        await msg.delete()
        await ctx.send(
            f"{user.mention}: You just got {amount} brewcoins from {ctx.author.mention}.\n{ctx.author.mention}: :thumbsup: All transactions should be received."
        )

    @mine.error
    async def on_command_error(self, ctx, error):
        """
        Does some stuff in case of cooldown error.
        """
        if isinstance(error, commands.CommandOnCooldown):
            potentialMessages = [
                f"This command is on cooldown, please wait {int(error.retry_after)}s.",
                f"Searching for more coins to exvate... ({int(error.retry_after)}s)",
                f"The GPU overheated. Hopefully it did not die, or you may have a hard time finding a new one. {int(error.retry_after)}s.",
                f"You should not be greedy and mine too many brewcoins... Please try again in {int(error.retry_after )}s.",
                f"The drill is overheated. You cannot brewcoin yet. Please wait {int(error.retry_after)}s.",
                f"Bad things may happen if you do not wait {int(error.retry_after)} more seconds before mining again... :ghost:",
            ]
            await ctx.send(random.choice(potentialMessages))
            print("\nAn anonymous magcro tried to do a command that was on cooldown")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(brewcoinCog(bot))
