#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_resource = testUser.newResource(testName)
new_entity = new_resource.newOrderRequest()
entity = testUser.getOrderRequest(new_entity.id)


class TestOrderRequest:
    def test_edit(self):
        result = entity.edit(status="Back orDEred")
        assert result.status == 'back_ordered', \
            'FAILED TO EDIT ORDER REQUEST'

    def test_delete(self):
        test_resource = testUser.newResource('testDelete')
        entityToDelete = test_resource.newOrderRequest()
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE ORDER REQUEST'

    def test_addComment(self):
        result = entity.addComment(testName, './tests/test_order_request.py')
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'
