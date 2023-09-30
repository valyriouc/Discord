import discord
import responses
import socket 

def get_info():
    info = {}
    with open("../auths.txt", "r") as fobj:
        for line in fobj.readlines():
            print(line)
            res = line.split(":")
        
            key = res[0].strip()
            value = res[1].strip()

            info[key] = value
    return info 

async def send_message(message, user_message, is_private):
    try: 
        response = responses.handle_request(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    info = get_info()

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
