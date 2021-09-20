"""
•𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}ping`
   ketik {i}ping untuk melihat kecepatan Panda Userbotmu.
"""
import time
import asyncio
from datetime import datetime
from speedtest import Speedtest

from . import *


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time



@ilhammansiz_cmd(pattern="ping")
async def dsb(ult):
    uptime = await get_readable_time((time.time() - start_time))
    start = datetime.now()
    ult = await eor(ult, "`🐼`")
    await asyncio.sleep(0.5)
    await ult.edit("`Pong 𖣘𖣘𖣘𖣘𖣘𖣘..`")
    await asyncio.sleep(0.5)
    await ult.edit("`𖣘𖣘𖣘𖣘𖣘𖣘...`")
    await ult.edit("`𖣘𖣘𖣘𖣘𖣘𖣘....`")
    await asyncio.sleep(0.5)
    await ult.edit("`⏰`")
    await asyncio.sleep(0.5)
    await ult.edit("`⏳`")
    await asyncio.sleep(0.5)
    await ult.edit("`⌛`")
    await asyncio.sleep(0.5)
    await ult.edit("`🔓`")
    await asyncio.sleep(0.5)
    await ult.edit("`🔒`")
    await asyncio.sleep(0.5)
    await ult.edit("`🚀`")
    await asyncio.sleep(0.5)
    await ult.edit("`🛰`")
    await asyncio.sleep(0.5)
    await ult.edit("`✦҈͜͡➳`")
    await ult.edit("`⚡`")
    await asyncio.sleep(0.5)
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await ult.edit(get_string("ping").format(ms, uptime))


