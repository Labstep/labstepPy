#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from random import randrange

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Get the entity
getOne = testUser.getWorkspace(11339)
workspace = LS.Workspace(getOne, testUser)

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
        result = LS.Workspace(workspaceToDelete, testUser).delete()
        assert result['deleted_at'] is not None, \
            'FAILED TO DELETE WORKSPACE'
