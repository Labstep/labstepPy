#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')

# Make new
new_exp = LS.newExperiment(user,'MONTY')
print('\n NEW \n')
print(new_exp)

# Delete it
del_exp = LS.deleteExperiment(user, new_exp)
print('\n DELETED \n')
print(del_exp)

# Get info on it, the 'deleted_at' field should be updated
get_exp = LS.getExperiment(user, del_exp['id'])
print('\n FIND \n')
print(get_exp)