import discord
import requests
import random
from config import BOTTOKEN



client = discord.Client()
c = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!tip'):
        TIPS = requests.get("https://raw.githubusercontent.com/Soldier101/Soldier101-Station/master/strings/tips.txt").text.split("\n")
        msgtip = random.choice(TIPS)
        await  client.send_message(message.channel, msgtip)
    if message.content.startswith('!goontip'):
        GOONTIPS = requests.get("https://raw.githubusercontent.com/goonstation/goonstation-2016/master/strings/roundstart_hints.txt").text.split("\n")
        msgtip = random.choice(GOONTIPS)
        await  client.send_message(message.channel, msgtip)
    if message.content.startswith('!goontips'):
        GOONTIPS = requests.get("https://raw.githubusercontent.com/goonstation/goonstation-2016/master/strings/roundstart_hints.txt").text.split("\n")
        msgtip = random.choice(GOONTIPS)
        await  client.send_message(message.channel, msgtip)


    if message.content.startswith('!die'):
        msgdie = '{0.author.mention} seizes up and falls limp, his eyes dead and lifeless. '.format(message)
        await client.send_message(message.channel, msgdie)
    if message.content.startswith('!suicide'):
        msgdie = '{0.author.mention} seizes up and falls limp, his eyes dead and lifeless. '.format(message)
        await client.send_message(message.channel, msgdie)
@client.event
async def on_ready():
    print('Signed in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(BOTTOKEN)
