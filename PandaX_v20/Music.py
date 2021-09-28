"""
🔖{i}lanjut
"""

from . import *


@ilhammansiz_cmd(
    pattern="lanjut$",
)
async def restartbt(ult):
    ok = await eor(ult, "`Sedang sabar ya  Ngentot...`")
    if Var.HEROKU_API:
        await restart(ok)
    else:
        await bash("pkill python3 && python3 -m MusicBot")
