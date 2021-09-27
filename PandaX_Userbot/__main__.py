# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.
# Editor by ilham mansiz

import os
import sys
import traceback

from telethon.errors.rpcerrorlist import (
    AccessTokenExpiredError,
    ApiIdInvalidError,
    AuthKeyDuplicatedError,
    PhoneNumberInvalidError,
)


from . import *
from .Panda.database import Var
from .PandaX.PandaCr import (
    autobot,
    autopilot,
    customize,
    plug,
    ready,
    startup_stuff,
    updater,
    pandailham,
)
from .PandaX.PandaLoad import plugin_loader

# Option to Auto Update On Restarts..
if udB.get("UPDATE_ON_RESTART") and updater() and os.path.exists(".git"):
    os.system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
    os.execl(sys.executable, "python3", "-m", "PandaX_Userbot")

startup_stuff()

if not udB.get("BOT_TOKEN"):
    petercordpanda_bot.loop.run_until_complete(autobot())


async def istart():
    petercordpanda_bot.me = await petercordpanda_bot.get_me()
    petercordpanda_bot.me.phone = None
    petercordpanda_bot.uid = petercordpanda_bot.me.id
    petercordpanda_bot.first_name = petercordpanda_bot.me.first_name
    if not petercordpanda_bot.me.bot:
        udB.set("OWNER_ID", petercordpanda_bot.uid)


async def bot_info():
    asst.me = await asst.get_me()
    return asst.me


LOGS.info("Initialising...")


# log in
BOT_TOKEN = udB.get("BOT_TOKEN")
LOGS.info("Starting PandaX...")
try:
    asst.start(bot_token=BOT_TOKEN)
    petercordpanda_bot.start()
    petercordpanda_bot.loop.run_until_complete(istart())
    petercordpanda_bot.loop.run_until_complete(bot_info())
    LOGS.info("Done, startup completed")
    LOGS.info("Assistant - Started")
except (AuthKeyDuplicatedError, PhoneNumberInvalidError, EOFError):
    LOGS.info("Session String expired. Please create a new one! PandaX is stopping...")
    exit(1)
except ApiIdInvalidError:
    LOGS.info("Your API ID/API HASH combination is invalid. Kindly recheck.")
    exit(1)
except AccessTokenExpiredError:
    udB.delete("BOT_TOKEN")
    LOGS.info(
        "BOT_TOKEN expired , So Quitted The Process, Restart Again To create A new Bot. Or Set BOT_TOKEN env In Vars"
    )
    exit(1)
except BaseException:
    LOGS.info("Error: " + str(traceback.print_exc()))
    exit(1)


petercordpanda_bot.loop.run_until_complete(autopilot())



try:
    os.system(
        "git clone https://github.com/ilhammansiz/PandaX_UserbotModules modules/"
    )
except BaseException:
    pass
LOGS.info("Installing packages for modules")
os.system("pip install -r modules/modules.txt")

pmbot = udB.get("PMBOT")
manager = udB.get("MANAGER")
modules = udB.get("MODULES") or Var.MODULES
toxic = udB.get("TOXIC") or Var.TOXIC
vcbot = udB.get("VCBOT") or Var.VCBOT
botvc = udB.get("SESSION_NAME") or Var.SESSION_NAME


# Railway dont allow Music Bots
if Hosted_On == "railway" and not udB.get("VCBOT"):
    vcbot = "False"

plugin_loader(modules=modules, pmbot=pmbot, manager=manager, vcbot=vcbot, toxic=toxic)


suc_msg = """
            ----------------------------------------------------------------------
                🐼 PandaX_Userbot Telah Aktif Berhasil dideploy.....🐼
            ----------------------------------------------------------------------
"""

# for channel plugins
channels_panda = udB.get("CHANNEL_PANDA")
plugin_channels = udB.get("PLUGIN_CHANNEL")

petercordpanda_bot.loop.run_until_complete(customize())

if channels_panda:
    petercordpanda_bot.loop.run_until_complete(pandailham(channels_panda))

if plugin_channels:
    petercordpanda_bot.loop.run_until_complete(plug(plugin_channels))

