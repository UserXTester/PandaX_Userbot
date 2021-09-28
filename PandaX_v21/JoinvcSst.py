
from pytgcalls.exceptions import NotConnectedError
from telethon import events

from . import *


@PadaBotX.on(events.NewMessage(incoming=True, pattern="/joinvc"))
async def join_(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat, event)
    if not ultSongs.group_call.is_connected:
        await ultSongs.vc_joiner()



@PadaBotX.on(events.NewMessage(incoming=True, pattern="/leavevc"))
async def leaver(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat)
    await ultSongs.group_call.stop()
    if CLIENTS.get(chat):
        del CLIENTS[chat]
    if VIDEO_ON.get(chat):
        del VIDEO_ON[chat]
    await eor(event, "`Left the voice chat.`")


@PadaBotX.on(events.NewMessage(incoming=True, pattern="/rejoin"))
async def rejoiner(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat)
    try:
        await ultSongs.group_call.reconnect()
    except NotConnectedError:
        return await eor(event, "You haven't connected to a voice chat!")
    await eor(event, "`Re-joining this voice chat.`")
