"""
β’πΎπ€π’π’ππ£π: `{i}addfilter <word><reply to a message>`
    add the used word as filter relating to replied message.
β’πΎπ€π’π’ππ£π: `{i}remfilter <word>`
    Remove the filtered user..
β’πΎπ€π’π’ππ£π: `{i}listfilter`
    list all filters.
"""

import os

from telegraph import upload_file as uf
from telethon.tl.types import User
from telethon.utils import pack_bot_file_id

from PandaX_Userbot.functions.filter_db import *

from . import *


@ilhammansiz_cmd(pattern="addfilter ?(.*)")
async def af(e):
    wrd = (e.pattern_match.group(1)).lower()
    wt = await e.get_reply_message()
    chat = e.chat_id
    if not (wt and wrd):
        return await eor(e, "`Use this command word to set as filter and reply...`")
    if wt and wt.media:
        wut = mediainfo(wt.media)
        if wut.startswith(("pic", "gif")):
            dl = await bot.download_media(wt.media)
            variable = uf(dl)
            m = "https://telegra.ph" + variable[0]
        elif wut == "video":
            if wt.media.document.size > 8 * 1000 * 1000:
                return await eod(x, "`Unsupported Media`")
            else:
                dl = await bot.download_media(wt.media)
                variable = uf(dl)
                os.remove(dl)
                m = "https://telegra.ph" + variable[0]
        else:
            m = pack_bot_file_id(wt.media)
        if wt.text:
            add_filter(int(chat), wrd, wt.text, m)
        else:
            add_filter(int(chat), wrd, None, m)
    else:
        add_filter(int(chat), wrd, wt.text, None)
    await eor(e, f"Done : Filter `{wrd}` Saved.")


@ilhammansiz_cmd(pattern="remfilter ?(.*)")
async def rf(e):
    wrd = (e.pattern_match.group(1)).lower()
    chat = e.chat_id
    if not wrd:
        return await eor(e, "`Give the filter to remove..`")
    rem_filter(int(chat), wrd)
    await eor(e, f"Done : Filter `{wrd}` Removed.")


@ilhammansiz_cmd(pattern="listfilter$")
async def lsnote(e):
    x = list_filter(e.chat_id)
    if x:
        sd = "Filters Found In This Chats Are\n\n"
        await eor(e, sd + x)
    else:
        await eor(e, "No Filters Found Here")


@petercordpanda_bot.on(events.NewMessage())
async def fl(e):
    if isinstance(e.sender, User) and e.sender.bot:
        return
    xx = (e.text).lower()
    chat = e.chat_id
    x = get_filter(int(chat))
    if x:
        if " " in xx:
            xx = xx.split(" ")
            kk = ""
            for c in xx:
                if c in x:
                    k = get_reply(int(chat), c)
                    if k:
                        kk = k
            if kk:
                msg = k["msg"]
                media = k["media"]
                await e.reply(msg, file=media)

        else:
            k = get_reply(chat, xx)
            if k:
                msg = k["msg"]
                media = k["media"]
                await e.reply(msg, file=media)
