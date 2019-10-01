#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import json
from datetime import datetime
from time import gmtime, strftime



user = LS.login('demo@labstep.com','demopassword')

"""
# Get Experiments
entity = LS.getProtocols(user,
                        #  search_query='new',
                         created_at_from='2019-09-01',
                         created_at_to='2019-09-30',
                        #  tag_id=241,
                         )
# Print details
for i in range(len(entity)):
    print('\n GETTING PROTOCOLS {} ='.format(i+1))
    print(entity[i]['name'])
    print(entity[i]['last_version']['created_at'])
"""


def getTime():
    timezone = strftime('%z', gmtime())
    tz_hour = timezone[:3]
    tz_minute = timezone[3:]
    timestamp = datetime.now().strftime("%Y-%m-%d" + "T" + "%H:%M:%S" +
                                        "{}:{}".format(tz_hour,tz_minute))
    return timestamp


