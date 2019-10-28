#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

testName = 'Api Default Name'
testDescription = 'Api Default Description'
testStatus = 'available'
testFilePath = './labstep/tests/test_setup.py'

# Create a new experiment
new_exp = testUser.newExperiment(name=testName,
                                 description=testDescription)

# Create a new protocol
new_pro = testUser.newProtocol(name=testName)

# Create a new resource
new_res = testUser.newResource(name=testName)

# Create a new tag
new_tag = testUser.newTag(name=testName)

# Create a new workspace
new_wksp = testUser.newWorkspace(name=testName)

# Create a new file
new_file = testUser.newFile(filepath=testFilePath)
