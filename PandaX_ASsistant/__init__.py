from telethon import Button, custom

from PandaX_Userbot import *
from PandaX_Userbot.Panda.database import Var
from PandaX_Userbot.functions.all import *
from PandaXBahasa import get_languages, get_string
from PandaX_Userbot.functions.asst_fns import *
from PandaX_Userbot.functions.botchat_db import *


OWNER_NAME = petercordpanda_bot.me.first_name
OWNER_ID = petercordpanda_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`terjadi kesalahan.`")


def get_back_button(name):
    button = [Button.inline("« ʙᴀᴄᴋ", data=f"{name}")]
    return button


