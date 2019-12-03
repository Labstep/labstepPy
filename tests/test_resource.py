#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newResource(testName)
entity = testUser.getResource(new_entity.id)
entity.addMetadata(fieldName='test', value=testName)
entity.addComment(testName)


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

    def test_getComments(self):
        result = entity.getComments()
        assert result, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result, \
            'FAILED TO GET TAGS'

    def test_addMetadata(self):
        result = entity.addMetadata(fieldName=testName, value=testName)
        assert result.label == testName, \
            'FAILED TO ADD METADATA'

    def test_getMetadata(self):
        result = entity.getMetadata()
        assert result, \
            'FAILED TO GET METADATA'

    def test_setResourceCategory(self):
        my_resourceCategory = testUser.getResourceCategorys()[0]
        result = entity.setResourceCategory(my_resourceCategory)
        assert result.resource_category is not None, \
            'FAILED TO ADD METADATA'

    def test_newOrderRequest(self):
        result = entity.newOrderRequest()
        assert result.status, \
            'FAILED TO MAKE NEW ORDER REQUEST'
