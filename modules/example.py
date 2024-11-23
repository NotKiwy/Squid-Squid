#example
#1.0.0

from pyrogram import filters

@app.on_message(filters.command("example", prefixes="#") & filters.me)
async def example_cmd(_, message):
    await message.edit_text("**Hey there!**")
