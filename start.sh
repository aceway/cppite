#!/usr/bin/env bash

BIN_FILE=$(readlink -f $0)
PROJ_BIN=$(dirname $BIN_FILE)
PROJ_HOME=$(dirname $PROJ_BIN)
SCRIPT_NAME=$(basename $BIN_FILE)

#echo $BIN_FILE
#echo $PROJ_BIN
#echo ${PROJ_HOME}
#echo $SCRIPT_NAME

old_pwd=`pwd`
cd ${PROJ_BIN}

python ./src/main.py

cd $old_pwd
