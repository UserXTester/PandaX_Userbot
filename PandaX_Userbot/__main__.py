# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.
# Editor by ilham mansiz

import multiprocessing
import os
import sys
import traceback
from sys import argv
from telethon.errors.rpcerrorlist import (
    AccessTokenExpiredError,
    ApiIdInvalidError,
    AuthKeyDuplicatedError,
    PhoneNumberInvalidError,
)

from MusicBot.services.callsmusic import run
from pyrogram import idle
from . import *
from .Panda.database import Var
from .PandaX.PandaCr import (
    autobot,
    autopilot,
    customize,
    plug,
    ready,
    startup_stuff,
    updater,
    pandailham,
)
from .PandaX.PandaLoad import plugin_loader
from .vc.loading import ALL_MODULES
from importlib import import_module

# Option to Auto Update On Restarts..
if udB.get("UPDATE_ON_RESTART") and updater() and os.path.exists(".git"):
    os.system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
    os.execl(sys.executable, "python3", "-m", "PandaX_Userbot")

startup_stuff()

if not udB.get("BOT_TOKEN"):
    petercordpanda_bot.loop.run_until_complete(autobot())


async def istart():
    petercordpanda_bot.me = await petercordpanda_bot.get_me()
    petercordpanda_bot.me.phone = None
    petercordpanda_bot.uid = petercordpanda_bot.me.id
    petercordpanda_bot.first_name = petercordpanda_bot.me.first_name
    if not petercordpanda_bot.me.bot:
        udB.set("OWNER_ID", petercordpanda_bot.uid)


async def bot_info():
    asst.me = await asst.get_me()
    return asst.me


LOGS.info("Initialising...")


# log in
BOT_TOKEN = udB.get("BOT_TOKEN")
LOGS.info("Starting PandaX...")
try:
    asst.start(bot_token=BOT_TOKEN)
    petercordpanda_bot.start()
    petercordpanda_bot.loop.run_until_complete(istart())
    petercordpanda_bot.loop.run_until_complete(bot_info())
    LOGS.info("Done, startup completed")
    LOGS.info("Assistant - Started")
except (AuthKeyDuplicatedError, PhoneNumberInvalidError, EOFError):
    LOGS.info("Session String expired. Please create a new one! PandaX is stopping...")
    exit(1)
except ApiIdInvalidError:
    LOGS.info("Your API ID/API HASH combination is invalid. Kindly recheck.")
    exit(1)
except AccessTokenExpiredError:
    udB.delete("BOT_TOKEN")
    LOGS.info(
        "BOT_TOKEN expired , So Quitted The Process, Restart Again To create A new Bot. Or Set BOT_TOKEN env In Vars"
    )
    exit(1)
except BaseException:
    LOGS.info("Error: " + str(traceback.print_exc()))
    exit(1)


petercordpanda_bot.loop.run_until_complete(autopilot())



try:
    os.system(
        "git clone https://github.com/ilhammansiz/PandaX_UserbotModules modules/"
    )
except BaseException:
    pass
LOGS.info("Installing packages for modules")
os.system("pip install -r modules/modules.txt")

pmbot = udB.get("PMBOT")
manager = udB.get("MANAGER")
modules = udB.get("MODULES") or Var.MODULES
toxic = udB.get("PANDA") or Var.PANDA
vcbot = udB.get("VCBOT") or Var.VCBOT
botvc = udB.get("SESSION_NAME") or Var.SESSION_NAME

# Railway dont allow Music Bots
if Hosted_On == "railway" and not udB.get("VCBOT"):
    vcbot = "False"

plugin_loader(modules=modules, pmbot=pmbot, manager=manager, toxic=toxic, vcbot=vcbot)


try:
    os.system(
        "git clone https://github.com/ilhammansiz/PandaToxic_userBot music/"
    )
except BaseException:
    pass
LOGS.info("Installing packages for modules")
os.system("pip install -r music/panda.txt")


def pycli():
    client.start()
    multiprocessing.Process(target=idle).start()
    run()



suc_msg = """
            ----------------------------------------------------------------------
                🐼 PandaX_Userbot Telah Aktif Berhasil dideploy.....🐼
            ----------------------------------------------------------------------
"""

# for channel plugins
channels_panda = udB.get("CHANNEL_PANDA")
plugin_channels = udB.get("PLUGIN_CHANNEL")

petercordpanda_bot.loop.run_until_complete(customize())

if channels_panda:
    petercordpanda_bot.loop.run_until_complete(pandailham(channels_panda))

if plugin_channels:
    petercordpanda_bot.loop.run_until_complete(plug(plugin_channels))

if not udB.get("LOG_OFF"):
    petercordpanda_bot.loop.run_until_complete(ready())


if __name__ == "__main__":
    if botvc:
        if client and run:
            multiprocessing.Process(target=pycli).start()
        LOGS.info(suc_msg)
        multiprocessing.Process(target=petercordpanda_bot.run_until_disconnected).start()
    else:
        LOGS.info(suc_msg)
        petercordpanda_bot.run_until_disconnected()


