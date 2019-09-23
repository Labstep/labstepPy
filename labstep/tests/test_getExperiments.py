#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import json

user = LS.login('demo@labstep.com','demopassword')

# Get
n = 3
exp = LS.getExperiments(user, n)

for i in range(n):
    print('\n GET EXPERIMENTS {} = \n'.format(i+1))
    print(exp[i])