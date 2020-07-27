#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

from fixtures import user, testString


class User:
    def test_login(self):
        user = labstep.login('apitest@labstep.com', 'apitestpass')
        assert user.id == 8400, \
            'FAILED TO LOGIN'

    def test_authenticate(self):
        user = labstep.authenticate(
            'apitest@labstep.com', '1c5b51d1-a1a5-4661-9eea-f71b7523f909')
        assert user.id == 8400, \
            'FAILED TO AUTHENTICATE'

    def test_setWorkspace(self):
        my_workspace = user.getWorkspace(11339)
        user.setWorkspace(my_workspace.id)
        my_experiment = user.newExperiment('Test')
        workspace_experiments = my_workspace.getExperiments()
        assert workspace_experiments[0].id == my_experiment.id, \
            'FAILED TO SET WORKSPACE'

    # getSingle()
    def test_getExperiment(self):
        entity = user.newExperiment(testString)
        result = user.getExperiment(entity.id)
        assert result.name == testString, \
            'FAILED TO GET EXPERIMENT'

    def test_getProtocol(self):
        entity = user.newProtocol(testString)
        result = user.getProtocol(entity.id)
        assert result.name == testString, \
            'FAILED TO GET PROTOCOL'

    def test_getResource(self):
        entity = user.newResource(testString)
        result = user.getResource(entity.id)
        assert result.name == testString, \
            'FAILED TO GET RESOURCE'

    def test_getResourceLocation(self):
        entity = user.newResourceLocation(testString)
        result = user.getResourceLocation(entity.id)
        assert result.name == testString, \
            'FAILED TO GET RESOURCE LOCATION'

    def test_getResourceCategory(self):
        entity = user.newResourceCategory(testString)
        result = user.getResourceCategory(entity.id)
        assert result.name == testString, \
            'FAILED TO GET RESOURCE CATEGORY'

    def test_getOrderRequest(self):
        new_resource = user.newResource(testString)
        entity = user.newOrderRequest(resource_id=new_resource.id)
        result = user.getOrderRequest(entity.id)
        assert result.name == testString, \
            'FAILED TO GET ORDER REQUEST'

    def test_getWorkspace(self):
        entity = user.newWorkspace(testString)
        result = user.getWorkspace(entity.id)
        assert result.name == testString, \
            'FAILED TO GET WORKSPACE'

    def test_getFile(self):
        entity = user.newFile('./tests/test_user.py')
        result = user.getFile(entity.id)
        assert result.id == entity.id, \
            'FAILED TO GET FILE'

    # getMany()
    def test_getExperiments(self):
        result = user.getExperiments()
        assert result[0].id, \
            'FAILED TO GET EXPERIMENTS'

    def test_getProtocols(self):
        result = user.getProtocols()
        assert result[0].id, \
            'FAILED TO GET PROTOCOLS'

    def test_getResources(self):
        result = user.getResources()
        assert result[0].id, \
            'FAILED TO GET RESOURCES'

    def test_getResourceCategorys(self):
        result = user.getResourceCategorys()
        assert result[0].id, \
            'FAILED TO GET RESOURCE CATEGORYS'

    def test_getResourceLocations(self):
        result = user.getResourceLocations()
        assert result[0].id, \
            'FAILED TO GET RESOURCE LOCATIONS'

    def test_getOrderRequests(self):
        result = user.getOrderRequests()
        assert result[0].id, \
            'FAILED TO GET ORDER REQUESTS'

    def test_getOrderRequestsWithFilter(self):
        result = user.getOrderRequests(status='new')
        assert result[0].id, \
            'FAILED TO GET ORDER REQUESTS WITH FILTER'

    def test_getTags(self):
        result = user.getTags()
        assert result[0].id, \
            'FAILED TO GET TAGS'

    def test_getWorkspaces(self):
        result = user.getWorkspaces()
        assert result[0].id, \
            'FAILED TO GET WORKSPACES'

    def test_getFiles(self):
        result = user.getFiles()
        assert result[0].id, \
            'FAILED TO GET FILES'

    # newEntity()
    def test_newExperiment(self):
        result = user.newExperiment(testString)
        assert result.name == testString, \
            'FAILED TO CREATE NEW EXPERIMENT'

    def test_newProtocol(self):
        result = user.newProtocol(testString)
        assert result.name == testString, \
            'FAILED TO CREATE NEW PROTOCOL'

    def test_newResource(self):
        result = user.newResource(testString)
        assert result.name == testString, \
            'FAILED TO CREATE NEW RESOURCE'

    def test_newResourceCategory(self):
        result = user.newResourceCategory(testString)
        assert result.name == testString, \
            'FAILED TO CREATE NEW RESOURCE CATEGORY'

    def test_newResourceLocation(self):
        result = user.newResourceLocation('testLocation')
        result.delete()
        assert result.name == 'testLocation', \
            'FAILED TO CREATE NEW RESOURCE LOCATION'

    def test_newOrderRequest(self):
        entity = user.newResource(testString)
        result = user.newOrderRequest(resource_id=entity.id)
        assert result.name == testString, \
            'FAILED TO CREATE NEW ORDER REQUEST'

    def test_newTag(self):
        result = user.newTag('test_newTag', type='experiment_workflow')
        result.delete()
        assert result.name == 'test_newTag', \
            'FAILED TO CREATE NEW TAG'

    def test_newWorkspace(self):
        result = user.newWorkspace(testString)
        assert result.name == testString, \
            'FAILED TO CREATE NEW WORKSPACE'

    def test_newFile(self):
        result = user.newFile('./tests/test_user.py')
        assert result is not None, \
            'FAILED TO ADD NEW FILE'
