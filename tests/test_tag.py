#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'test_newTag'


class TestTag:
    def test_edit(self):
        entity = testUser.newTag(testName)
        result = entity.edit('Pytest Edited')
        result.delete()
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT TAG NAME!'

    def test_delete(self):
        entity = testUser.newTag(testName)
        result = entity.delete()
        assert result is None, \
            'FAILED TO DELETE TAG'
