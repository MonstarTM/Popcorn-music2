from pyrogram import Client, filters
from pyrogram.types import Message
from utils import mp, RADIO, USERNAME
from config2 import Config
from config2 import STREAM

@Client.on_message(filters.command(["radio", f"radio@{USERNAME}"]))
async def radio(client, message: Message):
    if 1 in RADIO:
        k=await message.reply_text("Kindly stop existing Radio Stream /stopradio")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.start_radio()
    k=await message.reply_text(f"Started Radio: <code>{STREAM}</code>")
    await mp.delete(k)
    await mp.delete(message)

@Client.on_message(filters.command(['stopradio', f"stopradio@{USERNAME}"]))
async def stop(_, message: Message):
    if 0 in RADIO:
        k=await message.reply_text("Kindly start Radio First /radio")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.stop_radio()
    k=await message.reply_text("Radio stream ended.")
    await mp.delete(k)
    await mp.delete(message)
