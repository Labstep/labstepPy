#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from random import randrange

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Get the entity
workspace = testUser.getWorkspace(11344)

# Set variables for editting
randomNum = randrange(1, 9)
editName = 'Api Pytest Name Edit {n}'.format(n=randomNum)


class TestWorkspace:
    def test_edit(self):
        result = workspace.edit(editName)
        assert result.name == editName, \
            'INCORRECT EDITTED WORKSPACE NAME!'

    def test_delete(self):
        workspaceToDelete = testUser.newWorkspace('testDelete')
        result = workspaceToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE WORKSPACE'
