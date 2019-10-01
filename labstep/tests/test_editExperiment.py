#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from datetime import datetime
from time import gmtime, strftime

user = LS.login('demo@labstep.com','demopassword')

# Get
exp = LS.getExperiment(user,22586)
print('\n GET EXPERIMENT = \n')
print(exp)


# Edit it
edits = LS.editExperiment(user,exp,description='HELLO YOU')
print('\n EDITS = \n')
print(edits)