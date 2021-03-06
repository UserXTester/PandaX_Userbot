"""

β’πΎπ€π’π’ππ£π: `{i}circle`
   Balas ke audio lagu atau gif untuk mendapatkan catatan video.
β’πΎπ€π’π’ππ£π: `{i}ls`
   Dapatkan semua file di dalam direktori.
   
β’πΎπ€π’π’ππ£π: `{i}bots`
   Menunjukkan jumlah bot dalam obrolan saat ini dengan tautan permanen mereka.
β’πΎπ€π’π’ππ£π: `{i}hl <a link>`
   Sematkan tautan dengan spasi putih sebagai pesan.
β’πΎπ€π’π’ππ£π: `{i}id`
   Balas ke stiker untuk mendapatkan id nya.
   Balas ke pengguna untuk mendapatkan id nya.
   Dapatkan id obrolan tanpa harus membalas ke pesan.
β’πΎπ€π’π’ππ£π: `{i}sg <balas ke pengguna><username/id>`
   Dapatkan histori nama dari pengguna yang dibalas.
β’πΎπ€π’π’ππ£π: `{i}tr <kode bahasa> <(balas ke) pesan>`
   Terjemahkan kalimat kedalam bahasa yang ditentukan.
"""

import os
import time
from asyncio.exceptions import TimeoutError
from pathlib import Path

import cv2
from googletrans import Translator
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots
from telethon.tl.types import DocumentAttributeVideo as video
from telethon.utils import pack_bot_file_id

from . import *
from . import humanbytes as hb


