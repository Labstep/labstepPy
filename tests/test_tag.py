#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newTag(testName)
entity = testUser.getTags()[0]


class TestTag:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT TAG NAME!'

    def test_delete(self):
        result = entity.delete()
        assert result is None, \
            'FAILED TO DELETE TAG'
