#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')


# Get It
workspaces = user.getWorkspaces()

print(workspaces)



