#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

import labstep

testUser = labstep.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = labstep.helpers.getTime()

# Make new entity
new_entity = testUser.newResourceCategory(testName)
entity = testUser.getResourceCategory(new_entity.id)
entity.addMetadata(fieldName='test', value=testName)
entity.addComment(testName)


class TestResourceCategory:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT RESOURCE CATEGORY'

    def test_delete(self):
        entityToDelete = testUser.newResourceCategory('testDelete')
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE RESOURCE CATEGORY'

    def test_addComment(self):
        result = entity.addComment(testName, './tests/test_resource_category.py')
        assert result is not None, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result[0].id is not None, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result is not None, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result[0].id is not None, \
            'FAILED TO GET TAGS'

    def test_addMetadata(self):
        new_resource_category = testUser.newResourceCategory(testName)
        result = new_resource_category.addMetadata(fieldName=testName,
                                                   value=testName)
        assert result.label == testName, \
            'FAILED TO ADD METADATA'

    def test_getMetadata(self):
        result = entity.getMetadata()
        assert result[0].id is not None, \
            'FAILED TO GET METADATA'
