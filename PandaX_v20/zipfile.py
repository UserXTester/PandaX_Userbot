"""
•𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}zip <reply to file>
    zip the replied file
•𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}unzip <reply to zip file>`
    unzip the replied file.
•𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}azip <reply to file>`
   add file to batch for batch upload zip
•𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}dozip`
   upload batch zip the files u added from `{i}azip`
"""

import os
import time

from . import *


@ilhammansiz_cmd(pattern="zip$")
async def zipp(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        await eor(event, "Reply to any media/Document.")
        return
    xx = await eor(event, "`Processing...`")
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            image = await downloader(
                reply.file.name, reply.media.document, xx, t, "Downloading..."
            )
            file = image.name
        else:
            file = await event.download_media(reply)
    inp = file.replace(file.split(".")[-1], "zip")
    await bash(f"zip -r {inp} {file}")
    k = time.time()
    xxx = await uploader(inp, inp, k, xx, "Uploading...")
    await petercordpanda_bot.send_file(
        event.chat_id,
        xxx,
        force_document=True,
        thumb="PandaVersion/Panda/PandaBlanck.jpg",
        caption=f"`{xxx.name}`",
        reply_to=reply,
    )
    os.remove(inp)
    os.remove(file)
    await xx.delete()


@ilhammansiz_cmd(pattern="unzip$")
async def unzipp(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        await eor(event, "Reply to any media/Document.")
        return
    xx = await eor(event, "`Processing...`")
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            mime_type = file.mime_type
            if "application" not in mime_type:
                return await xx.edit("`Reply To zipped File`")
            image = await downloader(
                reply.file.name, reply.media.document, xx, t, "Downloading..."
            )
            file = image.name
            if not file.endswith(("zip", "rar", "exe")):
                return await xx.edit("`Reply To zip File Only`")
        else:
            return await xx.edit("`Reply to zip file only`")
    if not os.path.isdir("unzip"):
        os.mkdir("unzip")
    else:
        os.system("rm -rf unzip")
        os.mkdir("unzip")
    await bash(f"7z x {file} -aoa -ounzip")
    ok = get_all_files("unzip")
    for x in ok:
        k = time.time()
        xxx = await uploader(x, x, k, xx, "Uploading...")
        await petercordpanda_bot.send_file(
            event.chat_id,
            xxx,
            force_document=True,
            thumb="PandaVersiaon/Panda/PandaBlanck.jpg",
            caption=f"`{xxx.name}`",
        )
    await xx.delete()


@ilhammansiz_cmd(pattern="addzip$")
async def azipp(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        await eor(event, "Reply to any media/Document.")
        return
    xx = await eor(event, "`Processing...`")
    if not os.path.isdir("zip"):
        os.mkdir("zip")
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            image = await downloader(
                "zip/" + reply.file.name, reply.media.document, xx, t, "Downloading..."
            )
            file = image.name
        else:
            file = await event.download_media(reply.media, "zip/")
    await xx.edit(
        f"Downloaded `{file}` succesfully\nNow Reply To Other Files To Add And Zip all at once"
    )


@ilhammansiz_cmd(pattern="dozip$")
async def do_zip(event):
    if not os.path.isdir("zip"):
        return await eor(
            event, "First All Files Via {i}addzip then doZip to zip all files at one."
        )
    xx = await eor(event, "`processing`")
    await bash(f"zip -r petercordpanda.zip zip/*")
    k = time.time()
    xxx = await uploader(
        "petercordpanda.zip", "petercordpanda.zip", k, xx, "Uploading..."
    )
    await petercordpanda_bot.send_file(
        event.chat_id,
        xxx,
        force_document=True,
        thumb="PandaVersion/Panda/PandaBlanck.jpg",
    )
    os.system("rm -rf zip")
    os.remove("petercordpanda.zip")
    await xx.delete()
