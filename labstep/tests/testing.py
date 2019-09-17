#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import json
import datetime
from time import gmtime, strftime


user = LS.login('demo@labstep.com','demopassword')

# Get an experiment
get_some_exps = LS.getExperiments(user, count=2)
get1_exp = LS.getExperiment(user, 21967)

# Delete/archive an experiment
LS.deleteExperiment(user,get1_exp)



#timezone = strftime("%z", gmtime())
#print(timezone)

#timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S{}'.format(timezone))
#print(json.dumps(timestamp))
