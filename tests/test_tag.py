#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

testUser = labstep.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = labstep.helpers.getTime()


class TestTag:
    def test_edit(self):
        entity = testUser.newTag(testName, 'experiment_workflow')
        newName = labstep.helpers.getTime()
        result = entity.edit(newName)
        result.delete()
        assert result.name == newName, \
            'FAILED TO EDIT TAG NAME'

    def test_delete(self):
        testName = labstep.helpers.getTime()
        entityToDelete = testUser.newTag(testName, 'experiment_workflow')
        result = entityToDelete.delete()
        assert result is None, \
            'FAILED TO DELETE TAG'
