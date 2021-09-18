import asyncio
import time

from PandaX_Userbot import *
from PandaX_Userbot.Panda import *
from PandaX_Userbot.functions.all import *
from PandaX_Userbot.functions.sudos import *
from PandaX_Userbot.version import PandaX_version
from PandaX_Userbot.functions.nsfw_db import *
from PandaX_Userbot.functions.asstcmd_db import *
from PandaX_Userbot.functions.broadcast_db import *
from PandaX_Userbot.functions.gban_mute_db import *
from telethon import Button
from telethon.tl import functions, types
from PandaX_Userbot.utils import *
from strings import get_string


try:
    import glitch_me
except ModuleNotFoundError:
    os.system(
        "git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me"
    )

try:
    os.system(
        "git clone https://github.com/ilhammansiz/PandaX_UserbotModules modules/"
    )
except BaseException:
    pass
LOGS.info("Installing packages for modules")
os.system("pip install -r modules/modules.txt")

start_time = time.time()
petercordpanda_bot_version = "_PandaX_Userbot_"

OWNER_NAME = petercordpanda_bot.me.first_name
OWNER_ID = petercordpanda_bot.me.id

List = []
Dict = {}
N = 0

def grt(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

NOSPAM_CHAT = [
    -1001387666944,  # @PyrogramChat
    -1001109500936,  # @TelethonChat
    -1001050982793,  # @Python
    -1001256902287,  # @DurovsChat
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]
