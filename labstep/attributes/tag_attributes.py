#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep


user = labstep.login('apitest@labstep.com', 'apitestpass')

entity = user.getTags()
entity[0].attributes()
