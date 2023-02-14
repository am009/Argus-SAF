#!/bin/bash

export VIRTUALENVWRAPPER_PYTHON=python2.7
export WORKON_HOME=~/.py2venvs
source /usr/local/bin/virtualenvwrapper.sh
workon nativedroid

# start python server
python /root/Argus-SAF/tools/scripts/start_nativedroid_server.py /tmp/binaries/ localhost 50051 localhost 55001 ~/.amandroid_stash/amandroid/taintAnalysis/sourceAndSinks/NativeSourcesAndSinks.txt ~/.amandroid_stash/amandroid/taintAnalysis/sourceAndSinks/TaintSourcesAndSinks.txt > $1.pystdout.log 2> $1.pystderr.log &
nativedroid_pid=$!

# start java server
java -jar /root/Argus-SAF/binaries/argus-saf-3.2.1-SNAPSHOT-assembly.jar jnsaf /tmp/jn-saf/ 55001 localhost 50051 > >(tee $1.jnstdout.log) 2> >(tee $1.jnstderr.log >&2) &
jnsaf_pid=$!

sleep 5s

# start submitter
java -jar /root/Argus-SAF/binaries/argus-saf-3.2.1-SNAPSHOT-assembly.jar submitter $1 localhost 55001

# rm -rf /tmp/binaries
