from pyrogram import Client as Bot
from PandaX_Userbot import udB



bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="MusicBot.modules"),
)
