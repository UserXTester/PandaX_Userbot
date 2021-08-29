# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import os

from PandaX_Userbot import LOGS
from PandaX_Userbot.utils import (
    load_modules,
    load_assistant,
    load_manager,
    load_plugins,
    load_panda,
    load_pmbot,
    load_vc,
)


def plugin_loader(modules=None, pmbot=None, manager=None, vcbot=None):
    # for userbot
    files = sorted(os.listdir("PandaX_v20"))
    for plugin_name in files:
        try:
            if plugin_name.endswith(".py"):
                load_plugins(plugin_name[:-3])
                LOGS.info(f"Panda - Official -  Installed - {plugin_name}")
        except Exception as exc:
            LOGS.info(f"Panda - Official - ERROR - {plugin_name}")
            LOGS.info(str(type(exc)) + ": " + str(exc))
    LOGS.info("-" * 70)

   # for userbot
    files = sorted(os.listdir("Panda-Userbot"))
    for plugin_name in files:
        try:
            if plugin_name.endswith(".py"):
                load_plugins(plugin_name[:-3])
                LOGS.info(f"Panda - Official -  Installed - {plugin_name}")
        except Exception as exc:
            LOGS.info(f"Panda - Official - ERROR - {plugin_name}")
            LOGS.info(str(type(exc)) + ": " + str(exc))
    LOGS.info("-" * 70)

    # for assistant
    files = sorted(os.listdir("PandaX_ASsistant"))
    for plugin_name in files:
        try:
            if plugin_name.endswith(".py"):
                load_assistant(plugin_name[:-3])
                LOGS.info(f"Panda - Assistant -  Installed - {plugin_name}")
        except Exception as exc:
            LOGS.info(f"Panda - Assistant - ERROR - {plugin_name}")
            LOGS.info(str(type(exc)) + ": " + str(exc))
    LOGS.info("-" * 70)

    # for modulwa
    if modules == "True" or not modules:
        try:
            os.system(
                "git clone https://github.com/ilhammansiz/PandaX_UserbotModules.git modules/"
            )
        except BaseException:
            pass
        """
        LOGS.info("Installing packages for modules")
        os.system("pip install -r modules/modules.txt")
        """
        files = sorted(os.listdir("modules"))
        for plugin_name in files:
            try:
                if plugin_name.endswith(".py"):
                    load_modules(plugin_name[:-3])
                    LOGS.info(f"Panda - Modules -  Installed - {plugin_name}")
            except Exception as exc:
                LOGS.info(f"Panda - Modules - ERROR - {plugin_name}")
                LOGS.info(str(type(exc)) + ": " + str(exc))
        LOGS.info("-" * 70)
    else:
        pass
        # os.system("cp PandaX_v20/__init__.py modules/")

    # group manager
    if manager == "True":
        files = sorted(os.listdir("PandaX_ASsistant/PandaSX_userbot"))
        for plugin_name in files:
            if plugin_name.endswith(".py"):
                load_manager(plugin_name[:-3])
                LOGS.info(f"Panda - Group Manager - Installed - {plugin_name}.")
        LOGS.info("-" * 70)

    # chat via assistant
    if pmbot == "True":
        files = sorted(os.listdir("PandaX_ASsistant/pmbot"))
        for plugin_name in files:
            if plugin_name.endswith(".py"):
                load_pmbot(plugin_name[:-3])
        LOGS.info(f"Panda - PM Bot Message Forwards - Enabled.")
        LOGS.info("-" * 70)

    # vc bot
    if vcbot:
        files = sorted(os.listdir("PandaX_v21"))
        for plugin_name in files:
            if plugin_name.endswith(".py"):
                load_vc(plugin_name[:-3])
            if not plugin_name.startswith("_"):
                LOGS.info(f"Panda - VC Bot - Installed - {plugin_name}.")
        LOGS.info("-" * 70)
