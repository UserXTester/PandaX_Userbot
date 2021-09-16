# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

from safety.tools import *

from .PandaX.PandaStart import *

LOGS = LOGS

udB = redis_connection()

ultroid_bot, asst = client_connection()

vcClient = vc_connection(udB, ultroid_bot)

if not udB.get("HNDLR"):
    udB.set("HNDLR", ".")

if not udB.get("SUDO"):
    udB.set("SUDO", "False")

if not udB.get("SUDOS"):
    udB.set("SUDOS", "777000")

if not udB.get("BLACKLIST_CHATS"):
    udB.set("BLACKLIST_CHATS", "[]")

HNDLR = udB.get("HNDLR")

if not udB.get("DUAL_HNDLR"):
    udB.set("DUAL_HNDLR", "/")

Evar = udB.get("SUDO_HNDLR")
SUDO_HNDLR = Evar if Evar else HNDLR

Hosted_On = where_hosted()

import os
import time
from distutils.util import strtobool as sb

StartTime = time.time()

TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./downloads")
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
CMD_HELP = {}
DB_URI = os.environ.get("DATABASE_URL", None)
CUSTOM_CMD = os.environ.get("CUSTOM_CMD") or "."
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
G_BAN_LOGGER_GROUP = int(udB.get("LOG_CHANNEL"))
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(udB.get("LOG_CHANNEL"))


