# Team Ultroid
# copyright 2021 (c) TEAM ULTROID
# 

"""
• `{i}update`
   perintah untuk memeriksa pembaruan userbot dan memperbarui nya ke versi terbaru.
"""

from git import Repo
from telethon.tl.functions.channels import ExportMessageLinkRequest as GetLink

from . import *

PANDAPIC = "PandaVersion/Panda/Logo.jpg"
CL = udB.get("INLINE_PIC")
if CL:
    PANDAPIC = CL


@ilhammansiz_cmd(pattern="update ?(.*)")
async def _(e):
    xx = await eor(e, "`Checking for updates...`")
    m = updater()
    branch = (Repo.init()).active_branch
    if m:
        if e.pattern_match.group(1):
            if "fast" in e.pattern_match.group(1) or "soft" in e.pattern_match.group(1):
                await bash("git pull -f && pip3 install -r PandaVersion/Panda/requirements.txt")
                call_back()
                await xx.edit("`Fast Soft Updating...`")
                execl(sys.executable, "python3", "-m", "PandaX_Userbot")
                return
        x = await asst.send_file(
            int(udB.get("LOG_CHANNEL")),
            ULTPIC,
            caption="• **Update Available** •",
            force_document=False,
            buttons=Button.inline("Changelogs", data="changes"),
        )
        Link = x.message_link
        await xx.edit(
            f'<strong><a href="{Link}">[ChangeLogs]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )
    else:
        await xx.edit(
            f'<code>Your BOT is </code><strong>up-to-date</strong><code> with </code><strong><a href="https://github.com/ilhammansiz/PandaX_Userbot/tree/{branch}">[{branch}]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )

@ilhammansiz_cmd(
    pattern="update$",
)
async def restartbt(ult):
    ok = await eor(ult, "`Sedang update sabar ya  Panda-userbot...`")
    if Var.HEROKU_API:
        await restart(ok)
    else:
        await bash("pkill python3 && python3 -m PandaX_Userbot")


@callback("updtavail")
@owner
async def updava(event):
    await event.delete()
    await asst.send_file(
        int(udB.get("LOG_CHANNEL")),
        PANDAPIC,
        caption="• **Update Available** •",
        force_document=False,
        buttons=Button.inline("Changelogs", data="changes"),
    )
