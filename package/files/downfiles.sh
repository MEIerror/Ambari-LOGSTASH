#!/usr/bin/env bash
#time: 11/2/17


LOGSTASH_URL=$1 #es下载地址
WORK_DIR=$2  #安装目录
LOG_USER=$3

if [ ! -d ${WORK_DIR} ]; then
    mkdir -p ${WORK_DIR}
fi

if [ ! -d ${WORK_DIR}/logstash-5.2.0 ];then
wget -O ${WORK_DIR}/logstash-5.2.0.tar.gz  ${LOGSTASH_URL}
tar -zxf ${WORK_DIR}/logstash-5.2.0.tar.gz -C ${WORK_DIR}
fi


id ${LOG_USER} &> /dev/null
if [ $? -ne 0 ]; then
    useradd ${LOG_USER}
fi


