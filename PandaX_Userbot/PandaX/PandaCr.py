# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import asyncio
import os
import time
import urllib
from pathlib import Path
from random import randint
from urllib.request import urlretrieve

from pytz import timezone
from telethon.errors.rpcerrorlist import ChannelsTooMuchError
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

from .. import *
from ..Panda.database import Var
from ..functions.all import updater
from PandaX_Userbot.utils import load_modules


def startup_stuff():
    x = ["PandaVersion/auths", "PandaVersion/downloads", "modules", "PandaX_v21/downloads"]
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
            "https://telegra.ph//file/a65a4fddaba3a31dc4047.jpg", "channelphoto.jpg"
        )
        ll = await petercordpanda_bot.upload_file("channelphoto.jpg")
        await petercordpanda_bot(EditPhotoRequest(chat_id, InputChatUploadedPhoto(ll)))
        os.remove("channelphoto.jpg")
    else:
        os.remove(pfpa)


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
                "botfather", "PandaVersion/Panda/pandaasis.jpg"
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


async def plug(plugin_channels):
    if not os.path.exists("modules/__init__.py"):
        with open("modules/__init__.py", "w") as f:
            f.write("from PandaX_v20 import *")
    for Plug_channel in plugin_channels.split():
        try:
            if Plug_channel.startswith("@"):
                chat = Plug_channel
            else:
                try:
                    chat = int(Plug_channel)
                except BaseException:
                    return
            async for x in petercordpanda_bot.iter_messages(
                chat, search=".py", filter=InputMessagesFilterDocument, wait_time=10
            ):
                await asyncio.sleep(0.6)
                files = await petercordpanda_bot.download_media(x.media, "./modules/")
                file = Path(files)
                plugin = file.stem
                if "(" not in files:
                    try:
                        load_modules(plugin.replace(".py", ""))
                        LOGS.info(f"PandaX - PLUGIN_CHANNEL - Installed - {plugin}")
                    except Exception as e:
                        LOGS.info(f"PandaX - PLUGIN_CHANNEL - ERROR - {plugin}")
                        LOGS.info(str(e))
                        os.remove(files)
                else:
                    LOGS.info(f"Plugin {plugin} is Pre Installed")
                    os.remove(files)
        except Exception as e:
            LOGS.info(str(e))



async def pandailham(channel_panda):
    if not os.path.exists("Panda-Userbot/__init__.py"):
        with open("Panda-Userbot/__init__.py", "w") as f:
            f.write("from PandaX_v20 import *")
    for Plug_channel in plugin_channels.split():
        try:
            if Plug_channel.startswith("@"):
                chat = Plug_channel
            else:
                try:
                    chat = int(Plug_channel)
                except BaseException:
                    return
            async for x in petercordpanda_bot.iter_messages(
                chat, search=".py", filter=InputMessagesFilterDocument, wait_time=10
            ):
                await asyncio.sleep(0.6)
                files = await petercordpanda_bot.download_media(x.media, "./Panda-Userbot/")
                file = Path(files)
                plugin = file.stem
                if "(" not in files:
                    try:
                        load_panda(plugin.replace(".py", ""))
                        LOGS.info(f"PandaX - PLUGIN_CHANNEL - Installed - {plugin}")
                    except Exception as e:
                        LOGS.info(f"PandaX - PLUGIN_CHANNEL - ERROR - {plugin}")
                        LOGS.info(str(e))
                        os.remove(files)
                else:
                    LOGS.info(f"Plugin {plugin} is Pre Installed")
                    os.remove(files)
        except Exception as e:
            LOGS.info(str(e))


# some stuffs
async def ready():
    chat_id = int(udB.get("LOG_CHANNEL"))
    MSG = f"**PandaX_Userbot Berhasil deployed!**\n➖➖➖➖➖➖➖➖➖\n**UserMode**: [{petercordpanda_bot.me.first_name}](tg://user?id={petercordpanda_bot.me.id})\n**Assistant**: @{asst.me.username}\n➖➖➖➖➖➖➖➖➖\n**Support**: @TeamSquadUserbotSupport\n➖➖➖➖➖➖➖➖➖"
    BTTS = []
    PHOTO, spam_sent = None, None
    updava = updater()
    prev_spam = udB.get("LAST_UPDATE_LOG_SPAM")
    if prev_spam:
        try:
            await petercordpanda_bot.delete_messages(chat_id, int(prev_spam))
        except Exception as E:
            LOGS.info("Error while Deleting Previous Update Message :" + str(E))
    if updava:
        BTTS.append(Button.inline("Update Available", "updtavail"))

    if not udB.get("INIT_DEPLOY"):  # Detailed Message at Initial Deploy
        MSG = """🎇 **Thanks for Deploying PandaX_Userbot!**
• Here, are the Some Basic stuff from, where you can Know, about its Usage."""
        PHOTO = "https://telegra.ph//file/a65a4fddaba3a31dc4047.jpg"
        BTTS.append(Button.inline("• Click to Start •", "initft_2"))
        udB.set("INIT_DEPLOY", "Done")
    if BTTS == []:
        BTTS = None
    try:
        spam_sent = await asst.send_message(chat_id, MSG, file=PHOTO, buttons=BTTS)
    except ValueError as e:
        try:
            await (await petercordpanda_bot.send_message(LOG_CHANNEL, str(e))).delete()
            await asst.send_message(LOG_CHANNEL, MSG, file=PHOTO, buttons=BTTS)
        except Exception as g:
            LOGS.info(g)
    except Exception as el:
        LOGS.info(el)
        try:
            spam_sent = await petercordpanda_bot.send_message(chat_id, MSG)
        except Exception as ef:
            LOGS.info(ef)
    if spam_sent and not spam_sent.media:
        udB.set("LAST_UPDATE_LOG_SPAM", spam_sent.id)
    try:
        # To Let Them know About New Updates and Changes
        await petercordpanda_bot(JoinChannelRequest("@TeamSquadUserbotSupport"))
    except ChannelsTooMuchError:
        LOGS.info("Join @TeamSquadUserbotSupport to know about new Updates...")
