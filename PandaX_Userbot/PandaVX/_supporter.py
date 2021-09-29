import inspect
import os
import re
from pathlib import Path

from PandaX_v20 import *
from telethon import events, types

from PandaX_Userbot.PandaVX._decorators import *
from PandaX_Userbot.PandaVX._wrappers import eod, eor

from .. import udB, petercordpanda_bot, LOGSPAMMER
from ..Panda.core import LIST
from ..Panda.database import Var
from speedtest import Speedtest


IG_ALIVE = "instagram.com/imansiez77"
GROUP_LINK = "t.me/TeamSquadUserbotSupport"
EMOJI_HELP = "🐼"
REPO_NAME = "PandaToxic_Kentot"
ALIVE_LOGO = udB.get("ALIVE_PIC")
CMD_HELP = {}
ALIVE_NAME = petercordpanda_bot.me.first_name
BOTLOG = int(udB.get("LOG_CHANNEL"))
BOTLOG_CHATID = int(udB.get("LOG_CHANNEL"))
TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TEMP_DOWNLOAD_DIRECTORY", "PandaVersion/downloads/"
        )
G_BAN_LOGGER_GROUP = int(udB.get("LOG_CHANNEL"))
HEROKU_APP_NAME = Var.HEROKU_APP_NAME
HEROKU_API_KEY = Var.HEROKU_API
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
CHROME_DRIVER = os.environ.get(
            "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
        )
GOOGLE_CHROME_BIN = os.environ.get(
            "GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome"
        )
BOTVER = "PandaX_Userbot"
 
ultroid_bot = petercordpanda_bot
bot = petercordpanda_bot
borg = petercordpanda_bot
friday = petercordpanda_bot
jarvis = petercordpanda_bot


hndlr = "\\" + HNDLR


def admin_cmd(pattern=None, command=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    args["chats"] = black_list_chats
    args["blacklist_chats"] = True
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    if pattern is not None:
        if pattern.startswith(r"\#"):
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(hndlr + pattern)
        reg = re.compile("(.*)")
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = (
                    cmd.group(1)
                    .replace("$", "")
                    .replace("?(.*)", "")
                    .replace("(.*)", "")
                    .replace("(?: |)", "")
                    .replace("| ", "")
                    .replace("( |)", "")
                    .replace("?((.|//)*)", "")
                    .replace("?P<shortname>\\w+", "")
                )
            except BaseException:
                pass
            try:
                LIST[file_test].append(cmd)
            except BaseException:
                LIST.update({file_test: [cmd]})
        except BaseException:
            pass
    args["outgoing"] = True
    if "incoming" in args and not args["incoming"]:
        args["outgoing"] = True
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]
    return events.NewMessage(**args)


friday_on_cmd = admin_cmd
j_cmd = admin_cmd
command = ilhammansiz_cmd
ultroid_cmd = ilhammansiz_cmd
geezbot_cmd = admin_cmd


def sudo_cmd(allow_sudo=True, pattern=None, command=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    args["chats"] = black_list_chats
    args["blacklist_chats"] = True
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    if pattern is not None:
        if pattern.startswith(r"\#"):
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(hndlr + pattern)
    if allow_sudo:
        args["from_users"] = [int(user) for user in sudoers()]
        args["incoming"] = True
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]
    return events.NewMessage(**args)



