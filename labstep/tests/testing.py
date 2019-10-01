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


LS.getEntity(user,'experiment_workflow',12)


