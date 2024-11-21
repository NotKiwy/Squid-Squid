# ping
# 1.0.0
# SQUID-SQUID LLC
# Simple ping module. Created by SQUID-SQUID LLC.
from pyrogram import Client, filters
import time
import asyncio


async def loading(message):
    frames = ["◾◽◽◽", "◽◾◽◽", "◽◽◾◽", "◽◽◽◾", "◽◽◾◽", "◽◾◽◽"]
    for frame in frames:
        await message.edit(f"◾ `Loading... {frame}`")
        await asyncio.sleep(0.2)


@Client.on_message(filters.command("ping", prefixes="#") & filters.me)
async def ping(client, message):
    start = time.time()
    await loading(message)
    end = time.time()
    ping = round((end - start) * 1000, 2)
    await message.edit(f"◾ `Ping: {ping}ms`")