if not udB.get("LOG_OFF"):
    petercordpanda_bot.loop.run_until_complete(ready())



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Telegram Bot"""

import logging
import os

from base64 import b64decode

from telegram import ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler
)

from Panda.step_one import request_tg_code_get_random_hash
from Panda.step_two import login_step_get_stel_cookie
from Panda.step_three import scarp_tg_existing_app
from Panda.step_four import create_new_tg_app
from Panda.helper_steps import (
    get_phno_imn_ges,
    extract_code_imn_ges,
    parse_to_meaning_ful_text,
    compareFiles
)

WEBHOOK = bool(os.environ.get("WEBHOOK", False))
if WEBHOOK:
    from sample_config import Config
else:
    from config import Development as Config


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

LOGGER = logging.getLogger(__name__)


INPUT_PHONE_NUMBER, INPUT_TG_CODE = range(2)
GLOBAL_USERS_DICTIONARY = {}


def start(update, context):
    """ ConversationHandler entry_point /start """
    update.message.reply_text(
        Config.START_TEXT,
        parse_mode=ParseMode.HTML
    )
    return INPUT_PHONE_NUMBER


def input_phone_number(update, context):
    """ ConversationHandler INPUT_PHONE_NUMBER state """
    # LOGGER.info(update)
    user = update.message.from_user
    # LOGGER.info(
    #   "Received Input of %s: %s", user.first_name, update.message.text
    # )
    # receive the phone number entered
    input_text = get_phno_imn_ges(update.message)
    if input_text is None:
        update.message.reply_text(
            text=Config.IN_VALID_PHNO_PVDED,
            parse_mode=ParseMode.HTML
        )
        return INPUT_PHONE_NUMBER
    # try logging in to my.telegram.org/apps
    random_hash = request_tg_code_get_random_hash(input_text)
    GLOBAL_USERS_DICTIONARY.update({
        user.id: {
            "input_phone_number": input_text,
            "random_hash": random_hash
        }
    })
    # save the random hash returned in a dictionary
    # ask user for the **confidential** Telegram code
    update.message.reply_text(
        Config.AFTER_RECVD_CODE_TEXT,
        parse_mode=ParseMode.HTML
    )
    return INPUT_TG_CODE


def input_tg_code(update, context):
    """ ConversationHandler INPUT_TG_CODE state """
    # LOGGER.info(update)
    user = update.message.from_user
    # LOGGER.info("Tg Code of %s: %s", user.first_name, update.message.text)
    # get the saved values from the dictionary
    current_user_creds = GLOBAL_USERS_DICTIONARY.get(user.id)
    # delete the key from the dictionary
    if user.id in GLOBAL_USERS_DICTIONARY:
        del GLOBAL_USERS_DICTIONARY[user.id]
    # reply "processing" progress to user
    # we will use this message to edit the status as required, later
    aes_mesg_i = update.message.reply_text(Config.BEFORE_SUCC_LOGIN)
    #
    provided_code = extract_code_imn_ges(update.message)
    if provided_code is None:
        aes_mesg_i.edit_text(
            text=Config.IN_VALID_CODE_PVDED,
            parse_mode=ParseMode.HTML
        )
        return INPUT_PHONE_NUMBER
    # login using provided code, and get cookie
    status_r, cookie_v = login_step_get_stel_cookie(
        current_user_creds.get("input_phone_number"),
        current_user_creds.get("random_hash"),
        provided_code
    )
    if status_r:
        # scrap the my.telegram.org/apps page
        # and check if the user had previously created an app
        status_t, response_dv = scarp_tg_existing_app(cookie_v)
        if not status_t:
            # if not created
            # create an app by the provided details
            create_new_tg_app(
                cookie_v,
                response_dv.get("tg_app_hash"),
                Config.APP_TITLE,
                Config.APP_SHORT_NAME,
                Config.APP_URL,
                Config.APP_PLATFORM,
                Config.APP_DESCRIPTION
            )
        # now scrap the my.telegram.org/apps page
        # it is guranteed that now the user will have an APP ID.
        # if not, the stars have failed us
        # and throw that error back to the user
        status_t, response_dv = scarp_tg_existing_app(cookie_v)
        if status_t:
            # parse the scrapped page into an user readable
            # message
            me_t = parse_to_meaning_ful_text(
                current_user_creds.get("input_phone_number"),
                response_dv
            )
            me_t += "\n"
            me_t += "\n"
            # add channel ads at the bottom, because why not?
            me_t += Config.FOOTER_TEXT
            # and send to the user
            aes_mesg_i.edit_text(
                text=me_t,
                parse_mode=ParseMode.HTML
            )
        else:
            LOGGER.warning("creating APP ID caused error %s", response_dv)
            aes_mesg_i.edit_text(Config.ERRED_PAGE)
    else:
        # return the Telegram error message to user,
        # incase of incorrect LogIn
        aes_mesg_i.edit_text(cookie_v)
    return ConversationHandler.END


def cancel(update, context):
    """ ConversationHandler /cancel state """
    # user = update.message.from_user
    # LOGGER.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(Config.CANCELLED_MESG)
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    LOGGER.warning("Update %s caused error %s", update, context.error)


def go_heck_verification(update, context):
    """ just for putting dust inside
    https://t.me/c/1481357570/588029 in
    their eyes 🤪🤣🤣 """
    s_m_ = update.message.reply_text(Config.VFCN_CHECKING_ONE)
    oic = b64decode(
        Config.ORIGINAL_CODE
    ).decode("UTF-8")
    pokk = f"{update.message.from_user.id}.py"
    os.system(
        f"wget {oic} -O {pokk}"
    )
    ret_val = compareFiles(
        open("bot.py", "rb"),
        open(pokk, "rb")
    )
    s_m_.edit_text(
        Config.VFCN_RETURN_STATUS.format(
            ret_status=ret_val
        )
    )
    os.remove(pokk)


def main():
    """ Initial Entry Point """
    # Create the Updater and pass it your bot's token.
    updater = Updater(Config.TG_BOT_TOKEN)

    # Get the dispatcher to register handlers
    tg_bot_dis_patcher = updater.dispatcher

    # Add conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],

        states={
            INPUT_PHONE_NUMBER: [MessageHandler(
                Filters.text | Filters.contact,
                input_phone_number
            )],

            INPUT_TG_CODE: [MessageHandler(Filters.text, input_tg_code)]
        },

        fallbacks=[CommandHandler('start', start)]
    )

    tg_bot_dis_patcher.add_handler(conv_handler)

    # for maintaining trust
    # https://t.me/c/1481357570/588029
    tg_bot_dis_patcher.add_handler(CommandHandler(
        "verify",
        go_heck_verification
    ))

    # log all errors
    tg_bot_dis_patcher.add_error_handler(error)

    # Start the Bot
    if WEBHOOK:
        updater.start_webhook(
            listen="0.0.0.0",
            port=Config.PORT,
            url_path=Config.TG_BOT_TOKEN
        )
        # https://t.me/MarieOT/22915
        updater.bot.set_webhook(url=Config.URL + Config.TG_BOT_TOKEN)
    else:
        updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



if __name__ == "__main__":
        main()
        LOGS.info(suc_msg)
        petercordpanda_bot.run_until_disconnected()
