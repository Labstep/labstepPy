#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newTag(testName)
entity = new_entity


class TestTag:
    def test_edit(self):
        result = entity.edit('Edited Name')
        assert result.name == 'Edited Name', \
            'FAILED TO EDIT TAG NAME!'

    def test_delete(self):
        result = entity.delete()
        assert result is None, \
            'FAILED TO DELETE TAG'
