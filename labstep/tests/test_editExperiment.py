#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')

# Get
exp = LS.getExperiment(user,22586)
print('\n GET EXPERIMENT = \n')
print(exp)

# Edit it
edits = LS.editExperiment(user,exp,name='MIXED',description='NEW DESCRIPTION')
print('\n EDITTED = \n')
print(edits)
