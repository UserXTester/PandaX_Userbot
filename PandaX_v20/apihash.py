"""
🔖{i}lanjut
"""

from . import *


@ilhammansiz_cmd(
    pattern="lanjut$",
)
async def _(e):
    await eor(e, "`Sabar tot..`")
    await bash("python3 bot.py")
