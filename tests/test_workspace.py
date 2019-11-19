#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Default Name'

# Make new entity
new_entity = testUser.newWorkspace(testName)
entity = testUser.getWorkspace(new_entity.id)


class TestWorkspace:
    def test_edit(self):
        result = entity.edit('Edited Name')
        assert result.name == 'Edited Name', \
            'FAILED TO EDIT WORKSPACE'

    def test_delete(self):
        entityToDelete = testUser.newWorkspace(testName)
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE WORKSPACE'

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
