#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
resource = testUser.newResource(testName)
entity = resource.newItem(name='Pytest Acetone')


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

    def test_addMetadata(self):
        new_resource = testUser.newResource(testName)
        result = new_resource.addMetadata(fieldName=testName, value=testName)
        assert result.label == testName, \
            'FAILED TO ADD METADATA'

    def test_getMetadatas(self):
        result = entity.getMetadatas()
        assert result[0].name is not None, \
            'FAILED TO GET METADATA'
