#Ilham Mansiez
#Petercord Userbot
#Tentang AKU DAN DIA

FROM  ilhammansiz17/ilham-mansiez-petercord:Petercord-Userbot

# set timezone
ENV TZ=Asia/Jakarta




RUN apt-get autoremove --purge
RUN chmod +x /usr/local/bin/*
RUN pip3 install --upgrade pip setuptools 
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \

    # cloning the repo and installing requirements.
    && git clone -b PandaUserbot https://github.com/ilhammansiz/PandaX_Userbot.git /root/ilhammansiz/ \
    && pip3 install --no-cache-dir -r root/ilhammansiz/PandaVersion/Panda/requirements.txt \
    && pip3 uninstall av -y && pip3 install av --no-binary av

# changing workdir
WORKDIR /root/ilhammansiz/

# start the bot
CMD ["bash", "PandaVersion/Panda/startup.sh"]
