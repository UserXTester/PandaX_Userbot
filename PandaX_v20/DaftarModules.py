import asyncio
from . import *
from platform import uname

from PandaX_Userbot.Panda.core import *





@ilhammansiz_cmd(pattern="daftarplugin ?(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in HELP:
            await event.edit(str(HELP[args]))
        else:
            await event.edit("**`Command Tidak Ditemukan, Harap Ketik Command Dengan Benar`**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in HELP:
            string += "`" + str(i)
            string += "`\t 🖨  "
        await event.edit("**PandaX_Userbot**\n\n"
                         f"**◉ Bᴏᴛ ᴏꜰ PandaX_Userbot Plugin**\n**◉ Mᴏᴅᴜʟᴇꜱ : {len(HELP)}**\n\n"
                         "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                         f"◉ {string}◉\n\n")
        await event.reply(f"\n**Contoh** : Ketik <`.help afk`> Untuk Informasi Pengunaan.\nAtau Bisa Juga Ketik `.helpme` Untuk Main Menu Yang Lain-Nya.")
        await asyncio.sleep(1000)
        await event.delete()


@ilhammansiz_cmd(pattern="daftarmodules ?(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**`Command Tidak Ditemukan, Harap Ketik Command Dengan Benar`**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t 🖨  "
        await event.edit("**PandaX_Userbot**\n\n"
                         f"**◉ Bᴏᴛ ᴏꜰ PandaX_Userbot Plugin**\n**◉ Mᴏᴅᴜʟᴇꜱ : {len(CMD_HELP)}**\n\n"
                         "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                         f"◉ {string}◉\n\n")
        await event.reply(f"\n**Contoh** : Ketik <`.help afk`> Untuk Informasi Pengunaan.\nAtau Bisa Juga Ketik `.helpme` Untuk Main Menu Yang Lain-Nya.")
        await asyncio.sleep(1000)
        await event.delete()
