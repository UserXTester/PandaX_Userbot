from pyrogram import Client as Bot
from PandaX_Userbot import udB
from PandaX_Userbot.Panda.database import Var


bot = Bot(
    ":memory:",
    Var.API_ID,
    Var.API_HASH,
    bot_token=udB.get("BOT_TOKEN"),
    plugins=dict(root="MusicBot.modules"),
)
