#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from fixtures import resource, testString

# Make new entity
new_entity = resource()
entity = new_entity.addMetadata(fieldName=testString, value=testString)


class TestMetadata:
    def test_edit(self):
        result = entity.edit(fieldName='Pytest Edited')
        assert result.label == 'Pytest Edited', \
            'FAILED TO EDIT METADATA'

    def test_delete(self):
        entityToDelete = new_entity.addMetadata(fieldName='testDelete',
                                                value='testDelete')
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE METADATA'
