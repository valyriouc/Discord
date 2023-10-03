from typing import Any
from discord.flags import Intents 
import discord
import socket

import sys
sys.path.append("C:\\Hackerspace\\Source\\Discord\\")

import common.bots as bots
import common.credentials as creds

import testing.testDataProvider as tdata
import dataProvider as dp 

class HomieBot(discord.Client):
    def __init__(self, dataProvider: dp.DataProvider) -> None:
        intents = discord.Intents()
        intents.dm_messages = True
        intents.message_content = True
        intents.guild_messages = True
        intents.message_content = True
        intents.members = True

        super().__init__(intents=intents)

        self.dataProvider = dataProvider

    async def on_ready(self):
        print(f"Homie is now running")
    
    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        if not message.content.startswith("!"):
            return 
        print(message.content)
        data = self.__parse_message(message.content)  
        output = self.dataProvider.request_data(data)
        await message.reply(output)
    
    def __parse_message(self, message: str):
        data = {}
        parts = message.split(",")
        for it in range(0, len(parts)):
            keyword = parts[it].replace("!", "")
            data[keyword] = ""
        return data
    
info = creds.Credentials.get(
        "../auths.txt",
        bots.Bot.homie)
    
def run_testing_bot():
    print("Running into testing")
    bot = HomieBot(tdata.TestDataProvider())
    bot.run(info["Token"])

def run_discord_bot():
    # smarthome data provider  
    bot = HomieBot()
    bot.run(info["Token"])