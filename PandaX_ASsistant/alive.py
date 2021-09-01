from datetime import datetime


@asst_cmd("alive$")
@owner
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asst.send_message(
        event.chat_id,
        f"➔ Version : V-Mansiez.2021\n➔ Uptime : {ms}\n➔ Telethon Version : 3.98\n➔ Python Version : 3.9.2\n➔ OS : Linux\n➔ CPU : 8\n➔ Branch : PandaUserbot\n➔ Repo : [PandaXUserbot](https://github.com/ilhammansiz/PandaX_Userbot)",
      )






