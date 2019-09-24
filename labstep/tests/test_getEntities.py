#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import json

user = LS.login('demo@labstep.com','demopassword')

n = 3

# Get Experiments
exp = LS.getExperiments(user, n)
for i in range(n):
    print('\n GET EXPERIMENTS {} = \n'.format(i+1))
    print(exp[i])

# Get Protocols
protocol = LS.getProtocols(user, n)
for i in range(n):
    print('\n GET PROTOCOLS {} = \n'.format(i+1))
    print(protocol[i])

# Get Resources
resource = LS.getResources(user, n)
for i in range(n):
    print('\n GET RESOURCES {} = \n'.format(i+1))
    print(resource[i])

# Get Tags
tags = LS.getTags(user, n)
for i in range(n):
    print('\n GET TAGS {} = \n'.format(i+1))
    print(tags[i])