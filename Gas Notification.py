from web3 import Web3
import asyncio
from aiogram import Bot


#Enter Blockchain Node RPC
rpc=""

#Enter Your Bot Token
bot_token=""

#Enter Your Chat Id
chat_id=""

bot = Bot(token=bot_token)

async def send_telegram_message(text):
    await bot.send_message(chat_id=chat_id, text=text)


#Establish Connection with Blockchain
w3=Web3(Web3.HTTPProvider(rpc))

if not w3.is_connected():
    print('Not Connected')
else:
    print('Connected')

#Condition
while True:
    gas=w3.from_wei(w3.eth.gas_price,'gwei')

    #Customize target gas fee as preference
    if gas<=1:
        asyncio.run(send_telegram_message(f"Low Gas Fee!!! Current Gas fee is {gas} gwei"))
        break