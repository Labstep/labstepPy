#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep


user = labstep.login('apitest@labstep.com', 'apitestpass')
entity = user.newResource("Acetic Acid")
entity.addMetadata(fieldName="Refractive Index", value="1.73")
