#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Default Name'

# Make new entity
new_entity = testUser.newExperiment(testName)
entity = testUser.getExperiment(new_entity.id)


class TestExperiment:
    def test_edit(self):
        result = entity.edit('Edited Name', 'Edited Description')
        assert result.name == 'Edited Name', \
            'FAILED TO EDIT EXPERIMENT'

    def test_delete(self):
        entityToDelete = testUser.newExperiment(testName)
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE EXPERIMENT'

    def test_addProtocol(self):
        get_protocol = testUser.getProtocols()[0]
        result = entity.addProtocol(get_protocol)
        assert result, \
            'FAILED TO ADD PROTOCOL TO EXPERIMENT'

    def test_comment(self):
        result = entity.addComment(testName, './tests/test_experiments.py')
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'
