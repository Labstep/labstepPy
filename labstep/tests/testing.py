#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')

new = user.newFile('./labstep/tests/test_all.py')