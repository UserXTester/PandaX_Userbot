
from .. import asst, udB, petercordpanda_bot

CMD_HELP = {}


def sudoers():
    return udB["SUDOS"].split()


def should_allow_sudo():
    if udB["SUDO"] == "True":
        return True
    else:
        return False


def owner_and_sudos():
    return [str(petercordpanda_bot.uid), *sudoers()]
