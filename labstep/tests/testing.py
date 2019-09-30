#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import json

user = LS.login('demo@labstep.com','demopassword')

# Keep this for use for handle error
# Get Tag
# tags = LS.getTag(user,1266)
# print(len(tags),'TAGS FOUND \n\n')
# print(tags)








# Get resource
resource = LS.getResource(user, 404897)
print('\n GET \n')
print(resource)

# Edit status
renamed = LS.editResource(user,resource,name='OMG')#,status=resource['status'])
print('\n RENAMED \n')
print(renamed)

# Edit status
# edits = LS.editResource(user,resource,status='requested')
# print('\n EDITTED \n')
# print(edits)

# Get updated
# updated = LS.getResource(user, 404897)
# print('\n UPDATED \n')
# print(updated)