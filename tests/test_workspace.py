#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newWorkspace(testName)
entity = testUser.getWorkspace(new_entity.id)
my_workspace = testUser.setWorkspace(entity)


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
        test_exp = testUser.newExperiment(testName)
        test_exp.addTag(testName)
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

    def test_getTags(self):
        new_tag = testUser.newTag('test_newTag')
        result = entity.getTags()
        new_tag.delete()
        assert result[0].id, \
            'FAILED TO GET TAGS'
