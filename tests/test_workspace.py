#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newWorkspace(testName)
entity = testUser.getWorkspace(new_entity.id)
testUser.setWorkspace(entity.id)


class TestWorkspace:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT WORKSPACE'

    def test_delete(self):
        entityToDelete = testUser.newWorkspace(testName)
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE WORKSPACE'

    # getMany()
    def test_getExperiments(self):
        testUser.newExperiment(testName)
        result = entity.getExperiments()
        assert result[0].id, \
            'FAILED TO GET EXPERIMENTS'

    def test_getProtocols(self):
        testUser.newProtocol(testName)
        result = entity.getProtocols()
        assert result[0].id, \
            'FAILED TO GET PROTOCOLS'

    def test_getResources(self):
        testUser.newResource(testName)
        result = entity.getResources()
        assert result[0].id, \
            'FAILED TO GET RESOURCES'

    def test_getResourceCategorys(self):
        testUser.newResourceCategory(testName)
        result = entity.getResourceCategorys()
        assert result[0].id, \
            'FAILED TO GET RESOURCE CATEGORYS'

    def test_getResourceLocations(self):
        new_RL = testUser.newResourceLocation(testName)
        result = entity.getResourceLocations()
        new_RL.delete()
        assert result[0].id, \
            'FAILED TO GET RESOURCE LOCATIONS'

    def test_getOrderRequests(self):
        new_resource = testUser.newResource(testName)
        testUser.newOrderRequest(new_resource)
        result = entity.getOrderRequests()
        assert result[0].id, \
            'FAILED TO GET ORDER REQUESTS'

    def test_getTags(self):
        new_tag = testUser.newTag('test_newTag', type='experiment_workflow')
        result = entity.getTags()
        new_tag.delete()
        assert result[0].id, \
            'FAILED TO GET TAGS'

    # newEntity()
    def test_newExperiment(self):
        result = entity.newExperiment(testName)
        assert result.name == testName, \
            'FAILED TO CREATE NEW EXPERIMENT'

    def test_newProtocol(self):
        result = entity.newProtocol(testName)
        assert result.name == testName, \
            'FAILED TO CREATE NEW PROTOCOL'

    def test_newResource(self):
        result = entity.newResource(testName)
        assert result.name == testName, \
            'FAILED TO CREATE NEW RESOURCE'

    def test_newResourceCategory(self):
        result = entity.newResourceCategory(testName)
        assert result.name == testName, \
            'FAILED TO CREATE NEW RESOURCE CATEGORY'

    def test_newResourceLocation(self):
        result = entity.newResourceLocation(testName)
        result.delete()
        assert result.name == testName, \
            'FAILED TO CREATE NEW RESOURCE LOCATION'

    def test_newOrderRequest(self):
        new_resource = testUser.newResource(testName)
        result = entity.newOrderRequest(new_resource)
        assert result.name == testName, \
            'FAILED TO CREATE NEW ORDER REQUEST'

    def test_newTag(self):
        result = entity.newTag('test_newTag', type='experiment_workflow')
        result.delete()
        assert result.name == 'test_newTag', \
            'FAILED TO CREATE NEW TAG'

    def test_newFile(self):
        result = entity.newFile('./tests/test_workspace.py')
        assert result is not None, \
            'FAILED TO ADD NEW FILE'
