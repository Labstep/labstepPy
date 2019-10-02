#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import labstep.core as LSC

user = LS.login('demo@labstep.com','demopassword')


#
resource = LSC.newResource(user,'Test Ordered',status='Ordered')
#print(resource)




