"""
•𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}glitch <replt to media>`
    gives a glitchy gif.
"""

import os

from . import *


@ilhammansiz_cmd(pattern="glitch$")
async def _(e):
    reply = await e.get_reply_message()
    if not (reply and reply.media):
        return await eor(e, "Reply to any media")
    wut = mediainfo(reply.media)
    if not wut.startswith(("pic", "sticker")):
        return await eor(e, "`Unsupported Media`")
    xx = await eor(e, "`Gliching...`")
    ok = await bot.download_media(reply.media)
    cmd = f"glitch_me gif --line_count 200 -f 10 -d 50 '{ok}' ult.gif"
    stdout, stderr = await bash(cmd)
    await petercordpanda_bot.send_file(
        e.chat_id, "ult.gif", force_document=False, reply_to=reply
    )
    await xx.delete()
    os.remove(ok)
    os.remove("ult.gif")
