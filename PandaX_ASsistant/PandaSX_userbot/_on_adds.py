
from . import *


@asst.on(events.ChatAction())
async def dueha(e):
    if not e.user_added:
        return
    user = await e.get_user()
    if not user.is_self:
        return
    sm = udB.get("ON_MNGR_ADD")
    if sm == "OFF":
        return
    if not sm:
        sm = "Thanks for Adding me :)"
    await e.reply(sm, link_preview=False)
