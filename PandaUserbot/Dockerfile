## Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


FROM theteamultroid/ultroid:main

# set timezone
ENV TZ=Asia/Jakarta



RUN git clone https://github.com/ilhammansiz/PandaX_Userbot.git /root/ilhammansiz/
WORKDIR /root/ilhammansiz/

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
RUN pip3 install --no-cache-dir -r PandaVersion/Panda/requirements.txt
RUN pip3 uninstall av -y && pip3 install av --no-binary av

# start the bot
CMD ["bash", "PandaVersion/Panda/startup.sh"]