def register(**args):
    """ Register a new event. """
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', False)
    ignore_unsafe = args.get('ignore_unsafe', False)
    unsafe_pattern = r'^[^/!#@\$A-Za-z]'
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    disable_errors = args.get('disable_errors', False)
    insecure = args.get('insecure', False)

    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern

    if "disable_edited" in args:
        del args['disable_edited']

    if "ignore_unsafe" in args:
        del args['ignore_unsafe']

    if "groups_only" in args:
        del args['groups_only']

    if "disable_errors" in args:
        del args['disable_errors']

    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']

    if "insecure" in args:
        del args['insecure']

    if pattern:
        if not ignore_unsafe:
            args['pattern'] = pattern.replace('^.', unsafe_pattern, 1)

    def decorator(func):
        async def wrapper(check):
            if check.edit_date and check.is_channel and not check.is_group:
                # Messages sent in channels can be edited by other users.
                # Ignore edits that take place in channels.
                return
            if not LOGSPAMMER:
                check.chat_id
            else:
                pass

            if not trigger_on_fwd and check.fwd_from:
                return

            if groups_only and not check.is_group:
                await check.respond("`I don't think this is a group.`")
                return

            if check.via_bot_id and not insecure and check.out:
                return

            try:
                await func(check)

            # Thanks to @kandnub for this HACK.
            # Raise StopPropagation to Raise StopPropagation
            # This needed for AFK to working properly

            except events.StopPropagation:
                raise events.StopPropagation
            # This is a gay exception and must be passed out. So that it doesnt
            # spam chats
            except KeyboardInterrupt:
                pass
            except BaseException:

                # Check if we have to disable it.
                # If not silence the log spam on the console,
                # with a dumb except.

                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**PandaX_Userbot ERROR**\n"
                    link = "Silahkan chat: @bismillahselaluadaa"
                    text += "Untuk melaporkan kesalahan"
                    text += f"tinggal teruskan pesan ini {link}.\n"
                    text += "Ilham Mansiez Siap Membantu Kamu\n"

                    ftext = "========== DISCLAIMER =========="
                    ftext += "\nThis file uploaded ONLY here,"
                    ftext += "\nwe logged only fact of error and date,"
                    ftext += "\nwe respect your privacy,"
                    ftext += "\nyou may not report this error if you've"
                    ftext += "\nany confidential data here, no one will see your data\n"
                    ftext += "================================\n\n"
                    ftext += "--------BEGIN USERBOT TRACEBACK LOG--------\n"
                    ftext += "\nDate: " + date
                    ftext += "\nChat ID: " + str(check.chat_id)
                    ftext += "\nSender ID: " + str(check.sender_id)
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

                    command = "git log --pretty=format:\"%an: %s\" -10"

                    ftext += "\n\n\nLast 10 commits:\n"

                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("error.log", "w+")
                    file.write(ftext)
                    file.close()

            else:
                pass

        if not disable_edited:
            petercordpanda_bot.add_event_handler(wrapper, events.MessageEdited(**args))
        petercordpanda_bot.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper
    return decorator


edit_or_reply = eor
edit_delete = eod


ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os

    class Config(object):
        LOGGER = True
        LOCATION = os.environ.get("LOCATION", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
            "SCREEN_SHOT_LAYER_ACCESS_KEY", None
        )
        SUDO_COMMAND_HAND_LER = hndlr
        TMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TMP_DOWNLOAD_DIRECTORY", "PandaVersion/downloads/"
        )
        TEMP_DOWNLOAD_DIRECTORY = TMP_DOWNLOAD_DIRECTORY
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Ultroid")
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        G_BAN_LOGGER_GROUP = int(udB.get("LOG_CHANNEL"))
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        TG_BOT_TOKEN_BF_HER = Var.BOT_TOKEN
        TG_BOT_USER_NAME_BF_HER = asst.me.username
        DUAL_LOG = os.environ.get("DUAL_LOG", None)
        MAX_MESSAGE_SIZE_LIMIT = 4095
        UB_BLACK_LIST_CHAT = [
            int(blacklist) for blacklist in udB.get("BLACKLIST_CHATS")
        ]
        MAX_ANTI_FLOOD_MESSAGES = 10
        ANTI_FLOOD_WARN_MODE = types.ChatBannedRights(
            until_date=None, view_messages=None, send_messages=True
        )
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
        PM_LOG_GRP_ID = os.environ.get("PM_LOG_GRP_ID", None)
        NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", True))
        HEROKU_APP_NAME = Var.HEROKU_APP_NAME
        HEROKU_API_KEY = Var.HEROKU_API
        PRIVATE_GROUP_BOT_API_ID = int(udB.get("LOG_CHANNEL"))
        PM_LOGGR_BOT_API_ID = int(udB.get("LOG_CHANNEL"))
        DB_URI = os.environ.get("DATABASE_URL", None)
        NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 7)
        )
        NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 3)
        )
        EMOJI_TO_DISPLAY_IN_HELP = os.environ.get("EMOJI_TO_DISPLAY_IN_HELP", "🔰")
        HANDLR = hndlr
        SUDO_USERS = sudos
        GROUP_REG_SED_EX_BOT_S = os.environ.get(
            "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
        )
        TEMP_DIR = os.environ.get("TEMP_DIR", None)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        CHROME_DRIVER = os.environ.get(
            "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
        )
        GOOGLE_CHROME_BIN = os.environ.get(
            "GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome"
        )
        BLACKLIST_CHAT = UB_BLACK_LIST_CHAT
        MONGO_URI = os.environ.get("MONGO_URI", None)
        ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)
        ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
        ALIVE_MSG = os.environ.get("ALIVE_MSG", None)
        DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
        BIO_MSG = os.environ.get("BIO_MSG", None)
        LYDIA_API = os.environ.get("LYDIA_API", None)
        PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -69))
        PM_DATA = os.environ.get("PM_DATA", "ENABLE")
        DEEP_AI = os.environ.get("DEEP_AI", None)
        TAG_LOG = os.environ.get("TAG_LOG", None)


else:

    class Config(object):
        DB_URI = None


CMD_HNDLR = HNDLR
