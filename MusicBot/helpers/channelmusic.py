from telethon.tl.custom import Message


def get_chat_id(chat: Message):
    if chat.title.startswith("Channel Music: ") and chat.title[16:].isnumeric():
        return int(chat.title[15:])
    return chat.id
