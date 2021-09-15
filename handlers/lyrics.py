#Ur motherfucker If U Kang And Don't Give Creadits

import requests
from config import BOT_USERNAME
from pyrogram import Client
from helpers.filters import command


@Client.on_message(command(["lyrics", f"lyric"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**Wft???**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("🔎 **Searching Lyrics**")
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("**Lyrics not foundn.** Try searching with a clearer song title")
