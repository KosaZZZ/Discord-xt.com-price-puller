from discord import *
from requests import get
import asyncio

API_request = 'https://api.xt.com/data/api/v1/getTicker?market={pair}'.format(pair="hdd_usdt")
client = Client()

def GetPrice():
    XT_response = get(API_request).json()
    XT_response_data = XT_response['price']
    return str(XT_response_data) + " USDT"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.loop.create_task(status_update())


async def status_update():
    while True:
        price = GetPrice()

        await client.get_guild(921889338277650452).me.edit(nick=price) # Put Guild_id here
        print("Price Updated")
        await asyncio.sleep(5)


client.run('') # Put Bot Token here





