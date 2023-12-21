import asyncio
from pyrogram import Client

api_id = 18349141
api_hash = 'fa3a10f79ac5765fa9cd9a977a1923d3'

# 0123456789abcdef0123456789abcdef
# '6752471241:AAG2xMRFjT1oQQfyfSq4gjhIvOVl22zv8hs'


async def main():
    async with Client("mySession", api_id, api_hash) as app:
        await app.send_message(5884447415, "Greetings from **Pyrogram**!")


asyncio.run(main())