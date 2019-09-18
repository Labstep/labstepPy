#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')

# Make new
new_protocol = LS.newProtocol(user,'NEW')
print('\n NEW PROTOCOL \n')
print(new_protocol)

# Delete it
del_protocol = LS.deleteProtocol(user, new_protocol)
print('\n DELETED \n')
print(del_protocol)

# Get info on it, the 'deleted_at' field should be updated
get_protocol = LS.getProtocol(user, del_protocol['id'])
print('\n FIND \n')
print(get_protocol)