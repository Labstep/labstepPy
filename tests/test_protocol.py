#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newProtocol(testName)
entity = testUser.getProtocol(new_entity.id)
entity.addComment(testName)


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
        assert result[0].id is not None, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result[0].id is not None, \
            'FAILED TO GET TAGS'

    def test_getSteps(self):
        result = entity.getSteps()
        assert result is not None, \
            'FAILED TO GET STEPS'

    def test_addMaterial(self):
        result = entity.addMaterial()
        assert result is not None, \
            'FAILED TO ADD MATERIAL'

    def test_getMaterials(self):
        result = entity.getMaterials()
        assert result is not None, \
            'FAILED TO GET MATERIALS'

    def test_addTimer(self):
        result = entity.addTimer()
        assert result is not None, \
            'FAILED TO ADD TIMER'

    def test_getTimers(self):
        result = entity.getTimers()
        assert result is not None, \
            'FAILED TO GET TIMERS'

    def test_addTable(self):
        result = entity.addTable()
        assert result is not None, \
            'FAILED TO ADD TABLE'
    
    def test_getTables(self):
        result = entity.getTables()
        assert result is not None, \
            'FAILED TO GET TABLES'
