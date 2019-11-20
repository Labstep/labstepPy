#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'


class TestUser:
    def test_setWorkspace(self):
        my_workspace = testUser.getWorkspace(11339)
        testUser.setWorkspace(my_workspace)
        my_experiment = testUser.newExperiment('Test')
        workspace_experiments = my_workspace.getExperiments()
        assert workspace_experiments[0].id == my_experiment.id, \
            'FAILED TO SET WORKSPACE!'

    # getSingle()
    def test_getExperiment(self):
        entity = testUser.newExperiment(testName)
        result = testUser.getExperiment(entity.id)
        assert result.name == testName, \
            'FAILED TO GET EXPERIMENT'

    def test_getProtocol(self):
        entity = testUser.newProtocol(testName)
        result = testUser.getProtocol(entity.id)
        assert result.name == testName, \
            'FAILED TO GET PROTOCOL'

    def test_getResource(self):
        entity = testUser.newResource(testName)
        result = testUser.getResource(entity.id)
        assert result.name == testName, \
            'FAILED TO GET RESOURCE'

    def test_getWorkspace(self):
        entity = testUser.newWorkspace(testName)
        result = testUser.getWorkspace(entity.id)
        assert result.name == testName, \
            'FAILED TO GET WORKSPACE'

    # getMany()
    def test_getExperiments(self):
        result = testUser.getExperiments()
        assert result[0].name, \
            'FAILED TO GET EXPERIMENTS!'

    def test_getProtocols(self):
        result = testUser.getProtocols()
        assert result[0].name, \
            'FAILED TO GET PROTOCOLS!'

    def test_getResources(self):
        result = testUser.getResources()
        assert result[0].name, \
            'FAILED TO GET RESOURCES!'

    def test_getTags(self):
        result = testUser.getTags()
        assert result[0].name, \
            'FAILED TO GET TAGS!'

    def test_getWorkspaces(self):
        result = testUser.getWorkspaces()
        assert result[0].name, \
            'FAILED TO GET WORKSPACES!'

    # newEntity()
    def test_newExperiment(self):
        result = testUser.newExperiment(testName)
        assert result.name == testName, \
            'FAILED TO CREATE NEW EXPERIMENT'

    def test_newProtocol(self):
        result = testUser.newProtocol(testName)
        assert result.name == testName, \
            'INCORRECT NEW PROTOCOL NAME'

    def test_newResource(self):
        result = testUser.newResource(testName)
        assert result.name == testName, \
            'INCORRECT NEW RESOURCE NAME'

    """ def test_newTag(self):
        result = testUser.newTag(testName)
        result.delete()
        assert result.name == testName, \
            'INCORRECT NEW TAG NAME' """

    def test_newWorkspace(self):
        result = testUser.newWorkspace(testName)
        assert result.name == testName, \
            'INCORRECT NEW WORKSPACE NAME'

    def test_newFile(self):
        result = testUser.newFile('./tests/test_user.py')
        assert result, \
            'FAILED TO ADD NEW FILE!'
