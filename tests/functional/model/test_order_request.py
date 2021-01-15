#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from fixtures import user, orderRequest, testString

# Make new entity
entity = orderRequest()


class TestOrderRequest:
    def test_edit(self):
        result = entity.edit(status="Back orDEred")
        assert result.status == 'back_ordered', \
            'FAILED TO EDIT ORDER REQUEST'

    def test_delete(self):
        test_resource = user.newResource('testDelete')
        entityToDelete = test_resource.newOrderRequest()
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE ORDER REQUEST'

    def test_getResource(self):
        result = entity.getResource()
        assert result.id is not None, \
            'FAILED TO GET RESOURCE'

    def test_addComment(self):
        result = entity.addComment(testString, './tests/data/sample.txt')
        assert result is not None, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result is not None, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testString)
        assert result is not None, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result is not None, \
            'FAILED TO GET TAGS'

    def test_addMetadata(self):
        result = entity.addMetadata(fieldName=testString, value=testString)
        assert result.label == testString, \
            'FAILED TO ADD METADATA'

    def test_getMetadata(self):
        result = entity.getMetadata()
        assert result is not None, \
            'FAILED TO GET METADATA'

    def test_getSharelink(self):
        sharelink = entity.getSharelink()
        assert sharelink is not None
