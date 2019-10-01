#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')

# Make new
new_workspace = LS.newWorkspace(user,'NEW')
print('\n NEW \n')
print(new_workspace)

# Delete it
del_workspace = LS.deleteWorkspace(user, new_workspace)
print('\n DELETED \n')
print(del_workspace)

# Get info on it, the 'deleted_at' field should be updated
get_workspace = LS.getWorkspace(user, del_workspace['id'])
print('\n FIND \n')
print(get_workspace)