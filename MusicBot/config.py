# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

from PandaX_Userbot import udB
from PandaX_v20 import *
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = udB.get("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TeamSquadUserbotSupport")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/695cb726224d2a7037399.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = asst.me.username
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PandaX-MusicBot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "TeamSquadUserbotSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "PandaX-MusicBot")
OWNER = getenv("OWNER", "@diemmmmmmmmmm")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ilhammansiz/PandaX_Userbot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "TTKQOS-COPDKW-QMRNEW-WLXGOE-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
