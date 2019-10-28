#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from random import randrange

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Variables as in test_setup.py
testName = 'Api Default Name'
testComment = 'Api Default Comment'
testFilePath = './tests/test_resource.py'

# Get the entity
getOne = testUser.getResource(405415)
resource = LS.Resource(getOne, testUser)

# Set variables for editting
randomNum = randrange(1, 9)
editName = 'Api Pytest Name Edit {n}'.format(n=randomNum)


class TestResource:
    def test_edit(self):
        result = resource.edit(editName)
        assert result['name'] == editName, \
            'INCORRECT RESOURCE NAME!'

    def test_delete(self):
        # test_delete the 1st resource from the getMany list
        resourceToDelete = testUser.newResource('testDelete')
        result = resourceToDelete.delete()
        assert result['deleted_at'] is not None, \
            'FAILED TO DELETE RESOURCE'

    def test_comment(self):
        result = resource.comment(testComment, testFilePath)
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = resource.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'
