#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import json
import pprint

user = LS.login('demo@labstep.com','demopassword')

# Get
protocol = LS.getProtocol(user,9938)
print('\n GET PROTOCOL = \n')
print(protocol)


# Edit it
edits = LS.editProtocol(user,protocol,name='NEW MONTY',)
print('\n EDITTED = \n')
print(edits)