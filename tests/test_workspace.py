#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Default Name'

# Make new entity
new_entity = testUser.newWorkspace(testName)
entity = testUser.getWorkspace(new_entity.id)


class TestWorkspace:
    def test_edit(self):
        result = entity.edit('Edited Name')
        assert result.name == 'Edited Name', \
            'FAILED TO EDIT WORKSPACE'

    def test_delete(self):
        entityToDelete = testUser.newWorkspace(testName)
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE WORKSPACE'
