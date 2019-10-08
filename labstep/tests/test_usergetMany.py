#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')

n = 2

# Get experiments
experiments = user.getExperiments(count=n)
for i in range(len(experiments)):
    print('\n GETTING EXPERIMENTS[{}] \n'.format(i), experiments[i])

# Get protocols
protocols = user.getProtocols(count=n)
for i in range(len(protocols)):
    print('\n GETTING PROTOCOLS[{}] \n'.format(i), protocols[i])

# Get resources
resources = user.getResources(count=n)
for i in range(len(resources)):
    print('\n GETTING RESOURCES[{}] \n'.format(i), resources[i])

# Get tags
tags = user.getTags(count=n)
for i in range(len(tags)):
    print('\n GETTING TAGS[{}] \n'.format(i), tags[i])

# Get workspaces
workspaces = user.getWorkspaces(count=n)
for i in range(len(workspaces)):
    print('\n GETTING WORKSPACES[{}] \n'.format(i), workspaces[i])
