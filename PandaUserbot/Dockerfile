#Ilham Mansiez
#Petercord Userbot
#Tentang AKU DAN DIA

FROM  ilhammansiz17/ilham-mansiez-petercord:Petercord-Userbot

# set timezone
ENV TZ=Asia/Jakarta


RUN apt-get install -y bash \
    build-essential \
    cmake \
    curl \
    debian-archive-keyring \
    debian-keyring \
    ffmpeg \
    gcc \
    git \ 
    gnupg \
    jq \
    libatlas-base-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavfilter-dev \    
    libavformat-dev \      
    libavutil-dev \  
    libboost-python-dev \  
    libcurl4-openssl-dev \
    libffi-dev \ 
    libgconf-2-4 \
    libgtk-3-dev \
    libjpeg-dev \ 
    libjpeg62-turbo-dev \
    libopus-dev \
    libopus0 \
    libpq-dev \
    libreadline-dev \
    libswresample-dev \
    libswscale-dev \
    libssl-dev \
    libwebp-dev \
    libx11-dev \
    libxi6 \
    libxml2-dev \ 
    libxslt1-dev \  
    libyaml-dev \   
    linux-headers-amd64 \
    make \
    mediainfo \
    megatools \
    meson \
    musl \
    musl-dev \
    neofetch \
    netcat \
    ninja-build \
    openssh-client \
    openssh-server \
    openssl \
    p7zip-full \
    pdftk \
    pkg-config \
    procps \
    python3-dev \
    texinfo \
    unzip \
    util-linux \
    wkhtmltopdf \
    xvfb \
    yasm \
    zlib1g \
    zlib1g-dev

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \

    # cloning the repo and installing requirements.
    && git clone -b PandaUserbot https://github.com/ilhammansiz/PandaX_Userbot.git /root/ilhammansiz/ \
    && pip3 install --no-cache-dir -r root/ilhammansiz/PandaVersion/Panda/requirements.txt \
    && pip3 uninstall av -y && pip3 install av --no-binary av

# changing workdir
WORKDIR /root/ilhammansiz/

# start the bot
CMD ["bash", "PandaVersion/Panda/startup.sh"]
