#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newResourceCategory(testName)
entity = testUser.getResourceCategory(new_entity.id)


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
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'
