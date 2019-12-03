#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newResource(testName)
entity = testUser.getResource(new_entity.id)


class TestResource:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT RESOURCE'

    def test_delete(self):
        entityToDelete = testUser.newResource('testDelete')
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE RESOURCE'

    def test_addComment(self):
        result = entity.addComment(testName, './tests/test_resource.py')
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'

    def test_addMetadata(self):
        new_resource = testUser.newResource(testName)
        result = new_resource.addMetadata(fieldName=testName, value=testName)
        assert result.label == testName, \
            'FAILED TO ADD METADATA'

    def test_getMetadata(self):
        new_resource = testUser.newResource(testName)
        result = new_resource.addMetadata(fieldName=testName, value=testName)
        assert result.label == testName, \
            'FAILED TO GET METADATA'

    def test_setResourceCategory(self):
        my_resourceCategory = testUser.getResourceCategorys()[0]
        result = entity.setResourceCategory(my_resourceCategory)
        assert result.resource_category is not None, \
            'FAILED TO SET RESOURCE CATEGORY'

    def test_newOrderRequest(self):
        result = entity.newOrderRequest()
        assert result.status, \
            'FAILED TO MAKE NEW ORDER REQUEST'
