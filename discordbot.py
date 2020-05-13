# bot.py
import os
import re
import requests
import discord
from dotenv import load_dotenv
from json import JSONDecodeError

url = "https://cat-fact.herokuapp.com/facts/random"

args = ['']*10
# Set default args
args[1] = 1
fact = ''
i = 0

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


def getFacts(animal, amount):
    response = requests.get(url = url, params = {'animal_type': animal, 'amount': amount})
    try:
        return response.json()
    except JSONDecodeError:
        return {'text': 'Sorry, I couldn\'t find any '+ animal +' facts for you.'}



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.content = message.content.lower()
    
    if "i like " in message.content:
        other = message.content.split("i like ", 1)
        other = other[1].split(" ", 1)

        if other[0][-1] == 's':
            other[0] = other[0][:-1]

        fact = getFacts(other[0], 1)
        await message.channel.send(fact['text'])
        return

    args = ['']*10
    args[1] = 1
    args[0:1] = message.content.split(' ');

    if args[0] == "meow":

        fact = getFacts("cat", args[1])

        if int(args[1]) == 1:
            await message.channel.send(fact['text'])
            return

        for i in range(int(args[1])):
            await message.channel.send(fact[i]['text'])
            return

    if args[0] == 'woof':

        fact = getFacts("dog", args[1])

        if int(args[1]) == 1:
            await message.channel.send(fact['text'])
            return

        for i in range(int(args[1])):
            await message.channel.send(fact[i]['text'])
            return

    if "bruh" in message.content:

        await message.channel.send("\\*bruh sound effect\\*")
        return

client.run(TOKEN)
