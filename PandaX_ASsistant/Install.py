# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """๐ **Terimakasih sudah deploy PandaX_Userbot**
โข Sekarang kamu bisa menggunakan fiturnya yang toxic atau tidak ๐๐""",
    2: """๐** About PandaX_Userbot**
โฃ Made by **@TeamSquadUserbotSupport**""",
    3: """**๐กโข FAQs โข**
-> [TUTORIAL](https://t.me/UserbotTEAM_Tutorial)
**โข To Know About Updates**
  - Join @TeamSquadUserbotSupport.""",
    4: f"""โข `To Know All Available Commands`
  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """โข **For Any Other Query or Suggestion**
  - Move to **@TeamSquadUserbotSupport**.
โข Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_" + str(4)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_" + str(2)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )
