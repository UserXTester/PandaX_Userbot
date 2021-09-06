# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from os import environ
import asyncio
import multiprocessing
import os
import time
import traceback
import urllib
from pathlib import Path
from random import randint
from urllib.request import urlretrieve
from importlib import import_module
from PandaX_Userbot.vc import ALL_MODULES

from pyrogram import idle, Client
from pytz import timezone
from telethon.errors.rpcerrorlist import (
    AccessTokenExpiredError,
    ApiIdInvalidError,
    AuthKeyDuplicatedError,
    ChannelsTooMuchError,
    PhoneNumberInvalidError,
)
from telethon.tl.custom import Button
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    JoinChannelRequest,
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import (
    ChatAdminRights,
    InputChatUploadedPhoto,
    InputMessagesFilterDocument,
)

from . import *
from .Panda import DEVLIST
from .Panda.database import Var
from .functions.all import updater
from .PandaSX_userbot.PandaLoad import plugin_loader
from .utils import load_modules

x = ["PandaVersion/auths", "PandaVersion/downloads", "modules"]
for x in x:
    if not os.path.isdir(x):
        os.mkdir(x)

if udB.get("CUSTOM_THUMBNAIL"):
    urlretrieve(udB.get("CUSTOM_THUMBNAIL"), "PandaVersion/Panda/PandaBlanck.jpg")

if udB.get("GDRIVE_TOKEN"):
    with open("PandaVersion/auths/auth_token.txt", "w") as t_file:
        t_file.write(udB.get("GDRIVE_TOKEN"))

if udB.get("MEGA_MAIL") and udB.get("MEGA_PASS"):
    with open(".megarc", "w") as mega:
        mega.write(
            f'[Login]\nUsername = {udB.get("MEGA_MAIL")}\nPassword = {udB.get("MEGA_PASS")}'
        )

if udB.get("TIMEZONE"):
    try:
        timezone(udB.get("TIMEZONE"))
        os.environ["TZ"] = udB.get("TIMEZONE")
        time.tzset()
    except BaseException:
        LOGS.info(
            "Incorrect Timezone ,\nCheck Available Timezone From Here https://telegra.ph/iLHam-MansiezZ-06-27\nSo Time is Default UTC"
        )
        os.environ["TZ"] = "UTC"
        time.tzset()


async def autobot():
    await petercordpanda_bot.start()
    if Var.BOT_TOKEN:
        udB.set("BOT_TOKEN", str(Var.BOT_TOKEN))
        return
    if udB.get("BOT_TOKEN"):
        return
    LOGS.info("🛠 MEMBUAT BOT UNTUK ANDA DI @BotFather, HARAP TUNGU !!")
    who = await petercordpanda_bot.get_me()
    name = "PandaX_Userbot Assistant " + who.first_name
    if who.username:
        username = who.username + "_bot"
    else:
        username = "PandaX_Userbot_" + (str(who.id))[5:] + "_bot"
    bf = "Botfather"
    await petercordpanda_bot(UnblockRequest(bf))
    await petercordpanda_bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await petercordpanda_bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await petercordpanda_bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await petercordpanda_bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Mohon buat bot baru di @BotFather dan tambahkan var BOT_TOKEN, lalu isi token nya dan restart."
        )
        exit(1)
    await petercordpanda_bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await petercordpanda_bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await petercordpanda_bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await ultroid_bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Mohon buat bot baru di @BotFather dan tambahkan var BOT_TOKEN, lalu isi token nya dan restart."
            )
            exit(1)
    await petercordpanda_bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await petercordpanda_bot.get_messages(bf, limit=1))[0].text
    await petercordpanda_bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "PandaX_Userbot" + (str(who.id))[6:] + str(ran) + "_bot"
        await petercordpanda_bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await petercordpanda_bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            udB.set("BOT_TOKEN", token)
            await petercordpanda_bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message(bf, "menu...")
            LOGS.info(f"SELESAI, ASSISTANT BOT ANDA SUDAH DIBUAT @{username}")
        else:
            LOGS.info(
                f"Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot."
            )
            exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        udB.set("BOT_TOKEN", token)
        await petercordpanda_bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await petercordpanda_bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await petercordpanda_bot.send_message(bf, "menu...")
        LOGS.info(f"SELESAI, ASSISTANT BOT ANDA SUDAH DIBUAT @{username}")
    else:
        LOGS.info(
            f"Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot."
        )
        exit(1)


if not udB.get("BOT_TOKEN"):
    petercordpanda_bot.loop.run_until_complete(autobot())


