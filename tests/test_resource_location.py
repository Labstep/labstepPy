#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import user, resourceLocation, testString, newString

entity = resourceLocation()

class TestResourceLocation:
    def test_edit(self):
        newName = newString()
        result = entity.edit(newName)
        result.delete()
        assert result.name == newName, \
            'FAILED TO EDIT RESOURCE LOCATION'

    def test_delete(self):
        entityToDelete = user.newResourceLocation(newString())
        result = entityToDelete.delete()
        assert result is None, \
            'FAILED TO DELETE RESOURCE LOCATION'

    # def test_addComment(self):
    #     result = entity.addComment(testName,
    #                                './tests/test_resource_location.py')
    #     assert result is not None, \
    #         'FAILED TO ADD COMMENT AND FILE'

    # def test_addTag(self):
    #     result = entity.addTag(testName)
    #     assert result is not None, \
    #         'FAILED TO ADD TAG'
