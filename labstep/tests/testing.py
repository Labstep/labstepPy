#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')

# Make new experiment
newexp = LS.newExperiment(user,'Test')
print('NEW EXPERIMENT')
print(newexp)

# Delete that experiment
del_exp = LS.deleteExperiment(user, newexp)
print('DELETED')
print(del_exp)

# Get info on that experiment
get_exp = LS.getExperiment(user, exp['id'])
print('FIND')
print(get_exp)