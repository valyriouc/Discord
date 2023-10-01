import discord
import socket 
import common.credentials as creds
import common.bots as bots 

def run_discord_bot():
    info = creds.Credentials.get(
        "../auths.txt", 
        bots.Bot.botter)

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
        print("Starting to run")

    @client.event
    async def on_message(message):
       if message.author == client.user:
           return
       
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
           sock.connect(("127.0.0.1", 4454))
           sock.sendall(message.content.encode())

    client.run(TOKEN);
