#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import labstep.core as LSC

user = LS.login('demo@labstep.com','demopassword')


# Get
entity = LSC.getResources(user,
                        #   status='available'
                         )
print("\n I'M GETTING RESOURCES\n")
print(len(entity))

