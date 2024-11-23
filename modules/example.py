#example
#1.0.0
from pyrogram import filters

@app.on_message(filters.me)
async def example_cmd(_, message):
    if message.text == "#example":
        await message.edit("It works!")