@ilhammansiz_cmd(
    pattern="tr",
)
async def _(event):
    if len(event.text) > 3:
        if not event.text[3] == " ":
            return
    input = event.text[4:6]
    txt = event.text[7:]
    xx = await eor(event, "`menerjemahkan...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input or "en"
    elif input:
        text = txt
        lan = input or "en"
    else:
        return await eod(
            xx, f"`{hndlr}tr (kode bahasa)` dengan cara balas ke pesan.", time=5
        )
    translator = Translator()
    try:
        tt = translator.translate(text, dest=lan)
        output_str = f"**diterjemahkan** dari {tt.src} ke {lan}\n{tt.text}"
        await eor(xx, output_str)
    except Exception as exc:
        await eod(xx, str(exc), time=10)


@ilhammansiz_cmd(
    pattern="id ?(.*)",
)
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await eor(
                event,
                "**ID OBROLAN:**  `{}`\n**ID PENGGUNA:**  `{}`\n**BOT API FILE ID:**  `{}`".format(
                    str(event.chat_id),
                    str(r_msg.sender_id),
                    bot_api_file_id,
                ),
            )
        else:
            await eor(
                event,
                "**ID OBROLAN:**  `{}`\n**ID PENGGUNA:**  `{}`".format(
                    str(event.chat_id),
                    str(r_msg.sender_id),
                ),
            )
    elif event.pattern_match.group(1):
        ids = await get_user_id(event.pattern_match.group(1))
        return await eor(
            event,
            "**ID OBROLAN:**  `{}`\n**ID PENGGUNA:**  `{}`".format(
                str(event.chat_id),
                str(ids),
            ),
        )
    else:
        await eor(event, "**ID OBROLAN SAAT INI:**  `{}`".format(str(event.chat_id)))


@ilhammansiz_cmd(
    pattern="bots ?(.*)",
)
async def _(ult):
    await ult.edit("`proses...`")
    if ult.is_private:
        user = await ult.get_chat()
        if not user.bot:
            return await ult.edit("`anda yakin ?`")

    mentions = "**bot didalam obrolan ini**: \n"
    input_str = ult.pattern_match.group(1)
    to_write_chat = await ult.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions = f"**list bot di **{input_str}: \n"
        try:
            chat = await petercordpanda_bot.get_entity(input_str)
        except Exception as e:
            await eor(ult, str(e))
            return None
    try:
        async for x in petercordpanda_bot.iter_participants(
            chat,
            filter=ChannelParticipantsBots,
        ):
            if isinstance(x.participant, ChannelParticipantAdmin):
                mentions += "\n πΌ [{}](tg://user?id={}) `{}`".format(
                    x.first_name,
                    x.id,
                    x.id,
                )
            else:
                mentions += "\n [{}](tg://user?id={}) `{}`".format(
                    x.first_name,
                    x.id,
                    x.id,
                )
    except Exception as e:
        mentions += " " + str(e) + "\n"
    await eor(ult, mentions)


@ilhammansiz_cmd(
    pattern="hl",
)
async def _(ult):
    try:
        input = ult.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await eod(ult, "`masukkan beberapa tautan..`", time=5)
    await eor(ult, "[γ€γ€γ€γ€γ€γ€γ€](" + input + ")", link_preview=False)


@ilhammansiz_cmd(
    pattern="circle$",
)
async def _(e):
    a = await e.get_reply_message()
    if a is None:
        return await eor(e, "balas ke gif atau audio")
    if a.document and a.document.mime_type == "audio/mpeg":
        z = await eor(e, "**α΄α΄α΄Κα΄α΄α΄ Ι΄α΄α΄α΄ α΄ Ιͺα΄α΄α΄...**")
        toime = time.time()
        try:
            bbbb = await a.download_media(thumb=-1)
            im = cv2.imread(bbbb)
            dsize = (320, 320)
            output = cv2.resize(im, dsize, interpolation=cv2.INTER_AREA)
            cv2.imwrite("img.png", output)
            thumb = "img.png"
            os.remove(bbbb)
        except TypeError:
            bbbb = "resources/extras/petercordpanda.jpg"
            im = cv2.imread(bbbb)
            dsize = (320, 320)
            output = cv2.resize(im, dsize, interpolation=cv2.INTER_AREA)
            cv2.imwrite("img.png", output)
            thumb = "img.png"
        c = await downloader(
            "resources/downloads/" + a.file.name,
            a.media.document,
            z,
            toime,
            "α΄α΄Ι΄Ι’α΄Ι΄α΄α΄Κ...",
        )
        await z.edit("**α΄Ιͺα΄Ι΄α΄α΄Κ...\nsα΄α΄α΄Κα΄Ι΄Ι’ α΄α΄Ι΄Ι’α΄α΄Ι΄α΄ α΄ΚsΙͺ...**")
        await bash(
            f'ffmpeg -i "{c.name}" -preset ultrafast -acodec libmp3lame -ac 2 -ab 144 -ar 44100 comp.mp3'
        )
        await bash(
            f'ffmpeg -y -i "{thumb}" -i comp.mp3 -preset ultrafast -c:a copy circle.mp4'
        )
        taime = time.time()
        foile = await uploader("circle.mp4", "circle.mp4", taime, z, "α΄α΄Ι΄Ι’α΄α΄Κα΄α΄α΄...")
        metadata = extractMetadata(createParser("circle.mp4"))
        duration = metadata.get("duration").seconds
        attributes = [video(duration=duration, w=320, h=320, round_message=True)]
        await e.client.send_file(
            e.chat_id,
            foile,
            thumb=thumb,
            reply_to=a,
            attributes=attributes,
        )
        await z.delete()
        os.system("rm resources/downloads/*")
        os.system("rm circle.mp4 comp.mp3 img.png")
    elif a.document and a.document.mime_type == "video/mp4":
        z = await eor(e, "**α΄α΄α΄Κα΄α΄α΄ α΄ Ιͺα΄α΄α΄ Ι΄α΄α΄α΄...**")
        c = await a.download_media("resources/downloads/")
        await e.client.send_file(
            e.chat_id,
            c,
            video_note=True,
            thumb="resources/extras/petercordpanda.jpg",
            reply_to=a,
        )
        await z.delete()
        os.remove(c)
    else:
        return await eor(e, "**balas ke gif atau file audio saja.**")


@ilhammansiz_cmd(
    pattern="ls ?(.*)",
)
async def _(e):
    path = Path(e.pattern_match.group(1))
    if not path:
        path = Path(".")
    else:
        if not os.path.isdir(path):
            return await eod(e, "`direktori salah.`")
        if not os.listdir(path):
            return await eod(e, "`direktori ini kosong.`")
    files = path.iterdir()
    pyfiles = []
    jsons = []
    vdos = []
    audios = []
    pics = []
    others = []
    otherfiles = []
    folders = []
    text = []
    apk = []
    exe = []
    zip_ = []
    book = []
    for file in sorted(files):
        if os.path.isdir(file):
            folders.append("π " + str(file))
        elif str(file).endswith(".py"):
            pyfiles.append("π " + str(file))
        elif str(file).endswith(".json"):
            jsons.append("π? " + str(file))
        elif str(file).endswith((".mkv", ".mp4", ".avi", ".gif")):
            vdos.append("π₯ " + str(file))
        elif str(file).endswith((".mp3", ".ogg", ".m4a")):
            audios.append("π " + str(file))
        elif str(file).endswith((".jpg", ".jpeg", ".png", ".webp")):
            pics.append("πΌ " + str(file))
        elif str(file).endswith((".txt", ".text", ".log")):
            text.append("π " + str(file))
        elif str(file).endswith((".apk", ".xapk")):
            apk.append("π² " + str(file))
        elif str(file).endswith(".exe"):
            exe.append("β " + str(file))
        elif str(file).endswith((".zip", ".rar")):
            zip_.append("π " + str(file))
        elif str(file).endswith((".pdf", ".epub")):
            book.append("π " + str(file))
        elif "." in str(file)[1:]:
            others.append("π· " + str(file))
        else:
            otherfiles.append("π " + str(file))
    omk = [
        *sorted(folders),
        *sorted(pyfiles),
        *sorted(jsons),
        *sorted(zip_),
        *sorted(vdos),
        *sorted(pics),
        *sorted(audios),
        *sorted(apk),
        *sorted(exe),
        *sorted(book),
        *sorted(text),
        *sorted(others),
        *sorted(otherfiles),
    ]
    text = ""
    fls, fos = 0, 0
    flc, foc = 0, 0
    for i in omk:
        emoji = i.split()[0]
        name = i.split(maxsplit=1)[1]
        nam = name.split("/")[-1]
        if os.path.isdir(name):
            size = 0
            for path, dirs, files in os.walk(name):
                for f in files:
                    fp = os.path.join(path, f)
                    size += os.path.getsize(fp)
            if hb(size):
                text += emoji + f" `{nam}`" + "  `" + hb(size) + "`\n"
                fos += size
            else:
                text += emoji + f" `{nam}`" + "\n"
            foc += 1
        else:
            if hb(int(os.path.getsize(name))):
                text += (
                    emoji + f" `{nam}`" + "  `" + hb(int(os.path.getsize(name))) + "`\n"
                )
                fls += int(os.path.getsize(name))
            else:
                text += emoji + f" `{nam}`" + "\n"
            flc += 1
    tfos, tfls, ttol = hb(fos), hb(fls), hb(fos + fls)
    if not hb(fos):
        tfos = "0 B"
    if not hb(fls):
        tfls = "0 B"
    if not hb(fos + fls):
        ttol = "0 B"
    text += f"\n\n`Folders` :  `{foc}` :   `{tfos}`\n`Files` :       `{flc}` :   `{tfls}`\n`Total` :       `{flc+foc}` :   `{ttol}`"
    await eor(e, text)


@ilhammansiz_cmd(
    pattern="sa ?(.*)",
)
async def lastname(steal):
    mat = steal.pattern_match.group(1)
    if not (steal.is_reply or mat):
        await eor(
            steal,
            "`gunakan perintah ini dengan membalas ke pesan atau berikan id/username pengguna...`",
        )
        return
    if mat:
        user_id = await get_user_id(mat)
    message = await steal.get_reply_message()
    if message:
        user_id = message.sender.id
    chat = "@SangMataInfo_bot"
    id = f"/search_id {user_id}"
    lol = await eor(steal, "`memproses...`")
    try:
        async with petercordpanda_bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                response = await conv.get_response()
                respond = await conv.get_response()
                responds = await conv.get_response()
            except YouBlockedUserError:
                await lol.edit("mohon unblock @sangmatainfo_bot lalu coba lagi.")
                return
            if (
                response.text.startswith("tidak ada rekaman nama yang ditemukan.")
                or respond.text.startswith("tidak ada rekaman nama yang ditemukan.")
                or responds.text.startswith("tidak ada rekaman nama yang ditemukan.")
            ):
                await lol.edit(
                    "tidak ada rekaman nama yang ditemukan dari pengguna ini"
                )
                await steal.client.delete_messages(conv.chat_id, [msg.id, response.id])
                return
            else:
                if response.text.startswith("π"):
                    await lol.edit(respond.message)
                    await lol.reply(responds.message)
                elif respond.text.startswith("π"):
                    await lol.edit(response.message)
                    await lol.reply(responds.message)
                else:
                    await lol.edit(respond.message)
                    await lol.reply(response.message)
            await steal.client.delete_messages(
                conv.chat_id,
                [msg.id, responds.id, respond.id, response.id],
            )
    except TimeoutError:
        return await lol.edit("error: @SangMataInfo_bot tidak merespon.")
