## Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


FROM theteamultroid/ultroid:dev

# set timezone
ENV TZ=Asia/Jakarta

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \

    # cloning the repo and installing requirements.
    && git clone -b PandaUserbot https://github.com/ilhammansiz/PandaX_Userbot.git /root/ilhammansiz/ \
    && pip3 install --no-cache-dir -r root/ilhammansiz/PandaVersion/Panda/requirements.txt \
    && pip3 uninstall av -y && pip3 install av --no-binary av

# changing workdir
WORKDIR /root/ilhammansiz/

# start the bot
CMD ["bash", "PandaVersion/Panda/startup.sh"]
