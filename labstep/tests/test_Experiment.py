#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')


# get
exp = LS.getExperiment(user,22775)
print('\n GET EXPERIMENT = \n')
print(exp)

# Delete it
del_exp = LS.deleteExperiment(user,exp)
print('\n DELETED = \n')
print(del_exp)

# # Get info on it, the 'deleted_at' field should be updated
# get_exp = LS.getExperiment(user, del_exp['id'])
# print('\n FIND = \n')
# print(get_exp)