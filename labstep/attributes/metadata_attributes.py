#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep


user = labstep.login('apitest@labstep.com', 'apitestpass')
entity = user.newResource("Acetic Acid")
print(entity.addMetadata("Refractive Index", value="1.73"))
