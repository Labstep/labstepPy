#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
resource = testUser.newResource(testName)
entity = resource.newItem(name='Pytest Acetone')
entity.addMetadata(fieldName='test', value=testName)
entity.addComment(testName)


class TestResource:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT RESOURCE ITEM'

    def test_delete(self):
        entityToDelete = resource.newItem('testDelete')
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE RESOURCE ITEM'

    def test_addComment(self):
        result = entity.addComment(testName, './tests/test_resource.py')
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result, \
            'FAILED TO GET COMMENTS'

    def test_addMetadata(self):
        result = entity.addMetadata(fieldName=testName, value=testName)
        assert result.label == testName, \
            'FAILED TO ADD METADATA'

    def test_getMetadata(self):
        result = entity.getMetadata()
        assert result[0].label is not None, \
            'FAILED TO GET METADATA'
