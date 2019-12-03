#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newProtocol(testName)
entity = testUser.getProtocol(new_entity.id)


class TestProtocol:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT PROTOCOL'

    def test_delete(self):
        entityToDelete = testUser.newProtocol(testName)
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE PROTOCOL'

    def test_addComment(self):
        result = entity.addComment(testName, './tests/test_protocol.py')
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result, \
            'FAILED TO GET TAGS'