async def istart():
    petercordpanda_bot.me = await petercordpanda_bot.get_me()
    petercordpanda_bot.uid = petercordpanda_bot.me.id
    petercordpanda_bot.first_name = petercordpanda_bot.me.first_name
    if not petercordpanda_bot.me.bot:
        udB.set("OWNER_ID", petercordpanda_bot.uid)


async def autopilot():
    if Var.LOG_CHANNEL and str(Var.LOG_CHANNEL).startswith("-100"):
        udB.set("LOG_CHANNEL", str(Var.LOG_CHANNEL))
    k = []  # To Refresh private ids
    async for x in petercordpanda_bot.iter_dialogs():
        k.append(x.id)
    if udB.get("LOG_CHANNEL"):
        try:
            await petercordpanda_bot.get_entity(int(udB.get("LOG_CHANNEL")))
            return
        except BaseException:
            udB.delete("LOG_CHANNEL")
    try:
        r = await petercordpanda_bot(
            CreateChannelRequest(
                title="𝐏𝐚𝐧𝐝𝐚𝐗_𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐋𝐎𝐆",
                about="𝐏𝐚𝐧𝐝𝐚𝐗_𝐔𝐬𝐞𝐫𝐛𝐨𝐭 LOG GROUP.\n\n JOIN @TEAMSquadUserbotSupport",
                megagroup=True,
            ),
        )
    except ChannelsTooMuchError:
        LOGS.info(
            "Grup dan channel anda terlalu banyak, Keluar dari salah satu grup atau channel lalu restart."
        )
        exit(1)
    except BaseException:
        LOGS.info(
            "Ada yang Salah, Buat Grup dan atur id-nya di config var LOG_CHANNEL."
        )
        exit(1)
    chat_id = r.chats[0].id
    if not str(chat_id).startswith("-100"):
        udB.set("LOG_CHANNEL", "-100" + str(chat_id))
    else:
        udB.set("LOG_CHANNEL", str(chat_id))
    rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        anonymous=False,
        manage_call=True,
    )
    await petercordpanda_bot(EditAdminRequest(chat_id, asst.me.username, rights, "Assistant"))
    pfpa = await petercordpanda_bot.download_profile_photo(chat_id)
    if not pfpa:
        urllib.request.urlretrieve(
            "https://telegra.ph//file/813db0b898e3df7611c2c.jpg", "channelphoto.jpg"
        )
        ll = await petercordpanda_bot.upload_file("channelphoto.jpg")
        await petercordpanda_bot(EditPhotoRequest(chat_id, InputChatUploadedPhoto(ll)))
        os.remove("channelphoto.jpg")
    else:
        os.remove(pfpa)

async def bot_info():
    asst.me = await asst.get_me()
    return asst.me


LOGS.info("menginialisasi...")


# log in
BOT_TOKEN = udB.get("BOT_TOKEN")
LOGS.info("STARTING PANDA...")
try:
    asst.start(bot_token=BOT_TOKEN)
    petercordpanda_bot.start()
    petercordpanda_bot.loop.run_until_complete(istart())
    petercordpanda_bot.loop.run_until_complete(bot_info())
    LOGS.info("done, startup completed")
    LOGS.info("ASSISTANT - STARTED")
except (AuthKeyDuplicatedError, PhoneNumberInvalidError, EOFError):
    LOGS.info("Session String expired. Silahkan buat string baru, PandaX_Userbot dihentikan...")
    exit(1)
except ApiIdInvalidError:
    LOGS.info("HELLO, API ID/API HASH anda tidak diatur dengan benar, silahkan cek lagi !!.")
    exit(1)
except AccessTokenExpiredError:
    udB.delete("BOT_TOKEN")
    LOGS.info(
        "BOT_TOKEN expired, So Quitted The Process, Restart Again To create A new Bot. Or Set BOT_TOKEN env In Vars"
    )
    exit(1)
except BaseException:
    LOGS.info("Error: " + str(traceback.print_exc()))
    exit(1)


if str(petercordpanda_bot.uid) not in DEVLIST:
    chat = eval(udB.get("BLACKLIST_CHATS"))
    if -1001327032795 not in chat:
        chat.append(-1001327032795)
        udB.set("BLACKLIST_CHATS", str(chat))

petercordpanda_bot.loop.run_until_complete(autopilot())

pmbot = udB.get("PMBOT")
manager = udB.get("MANAGER")
modules = udB.get("MODULES") or Var.MODULES
vcbot = udB.get("VC_SESSION") or Var.VC_SESSION

plugin_loader(modules=modules, pmbot=pmbot, manager=manager, vcbot=vcbot)

