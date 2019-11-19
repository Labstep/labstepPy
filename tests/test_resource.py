#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Default Name'

# Make new entity
new_entity = testUser.newResource(testName)
entity = testUser.getResource(new_entity.id)


class TestResource:
    def test_edit(self):
        result = entity.edit('Edited Name')
        assert result.name == 'Edited Name', \
            'FAILED TO EDIT RESOURCE'

    def test_delete(self):
        entityToDelete = testUser.newResource('testDelete')
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE RESOURCE'

    def test_comment(self):
        result = entity.addComment(testName, './tests/test_resource.py')
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'
