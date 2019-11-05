#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from random import randrange

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Variables as in setup for test
testName = 'Api Default Name'
testComment = 'Api Default Comment'
testFilePath = './tests/test_resource.py'

# Get the entity
resource = testUser.getResource(405415)

# Set variables for editting
randomNum = randrange(1, 9)
editName = 'Api Pytest Name Edit {n}'.format(n=randomNum)


class TestResource:
    def test_edit(self):
        result = resource.edit(editName)
        assert result.name == editName, \
            'INCORRECT RESOURCE NAME!'

    def test_delete(self):
        resourceToDelete = testUser.newResource('testDelete')
        result = resourceToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE RESOURCE'

    def test_comment(self):
        result = resource.addComment(testComment, testFilePath)
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = resource.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'
