#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')

# Make new
new_resource = LS.newResource(user,'NEW')
print('\n NEW \n')
print(new_resource)

# Edit it
edits = LS.editResource(user, new_resource, name='RENAMED')
print('\n EDITTED \n')
print(edits)

# Delete it
del_resource = LS.deleteResource(user, new_resource)
print('\n DELETED \n')
print(del_resource)

# Get info on it, the 'deleted_at' field should be updated
get_resource = LS.getResource(user, del_resource['id'])
print('\n FIND \n')
print(get_resource)