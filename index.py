import discord

from dotenv import load_dotenv
load_dotenv()

import os
token = os.environ.get("token")
cat = os.environ.get("cat_api")

import requests

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as", self.user)

    async def on_message(self, message):
        if "poes" in message.content:
            data = requests.get('https://api.thecatapi.com/v1/images/search?breed_ids=beng&include_breeds=true?size=small', headers={"X-API-KEY": cat}).json()
            await message.channel.send(data[0]["url"])
client = MyClient()
client.run(token)