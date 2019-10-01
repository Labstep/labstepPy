#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')


# Get
resource = LS.getResource(user,404897)
print('\n GET RESOURCE = \n')
print(resource)

# Edit it
# edits = LS.editResource(user,resource,location='The Crick')
# print('\n EDITS = \n')
# print(edits)