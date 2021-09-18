# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from importlib import util
from pathlib import Path
from sys import modules


def load_plugins(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        path = Path(f"PandaX_v20/{plugin_name}.py")
        name = "PandaX_v20.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        from . import HNDLR, LOGS, asst, udB, petercordpanda_bot
        from .Panda.core import HELP, PLUGINS
        from .Panda.database import Var
        from .PandaVX import _supporter as xxx
        from .PandaVX._assistant import (
            asst_cmd,
            callback,
            in_pattern,
            inline,
            inline_owner,
            owner,
        )
        from .PandaVX._decorators import ilhammansiz_cmd, ultroid_cmd
        from .PandaVX._wrappers import eod, eor

        path = Path(f"PandaX_v20/{plugin_name}.py")
        name = "PandaX_v20.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.asst = asst
        mod.tgbot = asst
        mod.petercordpanda_bot = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.petercordpanda = petercordpanda_bot
        mod.ultroid_bot = petercordpanda_bot
        mod.owner = owner()
        mod.in_owner = inline_owner()
        mod.inline = inline()
        mod.in_pattern = in_pattern
        mod.eod = eod
        mod.edit_delete = eod
        mod.LOGS = LOGS
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.Var = Var
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.asst_cmd = asst_cmd
        mod.ilhammansiz_cmd = ilhammansiz_cmd
        mod.ultroid_cmd = ultroid_cmd
        mod.on_cmd = ilhammansiz_cmd
        mod.on_cmd = ultroid_cmd
        mod.callback = callback
        mod.Redis = udB.get
        modules["support"] = xxx
        modules["userbot"] = xxx
        modules["userbot.utils"] = xxx
        modules["userbot.config"] = xxx
        spec.loader.exec_module(mod)
        modules["PandaX_v20." + plugin_name] = mod
        if not plugin_name.startswith("_"):
            try:
                PLUGINS.append(plugin_name)
            except BaseException:
                if plugin_name not in PLUGINS:
                    PLUGINS.append(plugin_name)
                else:
                    pass
            try:
                doc = modules[f"PandaX_v20.{plugin_name}"].__doc__
                HELP.update({f"{plugin_name}": doc.format(i=HNDLR)})
            except KeyError:
                pass
            except Exception as e:
                print(e)


def load_panda(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        path = Path(f"Panda-Userbot/{plugin_name}.py")
        name = "Panda-Userbot.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        from . import HNDLR, LOGS, asst, udB, petercordpanda_bot
        from .Panda.core import HELP, PANDA
        from .Panda.database import Var
        from .PandaVX import _supporter as xxx
        from .PandaVX._assistant import (
            asst_cmd,
            callback,
            in_pattern,
            inline,
            inline_owner,
            owner,
        )
        from .PandaVX._decorators import ilhammansiz_cmd, ultroid_cmd
        from .PandaVX._wrappers import eod, eor

        path = Path(f"Panda-Userbot/{plugin_name}.py")
        name = "Panda-Userbot.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.asst = asst
        mod.tgbot = asst
        mod.petercordpanda_bot = petercordpanda_bot
        mod.ultroid_bot = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.petercordpanda = petercordpanda_bot
        mod.owner = owner()
        mod.in_owner = inline_owner()
        mod.inline = inline()
        mod.in_pattern = in_pattern
        mod.eod = eod
        mod.edit_delete = eod
        mod.LOGS = LOGS
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.Var = Var
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.asst_cmd = asst_cmd
        mod.ilhammansiz_cmd = ilhammansiz_cmd
        mod.ultroid_cmd = ultroid_cmd
        mod.on_cmd = ultroid_cmd
        mod.callback = callback
        mod.Redis = udB.get
        modules["support"] = xxx
        modules["userbot"] = xxx
        modules["userbot.utils"] = xxx
        modules["userbot.config"] = xxx
        spec.loader.exec_module(mod)
        modules["Panda-Userbot." + plugin_name] = mod
        if not plugin_name.startswith("_"):
            try:
                PANDA.append(plugin_name)
            except BaseException:
                if plugin_name not in PANDA:
                    PANDA.append(plugin_name)
                else:
                    pass
            try:
                doc = modules[f"Panda-Userbot.{plugin_name}"].__doc__
                HELP.update({f"{plugin_name}": doc.format(i=HNDLR)})
            except KeyError:
                pass
            except Exception as e:
                print(e)


# for modules


def load_modules(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        path = Path(f"modules/{plugin_name}.py")
        name = "modules.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        from . import HNDLR, LOGS, asst, udB, petercordpanda_bot
        from .Panda.core import HELP, MODULES
        from .Panda.database import Var
        from .PandaVX import _supporter as xxx
        from .PandaVX._assistant import (
            asst_cmd,
            callback,
            in_pattern,
            inline,
            inline_owner,
            owner,
        )
        from .PandaVX._decorators import ilhammansiz_cmd, ultroid_cmd
        from .PandaVX._supporter import Config, admin_cmd, sudo_cmd, register
        from .PandaVX._wrappers import eod, eor
        from PandaX_Userbot import CUSTOM_CMD

        path = Path(f"modules/{plugin_name}.py")
        name = "modules.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.asst = asst
        mod.tgbot = asst
        mod.petercordpanda_bot = petercordpanda_bot
        mod.ultroid_bot = petercordpanda_bot
        mod.ub = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.petercordpanda = petercordpanda_bot
        mod.borg = petercordpanda_bot
        mod.telebot = petercordpanda_bot
        mod.jarvis = petercordpanda_bot
        mod.friday = petercordpanda_bot
        mod.owner = owner()
        mod.in_owner = inline_owner()
        mod.inline = inline()
        mod.eod = eod
        mod.edit_delete = eod
        mod.LOGS = LOGS
        mod.in_pattern = in_pattern
        mod.hndlr = HNDLR
        mod.handler = HNDLR
        mod.HNDLR = HNDLR
        mod.CMD_HNDLR = HNDLR
        mod.CUSTOM_CMD = HNDLR
        mod.Config = Config
        mod.Var = Var
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.asst_cmd = asst_cmd
        mod.ilhammansiz_cmd = ilhammansiz_cmd
        mod.ultroid_cmd = ultroid_cmd
        mod.register = register
        mod.on_cmd = ultroid_cmd
        mod.callback = callback
        mod.Redis = udB.get
        mod.admin_cmd = admin_cmd
        mod.sudo_cmd = sudo_cmd
        modules["ub"] = xxx
        modules["var"] = xxx
        modules["jarvis"] = xxx
        modules["support"] = xxx
        modules["userbot"] = xxx
        modules["telebot"] = xxx
        modules["fridaybot"] = xxx
        modules["Panda"] = xxx
        modules["jarvis.utils"] = xxx
        modules["uniborg.util"] = xxx
        modules["telebot.utils"] = xxx
        modules["userbot.utils"] = xxx
        modules["..core.managers"] = xxx
        modules["userbot.events"] = xxx
        modules["userbot.plugins"] = xxx
        modules["jarvis.jconfig"] = xxx
        modules["userbot.config"] = xxx
        modules["fridaybot.utils"] = xxx
        modules["fridaybot.Config"] = xxx
        modules["userbot.uniborgConfig"] = xxx
        spec.loader.exec_module(mod)
        modules["modules." + plugin_name] = mod
        if not plugin_name.startswith("_"):
            try:
                MODULES.append(plugin_name)
            except BaseException:
                if plugin_name not in MODULES:
                    MODULES.append(plugin_name)
                else:
                    pass
            try:
                doc = modules[f"modules.{plugin_name}"].__doc__
                HELP.update({f"{plugin_name}": doc.format(i=HNDLR)})
            except KeyError:
                pass
            except Exception as e:
                print(e)


# for assistant


def load_assistant(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        path = Path(f"PandaX_ASsistant/{plugin_name}.py")
        name = "PandaX_ASsistant.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        from . import HNDLR, LOGS, asst, udB, petercordpanda_bot
        from .PandaVX._assistant import asst_cmd, callback, in_pattern, inline_owner, owner
        from .PandaVX._wrappers import eod, eor

        path = Path(f"PandaX_ASsistant/{plugin_name}.py")
        name = "PandaX_ASsistant.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.petercordpanda_bot = petercordpanda_bot
        mod.petercordpanda = petercordpanda_bot
        mod.Redis = udB.get
        mod.udB = udB
        mod.bot = petercordpanda_bot
        mod.asst = asst
        mod.owner = owner()
        mod.in_pattern = in_pattern
        mod.in_owner = inline_owner()
        mod.eod = eod
        mod.eor = eor
        mod.callback = callback
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.asst_cmd = asst_cmd
        spec.loader.exec_module(mod)
        modules["PandaX_ASsistant." + plugin_name] = mod


# msg forwarder


def load_pmbot(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        path = Path(f"PandaX_ASsistant/pmbot/{plugin_name}.py")
        name = "PandaX_ASsistant.pmbot.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        from . import HNDLR, LOGS, asst, udB, petercordpanda_bot
        from .PandaVX._assistant import asst_cmd, callback, owner
        from .PandaVX._wrappers import eod, eor

        path = Path(f"PandaX_ASsistant/pmbot/{plugin_name}.py")
        name = "PandaX_ASsistant.pmbot.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.petercordpanda_bot = petercordpanda_bot
        mod.petercordpanda_bot = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.Redis = udB.get
        mod.udB = udB
        mod.asst = asst
        mod.owner = owner()
        mod.eod = eod
        mod.eor = eor
        mod.callback = callback
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.asst_cmd = asst_cmd
        spec.loader.exec_module(mod)
        modules["PandaX_ASsistant.pmbot" + plugin_name] = mod


def load_manager(plugin_name):
    if plugin_name.startswith("__"):
        pass
    else:
        from . import HNDLR, LOGS, asst, udB, petercordpanda_bot
        from .PandaVX._assistant import asst_cmd, callback, owner

        path = Path(f"PandaX_ASsistant/PandaSX_userbot/{plugin_name}.py")
        name = "PandaX_ASsistant.PandaSX_userbot.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.petercordpanda_bot = petercordpanda_bot
        mod.petercordpanda_bot = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.Redis = udB.get
        mod.udB = udB
        mod.asst = asst
        mod.owner = owner()
        mod.callback = callback
        mod.asst_cmd = asst_cmd
        spec.loader.exec_module(mod)
        modules["PandaX_ASsistant.PandaSX_userbot" + plugin_name] = mod


def load_vc(plugin_name):
    if not plugin_name.startswith("__"):
        from . import HNDLR, LOGS, asst, udB, petercordpanda_bot, vcClient
        from .Panda.core import VC_HELP

        path = Path(f"PandaX_v21/{plugin_name}.py")
        name = "PandaX_v21.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.petercordpanda_bot = petercordpanda_bot
        mod.petercordpanda = petercordpanda_bot
        mod.ultroid = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.Redis = udB.get
        mod.udB = udB
        mod.asst = asst
        mod.vcClient = vcClient
        mod.LOGS = LOGS
        spec.loader.exec_module(mod)
        modules["PandaX_v21." + plugin_name] = mod
        try:
            VC_HELP.update(
                {
                    plugin_name: modules[f"PandaX_v21.{plugin_name}"].__doc__.format(
                        i=udB["VC_HNDLR"] if udB.get("VC_HNDLR") else HNDLR
                    )
                    + "\n"
                }
            )
        except BaseException:
            pass


def load_vcbot(plugin_name):
    if not plugin_name.startswith("__"):
        from . import HNDLR, LOGS, asst, udB, petercordpanda_bot, MusicPanda
        from .Panda.core import VC_HELP

        path = Path(f"PandaMusicBot/{plugin_name}.py")
        name = "PandaMusicBot.{}".format(plugin_name)
        spec = util.spec_from_file_location(name, path)
        mod = util.module_from_spec(spec)
        mod.petercordpanda_bot = petercordpanda_bot
        mod.petercordpanda = petercordpanda_bot
        mod.ultroid = petercordpanda_bot
        mod.bot = petercordpanda_bot
        mod.Redis = udB.get
        mod.udB = udB
        mod.asst = asst
        mod.MusicPanda = MusicPanda
        mod.LOGS = LOGS
        spec.loader.exec_module(mod)
        modules["PandaMusicBot." + plugin_name] = mod
        try:
            VC_HELP.update(
                {
                    plugin_name: modules[f"PandaMusicBot.{plugin_name}"].__doc__.format(
                        i=udB["VC_HNDLR"] if udB.get("VC_HNDLR") else HNDLR
                    )
                    + "\n"
                }
            )
        except BaseException:
            pass