# for channel plugins
Plug_channel = udB.get("PLUGIN_CHANNEL")
if Plug_channel:

    async def plug():
        try:
            if Plug_channel.startswith("@"):
                chat = Plug_channel
            else:
                try:
                    chat = int(Plug_channel)
                except BaseException:
                    return
            async for x in petercordpanda_bot.iter_messages(
                chat, search=".py", filter=InputMessagesFilterDocument
            ):
                await asyncio.sleep(0.6)
                files = await petercordpanda_bot.download_media(x.media, "./modules/")
                file = Path(files)
                plugin = file.stem
                if "(" not in files:
                    try:
                        load_modules(plugin.replace(".py", ""))
                        LOGS.info(f"PandaX_Userbot - PLUGIN_CHANNEL - Installed - {plugin}")
                    except Exception as e:
                        LOGS.info(f"PandaX_Userbot - PLUGIN_CHANNEL - ERROR - {plugin}")
                        LOGS.info(str(e))
                else:
                    LOGS.info(f"Plugin {plugin} Sudah Di Install")
                    os.remove(files)
        except Exception as e:
            LOGS.info(str(e))




# customize assistant


async def customize():
    try:
        chat_id = int(udB.get("LOG_CHANNEL"))
        xx = await petercordpanda_bot.get_entity(asst.me.username)
        if xx.photo is None:
            LOGS.info("Mengkostumisasi assistant bot anda di @BotFather")
            UL = f"@{asst.me.username}"
            if (petercordpanda_bot.me.username) is None:
                sir = petercordpanda_bot.me.first_name
            else:
                sir = f"@{petercordpanda_bot.me.username}"
            await petercordpanda_bot.send_message(
                chat_id, "Kostumisasi otomatis dimulai di @botfather"
            )
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", "/cancel")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", "/start")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", "/setuserpic")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await petercordpanda_bot.send_file(
                "botfather", "PandaVersion/Panda/PandaGrup.jpg"
            )
            await asyncio.sleep(2)
            await petercordpanda_bot.send_message("botfather", "/setabouttext")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message(
            "botfather", f"🙋 Hello ✨ Saya PandaX_Userbot Assistant {sir}"
            )
            await asyncio.sleep(2)
            await petercordpanda_bot.send_message("botfather", "/setdescription")
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await petercordpanda_bot.send_message(
            "botfather",
            f"PandaX_Userbot Assistant\nPengguna ~ {sir}\n\nBy ~ @diemmmmmmmmmm\nSupport ~ @TEAMSquadUserbotSupport ",
            )
            await asyncio.sleep(2)
            await petercordpanda_bot.send_message(
                chat_id, "**Kostumisasi Otomatis** Selesai Di @BotFather"
            )
            LOGS.info("Customisation Done")
    except Exception as e:
        LOGS.info(str(e))


# some stuffs
async def ready():
    chat_id = int(udB.get("LOG_CHANNEL"))
    MSG = f"**♨ PandaX_Userbot AKTIF ♨**\n➖➖➖➖➖➖➖➖➖\n**Userbot**: [{petercordpanda_bot.me.first_name}](tg://user?id={petercordpanda_bot.me.id})\n**ASSISTANT**: @{asst.me.username}\n➖➖➖➖➖➖➖➖➖\n**SUPPORT**: @TEAMSquadUserbotSupport\n➖➖➖➖➖➖➖➖➖"
    BTTS = [Button.inline("♨ BUKA MENU HELP ♨", "open")]
    try:
        # To Let Them know About New Updates and Changes
        await petercordpanda_bot(JoinChannelRequest("@TEAMSquadUserbotSupport"))
    except BaseException:
        pass



def pycli():
    vcasst.start()
    multiprocessing.Process(target=idle).start()
    CallsClient.run()


suc_msg = """
            ----------------------------------------------------------------------
             ♻ PandaX_Userbot ♻ has been deployed! Visit @TEAMSquadUserbotSupport for updates!
            ----------------------------------------------------------------------
"""

petercordpanda_bot.loop.run_until_complete(customize())
if Plug_channel:
    petercordpanda_bot.loop.run_until_complete(plug())
petercordpanda_bot.loop.run_until_complete(ready())


if __name__ == "__main__":
    if vcbot:
        if vcasst and vcClient and CallsClient:
            multiprocessing.Process(target=pycli).start()
        LOGS.info(suc_msg)
        multiprocessing.Process(target=petercordpanda_bot.run_until_disconnected).start()
    else:
        LOGS.info(suc_msg)
        petercordpanda_bot.run_until_disconnected()
