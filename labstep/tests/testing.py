#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import json

user = LS.login('demo@labstep.com','demopassword')

# Get Tags
tags = LS.getTags(user, name='Hello')
print(len(tags),'TAGS FOUND \n\n')
print(tags)