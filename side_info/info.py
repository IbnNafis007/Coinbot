from random import randint
import datetime
import discord


# event = "!event {If following page : 1,2,3,etc} : Display the next events\n\n"


class Info:
    def __init__(self, auth):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        return

    def info(self):
        all = "!all [coins(s)] : Request on all Exchanges\n"
        btc = "!btc : Request on BTC price\n"
        rex = "!rex [coin(s)] : Request on Bittrex\n"
        finex = "!finex [coin(s)] : Request on Bitfinex\n"
        polo = "!polo [coin(s)] : Request on Poloniex\n"
        topia = "!topia [coin(s)] : Request on Cryptopia\n"
        binance = "!binance [coin(s)] : Request on Binance\n\n"
        top = "!top : Request about the best/worst tendancies\n"
        cmc = "!cmc : Request on the MarketCap\n"
        order = "!order [price][win][lose] : To estimate your possible wins/losses\n"
        whale = "!whale [Coin]{Limit in BTC} : Retrieve the big orders\n\n"
        info = "!infos : Know all the bot commands\n"
        conv = "!conv [coin][number of coins] : To know the coin's price in BTC/USD\n"
        name = "!name [coin] : Request about the Coin itself and some side infos\n"
        sum = "!sum [url] : shorten an article on a website. (The result may be unclear, sorry :( )\n\n"
        stats = "!stats [Coin OR Command] : Retrieve the stats of a coin/command\n"
        list = "!db info : Retrieve data about the commands used on the server\n\n"
        code = "!code : Display the url of the GitHub repository used for this bot\n"
        money = "!money : If you want to donate cryptos to Abolah, the creator of this bot\n"

        data_info = "```css\n" + all + btc + rex + finex + polo + topia + binance + top + cmc + order + whale + info + conv + name + sum + stats + list + code + money + "```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="")
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":hammer: Version", value="1.5.1")
        embed.add_field(name=":star2: Request about Coinbot's commands",
                        value="Here are the informations I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":information_source: Informations about Coinbot", value=data_info)
        return embed
