from PandaX_v20 import *



"""
🔖 {i}skull
🔖 {i}kontol
🔖 {i}ok
"""



GAMBAR_OK = """
░▐▀▀▀▀▀▀▀▀▌▐▀▌▄▄▄▀▀▓▀
░▐▌▓▀▀▀▀▓▌▌▐▐▌▀▌▄▄▀░░
░▐▐▌▐▀▀▌▐▐▌▐▌▐▓▄▀░░░░
░▐▌▌▐▄▄▌▐▌▌▐▐▌▓▀▄░░░░
░▐▐▓▄▄▄▄▓▐▌▐▌▌▄▌▀▀▄░░
░▐▄▄▄▄▄▄▄▄▌▐▄▌▀▀▀▄▄▓▄
"""


GAMBAR_TENGKORAK = """
░░░░░░░░░░░░░▄▐░░░░
░░░░░░░▄▄▄░░▄██▄░░░
░░░░░░▐▀█▀▌░░░░▀█▄░
░░░░░░▐█▄█▌░░░░░░▀█▄
░░░░░░░▀▄▀░░░▄▄▄▄▄▀▀
░░░░░▄▄▄██▀▀▀▀░░░░░
░░░░█▀▄▄▄█░▀▀░░░░░░
░░░░▌░▄▄▄▐▌▀▀▀░░░░░
░▄░▐░░░▄▄░█░▀▀░░░░░
░▀█▌░░░▄░▀█▀░▀░░░░░
░░░░░░░░▄▄▐▌▄▄░░░░░
░░░░░░░░▀███▀█▄░░░░
░░░░░░░▐▌▀▄▀▄▀▐░░░░
░░░░░░░▐▀░░░░░░▐▌░░
░░░░░░░█░░░░░░░░█░░
░░░░░░▐▌░░░░░░░░░█░
"""

GAMBAR_KONTL = """
⣠⡶⠚⠛⠲⢄⡀
⣼⠁ ⠀⠀⠀ ⠳⢤⣄
⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇
⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄
⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄
⠀⠀⠀⠘⣆ ⠀⠀⠀⠀ ⠀⠈⠓⢦⣀
⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤
⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
⠀⠀⠀⠀⠀⠀⠀⡴⠋⠓⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠈⣇
⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢦⣀⣀⣀⣀⣠⡴⠚⠁⠉⠉⠉
"""




@ilhammansiz_cmd(pattern=r"(?:kntl|kontol)\s?(.)?")
async def emoji_kontl(e):
    emoji = e.pattern_match.group(1)
    kontl = GAMBAR_KONTL
    if emoji:
        kontl = kontl.replace('😂', emoji)
    await e.edit(kontl)


@ilhammansiz_cmd(pattern=r"oke$")
async def emoji_oke(e):
    emoji = e.pattern_match.group(1)
    oke = GAMBAR_OK
    if emoji:
        oke = oke.replace('😂', emoji)
    await e.edit(oke)


@ilhammansiz_cmd(pattern=r"skull$")
async def emoji_tengkorak(e):
    emoji = e.pattern_match.group(1)
    tengkorak = GAMBAR_TENGKORAK
    if emoji:
        tengkorak = tengkorak.replace('😂', emoji)
    await e.edit(tengkorak)


