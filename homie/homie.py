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
        data = None
        try:
            data = self.__parse_message(message.content)  
        except ValueError as e:
            await message.reply(e)

        if not data["success"]:
            await message.reply(data["error"])
            return

        # Validate commands if they exists and have the necessary properties 
        output = self.dataProvider.request_data(data["commands"])
        await message.reply(output)
    
    def __parse_message(self, message: str) -> object:
        data = {
            "success": True,
            "error": "",
            "commands": []
        }
        readWithContent = False
        parts = message.split(",")
        for it in range(0, len(parts)):
            command = parts[it].replace("!", "").strip()
            commandDesc = None
            if readWithContent:
                data["success"] = False
                data["error"] = "Only one command is allowed when this command has content"
            if ":" in command:
                # parse a command with content
                commandDesc = HomieBot.__parse_with_content(command)
                readWithContent = True
                pass
            else:
                # parse command without content 
                commandDesc = HomieBot.__parse_without_content(command)
                pass 
            data["commands"].append(commandDesc)
        return data
    

    @staticmethod
    def __parse_with_content(command: str) -> object:
        comm = {
            "identifier": "",
            "content": "",
            "hasContent": True
        }
        commandParts = command.split(":")
        if (len(commandParts) != 2):
            raise ValueError("Malformed command detected")
        # Normilize input
        for it in range(0, 2):
            commandParts[it] = commandParts[it].strip()
        if (commandParts[1] == ""):
            raise ValueError("Expected content but got empty string")
        comm["identifier"] = commandParts[0]
        comm["content"] = commandParts[1]
        return comm
    
    @staticmethod 
    def __parse_without_content(command: str) -> object:
        comm = {
            "identifier": "",
            "content": "",
            "hasContent": False
        }
        comm["identifier"] = command
        return comm

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