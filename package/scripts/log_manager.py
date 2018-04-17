#!/use/bin/env python
# coding = utf-8

from resource_management import *
from resource_management.core.resources.system import  File

def conf():
    import params
    import status_params

    File(params.logstash_yml_conf,
         owner=params.logstash_user,
         group=params.logstash_group,
         content=InlineTemplate(params.logstash_yml)
         )

    File(params.startup_conf,
         owner=params.logstash_user,
         group=params.logstash_group,
         content=InlineTemplate(params.startup_options)
         )
    File(params.logtest_conf,
         owner=params.logstash_user,
         group=params.logstash_group,
         content=InlineTemplate(params.log_es)
         )

    File(status_params.logstash_pid_file,
         owner=params.logstash_user,
         group=params.logstash_group
         )

