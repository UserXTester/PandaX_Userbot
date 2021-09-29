from googletrans import Translator, LANGUAGES

Tr = "id"

@asst_cmd("tr")
@owner
async def _(e):
    Translator()
    if not event.is_private:
        return
    x = await event.get_reply_message()
    if x is None:
        return await e.reply("**Beri saya kata atau balas agar saya dapat menerjemahkannya**")
    try:
        reply_text = await getTranslate(deEmojify(message), dest=Tr)
    except ValueError:
        await e.reply("** Kode bahasa salah !**")
        return
    source_lan = LANGUAGES[f"{reply_text.src.lower()}"]
    transl_lan = LANGUAGES[f"{reply_text.dest.lower()}"]
    reply_text = f"⌔∮ **Diterjemahkan dari {source_lan.title()}({reply_text.src.lower()}) الى {transl_lan.title()}({reply_text.dest.lower()}) :**\n  - {reply_text.text}"
    await e.reply(reply_text)

async def getTranslate(text, **kwargs):
    translator = Translator()
    result = None
    for _ in range(10):
        try:
            result = translator.translate(text, **kwargs)
        except Exception:
            translator = Translator()
            await sleep(0.1)
    return result
