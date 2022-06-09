ARG UBUNTU_MIRROR=mirrors.tuna.tsinghua.edu.cn

FROM ubuntu:18.04
ARG UBUNTU_MIRROR
# clean files in .gitignore before building image

# develop: docker run -it --name test_jucify -v C:\JuCify\:/root/Jucify ubuntu:22.04
# headless jdk saves 300mb space
# "build-essential python3.7-dev graphviz libgraphviz-dev" is required for pygraphviz
SHELL ["/bin/bash", "-c"]

RUN sed -i "s/archive.ubuntu.com/${UBUNTU_MIRROR}/g" /etc/apt/sources.list \
 && sed -i "s/security.ubuntu.com/${UBUNTU_MIRROR}/g" /etc/apt/sources.list \
 && apt update && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends curl git wget sudo unzip software-properties-common nano openjdk-11-jdk-headless python2.7 protobuf-compiler \
 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY [".", "/root/Argus-SAF/"]

WORKDIR /root
SHELL ["/bin/bash", "-c"]
# Python env
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py \
 && python2.7 get-pip.py \
 && python2.7 -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
 && python2.7 -m pip install virtualenvwrapper \
 && echo export VIRTUALENVWRAPPER_PYTHON=python2.7 >> /root/.bashrc \
 && echo export WORKON_HOME=~/.py2venvs >> /root/.bashrc \
 && echo source /usr/local/bin/virtualenvwrapper.sh >> /root/.bashrc \
 && export VIRTUALENVWRAPPER_PYTHON=python2.7 \
 && export WORKON_HOME=~/.py2venvs \
 && source /usr/local/bin/virtualenvwrapper.sh \
 && mkvirtualenv --system-site-packages nativedroid \
 && python -m pip install -r ./Argus-SAF/nativedroid/requirements.txt \
 && cd Argus-SAF/ \
 && tools/scripts/install.sh nativedroid \
 && rm -rf /tmp/* /var/tmp/*

WORKDIR /root/Argus-SAF
# download ~/.amandroid_stash
RUN java -jar binaries/argus-saf-3.2.1-SNAPSHOT-assembly.jar taint -o /tmp ./benchmarks/NativeFlowBench/native_leak.apk && rm -rf /tmp/* /var/tmp/*

# /root/Argus-SAF/runTool.sh
ENTRYPOINT ["/bin/bash", "/root/Argus-SAF/runTool.sh"]
CMD ["/root/apps/app.apk"]
