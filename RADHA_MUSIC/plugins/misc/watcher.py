from pyrogram import filters
from pyrogram.types import Message

from RADHA_MUSIC import app
from RADHA_MUSIC.core.call import RADHA

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await RADHA.stop_stream_force(message.chat.id)
