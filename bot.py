import discord
import time
import random
import json
from dotenv import load_dotenv
import os
import re

env = load_dotenv("./.env")
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in')


def match (syntax, msg):
    return re.search(f"\\b{syntax}\\s*[.,!?;]*$", msg, flags=re.IGNORECASE)


@client.event
async def on_message(message):

    # if message.author != client.user:
    mots = json.load(open('mots.json'))
    msg = message.content.split(' ')
    if message.content.startswith('!spam'):
        try:
            await message.delete()
            nbr = int(msg[1])
            txt = ' '.join(msg[2:])
            for i in range(nbr):
                await message.channel.send(txt)
                time.sleep(1)

        except Exception as e:
            await message.channel.send('Essais putôt: !spam nombre_de_fois texte')

    for mot in mots:
        for syntax in mot[0]:
            if match(syntax, message.content):
                await message.reply(random.choice(mot[1]), mention_author=True)

client.run(token)
