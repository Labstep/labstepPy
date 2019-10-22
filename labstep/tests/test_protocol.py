#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from random import randrange

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Variables as in test_setup.py
testName = 'Api Default Name'
testComment = 'Api Default Comment'
testFilePath = './labstep/tests/test_setup.py'

# Get the entity
getOne = testUser.getProtocol(10924)
protocol = LS.Protocol(getOne, testUser)

# Set variables for editting
randomNum = randrange(1, 9)
editName = 'Api Pytest Name Edit {n}'.format(n=randomNum)


class TestProtocol:
    def test_edit(self):
        result = protocol.edit(editName)
        assert result['name'] == editName, \
            'INCORRECT EDITTED PROTOCOL NAME!'

    def test_delete(self):
        # test_delete the 1st protocol from the getMany list
        getMany = testUser.getProtocols(search_query='pytest')
        getOne = testUser.getProtocol(getMany[0]['id'])
        protocol = LS.Protocol(getOne, testUser)

        result = protocol.delete()
        assert result['deleted_at'] is not None, \
            'FAILED TO DELETE PROTOCOL'

    def test_comment(self):
        result = protocol.comment(testComment, testFilePath)
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    # def test_addTag(self):
    #     result = protocol.addTag(testName)
    #     assert result, \
    #         'FAILED TO ADD TAG'
