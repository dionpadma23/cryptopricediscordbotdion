import discord
import requests


#DISCORD REUQIREMENTS (DO NOT CHANGE OR DELETE)
TOKEN = "ODM2MjQzNjg5NjA4OTcwMjUy.YIbKoA.Vj0i4-e-k6YsM8Pw_uqLxlbhOu4"

client = discord.Client()

@client.event
async def on_message(message):
    #Making The Bot Decline it Self
    if message.author == client.user:
        return

    if message.content.startswith('$price'):
        msg1 = message.content [6:15]
        msg1 = msg1.replace(' ','')
        if msg1 == "BTC":
            NUMBAH = 0
        elif msg1 == "ETH":
            NUMBAH = 1
        elif msg1 == "BNB" :
            NUMBAH = 2
        elif msg1 == "XRP" :
            NUMBAH = 3
        elif msg1 == "USDT" :
            NUMBAH = 4
        elif msg1 == "TKO" :
            NUMBAH = 243
        #API REQUIREMENT PRICE
        api_key = "958aba05-0035-4e1e-850e-e5f78d5d431c"
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key
        }
        symbols = "BTC","IDR"


        # make a request to the coinmarketcap api
        response = requests.get(url, headers=headers)
        response_json = response.json()


        # extract the bitcoin price from the json data
        btc_price = response_json['data'][NUMBAH]
        sorted = btc_price['quote']['USD']['price']
        sortedprice = round(sorted, 2)
        msg = 'Currently ' + msg1 +' is at USD '+ str(sortedprice) .format(message)
        await message.channel.send(msg)

#DISCORD REUQIREMENTS (DO NOT CHANGE OR DELETE)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Crypto Prices to USD!"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
