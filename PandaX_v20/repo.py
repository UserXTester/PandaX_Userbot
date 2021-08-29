from telethon.errors import ChatSendInlineForbiddenError
from telethon.errors.rpcerrorlist import BotMethodInvalidError as bmi

from . import *

REPOMSG = (
    "💐 **Panda USERBOT** 💐\n\n",
    "REPO - [REPO](https://github.com/PandaUserbot/Panda)\n",
    "MODULES - [MODULES](https://github.com/IlhamMansiz/PandaX_UserbotModules)\n",
    "SUPPORT - @TEAMSquadUserbotSupport",
)


@ilhammansiz_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await petercordpanda_bot.inline_query(asst.me.username, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == petercordpanda_bot.uid:
            await e.delete()
    except (ChatSendInlineForbiddenError, bmi):
        await eor(e, REPOMSG)


@ilhammansiz_cmd(pattern="ialive$")
async def repify(e):
    try:
        q = await petercordpanda_bot.inline_query(asst.me.username, "aliveilham")
        await q[0].click(e.chat_id)
        if e.sender_id == petercordpanda_bot.uid:
            await e.delete()
    except (ChatSendInlineForbiddenError, bmi):
        await eor(e, REPOMSG)
