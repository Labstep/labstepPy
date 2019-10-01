#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import labstep.core as LSC

user = LS.login('demo@labstep.com','demopassword')


# Get
exp = LSC.getExperiment(user,22785)

# Add comment
comment = LSC.addComment(user,exp,'Monty is commenting')

print(exp)
print(comment)

# Add protocol
# protocol = LSC.getProtocol(user,6171) # Existing protocol id
# protocol = LSC.getProtocol(user,1) # Non-existing protocol id
# add = LSC.addProtocol(user,exp,protocol)

