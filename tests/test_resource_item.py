#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import testString, resource, resourceItem

# Make new entity
entity = resourceItem()


class TestResource:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT RESOURCE ITEM'

    def test_delete(self):
        entityToDelete = resource().newItem('testDelete')
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE RESOURCE ITEM'

    def test_addComment(self):
        result = entity.addComment(testString, './tests/test_resource.py')
        assert result is not None, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result[0].id is not None, \
            'FAILED TO GET COMMENTS'

    def test_addMetadata(self):
        result = entity.addMetadata(fieldName=testString, value=testString)
        assert result.label == testString, \
            'FAILED TO ADD METADATA'

    def test_getMetadata(self):
        result = entity.getMetadata()
        assert result[0].id is not None, \
            'FAILED TO GET METADATA'
