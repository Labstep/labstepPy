#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from random import randrange

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Variables as in setup for test
testName = 'Api Default Name'
testComment = 'Api Default Comment'
testFilePath = './tests/test_order_request.py'

# Get the entity
orderRequest = testUser.getOrderRequest(405415)

# Set variables for editting
randomNum = randrange(1, 9)
editName = 'Api Pytest Name Edit {n}'.format(n=randomNum)


class TestOrderRequest:
    def test_edit(self):
        result = orderRequest.edit(editName)
        assert result.name == editName, \
            'INCORRECT RESOURCE NAME!'

    def test_delete(self):
        orderRequestToDelete = testUser.newOrderRequest('testDelete')
        result = orderRequestToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE RESOURCE'

    def test_comment(self):
        result = orderRequest.addComment(testComment, testFilePath)
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = orderRequest.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'
