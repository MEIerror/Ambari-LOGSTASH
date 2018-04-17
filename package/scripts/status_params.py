#!/usr/bin/env python
"""
Elasticsearch  service params

"""

from resource_management import *
from resource_management.libraries.script.script import Script
from resource_management.libraries.functions import format
config = Script.get_config()

logstash_pid_dir = config['configurations']['logstash-site']['logstash_pid_dir']
logstash_pid_file = format("{logstash_pid_dir}/logstash.pid")