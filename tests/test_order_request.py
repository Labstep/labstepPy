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
entity.addMetadata(fieldName='test', value=testName)
entity.addComment(testName)


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

    def test_getResource(self):
        result = entity.getResource()
        assert result.id == new_resource.id, \
            'FAILED TO GET METADATA'

    def test_addComment(self):
        result = entity.addComment(testName, './tests/test_order_request.py')
        assert result is not None, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result is not None, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result is not None, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result is not None, \
            'FAILED TO GET TAGS'

    def test_addMetadata(self):
        result = entity.addMetadata(fieldName=testName, value=testName)
        assert result.label == testName, \
            'FAILED TO ADD METADATA'

    def test_getMetadata(self):
        result = entity.getMetadata()
        assert result is not None, \
            'FAILED TO GET METADATA'
