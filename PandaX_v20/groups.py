# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
•𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}setgpic <reply to Photo>`
    Set Profile photo of Group.
•𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}unbanall`
    Unban all Members of a group.
•𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}rmusers`
    Remove users specifically.
"""
from telethon.tl.functions.channels import EditBannedRequest, EditPhotoRequest
from telethon.tl.types import (
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)

from . import *


@ilhammansiz_cmd(pattern="setgpic$", groups_only=True, admins_only=True)
async def _(ult):
    if not ult.is_reply:
        return await eod(ult, "`Reply to a Media..`")
    reply_message = await ult.get_reply_message()
    try:
        replfile = await reply_message.download_media()
    except AttributeError:
        return await eor(ult, "Reply to a Photo..")
    file = await ult.client.upload_file(replfile)
    mediain = mediainfo(reply_message.media)
    try:
        if "pic" in mediain:
            await ult.client(EditPhotoRequest(ult.chat_id, file))
        else:
            return await eod(ult, "`Invalid MEDIA Type !`")
        await eod(ult, "`Group Photo has Successfully Changed !`")
    except Exception as ex:
        await eod(ult, "Error occured.\n`{}`".format(str(ex)))
    os.remove(replfile)


@ilhammansiz_cmd(
    pattern="unbanall$",
    groups_only=True,
)
async def _(event):
    xx = await eor(event, "Searching Participant Lists.")
    p = 0
    (await event.get_chat()).title
    async for i in event.client.iter_participants(
        event.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await event.client.edit_permissions(event.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await eod(xx, "{title}: {p} unbanned")


@ilhammansiz_cmd(
    pattern="rmusers ?(.*)",
    groups_only=True,
)
async def _(event):
    xx = await eor(event, "Searching Participant Lists.")
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not (chat.admin_rights or chat.creator):
            return await eod(xx, "`You aren't an admin here!`", time=5)
    p = 0
    b = 0
    c = 0
    d = 0
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    async for i in event.client.iter_participants(event.chat_id):
        p += 1
        rights = ChatBannedRights(
            until_date=None,
            view_messages=True,
        )
        if isinstance(i.status, UserStatusEmpty):
            y += 1
            if "empty" in input_str:
                try:
                    await event.client(
                        EditBannedRequest(event.chat_id, i, rights),
                    )
                    c += 1
                    y -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusLastMonth):
            m += 1
            if "month" in input_str:
                try:
                    await event.client(
                        EditBannedRequest(event.chat_id, i, rights),
                    )
                    c += 1
                    m -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusLastWeek):
            w += 1
            if "week" in input_str:
                try:
                    await event.client(
                        EditBannedRequest(event.chat_id, i, rights),
                    )
                    c += 1
                    w -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusOffline):
            o += 1
            if "offline" in input_str:
                try:
                    await event.client(
                        EditBannedRequest(event.chat_id, i, rights),
                    )
                    c += 1
                    o -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusOnline):
            q += 1
            if "online" in input_str:
                try:
                    await event.client(
                        EditBannedRequest(event.chat_id, i, rights),
                    )
                    c += 1
                    q -= 1
                except BaseException:
                    pass
        if isinstance(i.status, UserStatusRecently):
            r += 1
            if "recently" in input_str:
                try:
                    await event.client(
                        EditBannedRequest(event.chat_id, i, rights),
                    )
                    c += 1
                    r -= 1
                except BaseException:
                    pass
        if i.bot:
            b += 1
            if "bot" in input_str:
                try:
                    await event.client(
                        EditBannedRequest(event.chat_id, i, rights),
                    )
                    c += 1
                    b -= 1
                except BaseException:
                    pass
        elif i.deleted:
            d += 1
            if "deleted" in input_str:
                try:
                    await event.client(
                        EditBannedRequest(event.chat_id, i, rights),
                    )
                    c += 1
                    d -= 1
                except BaseException:
                    pass
        elif i.status is None:
            n += 1
            if "none" in input_str:
                try:
                    await event.client(
                        EditBannedRequest(event.chat_id, i, rights),
                    )
                    c += 1
                    n -= 1
                except BaseException:
                    pass
    required_string = ""
    if input_str:
        required_string += f"**>> Kicked** `{c} / {p}` **users**\n\n"
        required_string += f"  **••Deleted Accounts••** `{d}`\n"
        required_string += f"  **••UserStatusEmpty••** `{y}`\n"
        required_string += f"  **••UserStatusLastMonth••** `{m}`\n"
        required_string += f"  **••UserStatusLastWeek••** `{w}`\n"
        required_string += f"  **••UserStatusOffline••** `{o}`\n"
        required_string += f"  **••UserStatusOnline••** `{q}`\n"
        required_string += f"  **••UserStatusRecently••** `{r}`\n"
        required_string += f"  **••Bots••** `{b}`\n"
        required_string += f"  **••None••** `{n}`\n"
    else:
        required_string += f"**>> Total** `{p}` **users**\n\n"
        required_string += f"  `{HNDLR}rmusers deleted`  **••**  `{d}`\n"
        required_string += f"  `{HNDLR}rmusers empty`  **••**  `{y}`\n"
        required_string += f"  `{HNDLR}rmusers month`  **••**  `{m}`\n"
        required_string += f"  `{HNDLR}rmusers week`  **••**  `{w}`\n"
        required_string += f"  `{HNDLR}rmusers offline`  **••**  `{o}`\n"
        required_string += f"  `{HNDLR}rmusers online`  **••**  `{q}`\n"
        required_string += f"  `{HNDLR}rmusers recently`  **••**  `{r}`\n"
        required_string += f"  `{HNDLR}rmusers bot`  **••**  `{b}`\n"
        required_string += f"  `{HNDLR}rmusers none`  **••**  `{n}`\n\n"
        required_string += f"**••Empty**  `Name with deleted Account`\n"
        required_string += f"**••None**  `Last Seen A Long Time Ago`\n"
    await eod(xx, required_string)
