#example
#1.0.0
#SQUID-SQUID LLC
#Example of module.
from pyrogram import filters

@app.on_message(filters.command("example", prefixes="#") & filters.me)
async def ping_cmd(_, message):
    await message.reply("It works!")
