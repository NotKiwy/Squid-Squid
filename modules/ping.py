#ping
#1.2.0
from pyrogram import Client, filters
import time
import asyncio

async def loading(message):
    frames = ["◾◽◽◽", "◽◾◽◽", "◽◽◾◽", "◽◽◽◾", "◽◽◾◽", "◽◾◽◽"]
    for frame in frames:
        await message.reply(f"◾ `Loading... {frame}`")
        await asyncio.sleep(0.2)

@app.on_message(filters.me)
async def ping(_, message):
    if message.text == "#ping":
        start = time.time()
        msg = await message.reply("Starting ping test...")
        await loading(msg)
        end = time.time()
        ping = round((end - start) * 1000, 2)
        await msg.edit(f"◾ `Ping: {ping}ms`")
