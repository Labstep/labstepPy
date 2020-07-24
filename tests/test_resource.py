#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import user, resource, testString

# Make new entity
entity = resource(user)


class TestResource:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT RESOURCE'

    def test_delete(self):
        entityToDelete = user.newResource('testDelete')
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE RESOURCE'

    def test_addComment(self):
        result = entity.addComment(testString, './tests/test_resource.py')
        assert result is not None, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result[0].id is not None, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testString)
        assert result is not None, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result[0].id is not None, \
            'FAILED TO GET TAGS'

    def test_addMetadata(self):
        result = entity.addMetadata(fieldName=testString, value=testString)
        assert result.label == testString, \
            'FAILED TO ADD METADATA'

    def test_getMetadata(self):
        result = entity.getMetadata()
        assert result[0].id is not None, \
            'FAILED TO GET METADATA'

    def test_setResourceCategory(self):
        my_resourceCategory = user.getResourceCategorys()[0]
        result = entity.setResourceCategory(my_resourceCategory.id)
        assert result.resource_category is not None, \
            'FAILED TO ADD METADATA'

    def test_newOrderRequest(self):
        result = entity.newOrderRequest()
        assert result.status, \
            'FAILED TO MAKE NEW ORDER REQUEST'

    def test_newItem(self):
        result = entity.newItem(name=testString)
        assert result.id, \
            'FAILED TO MAKE NEW ITEM'

    def test_getItems(self):
        result = entity.getItems()
        assert result[0].id, \
            'FAILED TO GET ITEMS'
