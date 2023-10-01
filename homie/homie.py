import discord
import socket
import common.credentials as creds
import common.bots as bots

def run_discord_bot():
    info = creds.Credentials.get(
        "../auths.txt",
        bots.Bot.homie)
    
    TOKEN = info["Token"]

    intents = discord.Intents()
    intents.dm_messages = True
    intents.message_content = True
    intents.guild_messages = True
    intents.message_content = True
    intents.members = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")
    
    @client.event
    async def on_message(message):
        if message.auther == client.user:
            return
        
    client.run(TOKEN)