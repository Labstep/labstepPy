#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

testUser = labstep.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = labstep.helpers.getTime()

# Make new entity
new_entity = testUser.newResource(testName)
entity = new_entity.addMetadata(fieldName=testName, value=testName)


class TestMetadata:
    def test_edit(self):
        result = entity.edit(fieldName='Pytest Edited')
        assert result.label == 'Pytest Edited', \
            'FAILED TO EDIT METADATA'

    def test_delete(self):
        entityToDelete = new_entity.addMetadata(fieldName='testDelete',
                                                value='testDelete')
        result = entityToDelete.delete()
        assert result is None, \
            'FAILED TO DELETE METADATA'
