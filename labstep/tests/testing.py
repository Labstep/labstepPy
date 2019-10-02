#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import labstep.core as LSC

user = LS.login('demo@labstep.com','demopassword')


# Get It
get = LSC.getWorkspaces(user,name='first')
#print(get)

for i in range(24):
    LSC.deleteWorkspace(user,get[i])




