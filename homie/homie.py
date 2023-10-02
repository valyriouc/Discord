from typing import Any
from discord.flags import Intents 
import discord
import socket

import sys
sys.path.append("C:\\Hackerspace\\Source\\Discord\\")

import common.bots as bots
import common.credentials as creds

class HomieBot(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents()
        intents.dm_messages = True
        intents.message_content = True
        intents.guild_messages = True
        intents.message_content = True
        intents.members = True

        super().__init__(intents=intents)

    async def on_ready(self):
        print(f"Homie is now running")
    

# TODO: Use class approach
def run_discord_bot():
    info = creds.Credentials.get(
        "../auths.txt",
        bots.Bot.homie)
    
    # TOKEN = info["Token"]

    # intents = discord.Intents()
    # intents.dm_messages = True
    # intents.message_content = True
    # intents.guild_messages = True
    # intents.message_content = True
    # intents.members = True

    # client = discord.Client(intents=intents)
    
    # @client.event
    # async def on_message(message):
    #     if message.auther == client.user:
    #         return
    
    bot = HomieBot()
    bot.run(info["Token"])