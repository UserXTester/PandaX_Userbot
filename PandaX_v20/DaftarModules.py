import asyncio
from . import *
from platform import uname

from PandaX_Userbot.Panda.core import *



modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(OWNER_NAME) if OWNER_NAME else uname().node
# ============================================
REPO_NAME = "PandaToxic_Kentot"
EMOJI_HELP = "🐼"

@register(outgoing=True, pattern="^.daftarmodules(?: |$)(.*)")
async def help(rambot):
    """ For .help command,"""
    args = rambot.pattern_match.group(1)
    if args:
        if args in CMD_HELP:
            await rambot.edit(str(CMD_HELP[args]))
        else:
            await rambot.edit("**`NGETIK YANG BENER NGENTOT!`**")
            await asyncio.sleep(50)
            await rambot.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t {EMOJI_HELP}  "
        await rambot.edit(f"**{REPO_NAME}**\n\n"
                         f"**{EMOJI_HELP} 𝙿𝙴𝙼𝙸𝙻𝙸𝙺 𝙱𝙾𝚃 : {DEFAULTUSER}**\n**{EMOJI_HELP}  𝙼𝙾𝙳𝚄𝙻𝙴𝚂 : {len(modules)}**\n\n"
                         f"**{EMOJI_HELP} 𝚂𝙴𝙼𝚄𝙰 𝙼𝙴𝙽𝚄 :**\n\n ══════════╣❃ ♕ ❃╠══════════\n\n"
                         f"{EMOJI_HELP} {string}\n\n ══════════╣❃ ♕ ❃╠══════════\n\nNGETIK YANG BENER YA NGENTOOOOT!!\n\n")
        await rambot.reply(f"\n**Contoh** : Ketik <`.help ping`> Untuk Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba wahahaha..")
        await asyncio.sleep(50)
        await rambot.delete()
