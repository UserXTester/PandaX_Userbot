import requests
from pyrogram import Client as Bot
from PandaX_Userbot.Panda.database import Var
from MusicBot.config import BG_IMAGE 
from MusicBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)
bot = Bot(
    ":memory:",
    Var.API_ID,
    Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    plugins=dict(root="MusicBot.modules"),
)

bot.start()
run()
