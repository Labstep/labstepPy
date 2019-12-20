#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

testUser = labstep.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = labstep.helpers.getTime()


class TestResourceLocation:
    def test_edit(self):
        entity = testUser.newResourceLocation(testName)
        result = entity.edit('Pytest Edited')
        result.delete()
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT RESOURCE LOCATION'

    def test_delete(self):
        entityToDelete = testUser.newResourceLocation('testDelete')
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
