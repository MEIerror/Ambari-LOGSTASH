#!/usr/bin/env python
"""
Elasticsearch Params configurations
"""

from resource_management import *
import os

# server configurations
config = Script.get_config()



logstash_user = config['configurations']['logstash-env']['logstash_user']
logstash_group = config['configurations']['logstash-env']['logstash_group']
work_dir = config['configurations']['logstash-env']['work_dir']
logstash_tar_url = config['configurations']['logstash-env']['logstash_tar_url']

logstash_yml = config['configurations']['logstash-site']['logstash.yml']
startup_options = config['configurations']['logstash-site']['startup.options']
log_es = config['configurations']['logstash-site']['log_es.conf']

logstash_yml_conf = format("{work_dir}/logstash-5.2.0/config/logstash.yml")
startup_conf = format("{work_dir}/logstash-5.2.0/config/startup.options")
logtest_conf = format("{work_dir}/logstash-5.2.0/config/log-es.conf")



hostname = config['hostname']
java_home = config['hostLevelParams']['java_home']

service_packagedir = os.path.realpath(__file__).split('/scripts')[0]

logstash_server_host = ""
logstash_server_hosts = config['clusterHostInfo']['logstash_master_hosts']
if logstash_server_hosts is not None and len(logstash_server_hosts) > 0:
    logstash_host = logstash_server_hosts[0]

















