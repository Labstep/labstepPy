#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import newString, instrument


class TestInstrument:
    def test_edit(self):
        entity = instrument()
        newName = newString()
        result = entity.edit(newName)
        assert result.name == newName, \
            'FAILED TO EDIT INSTRUMENT NAME'

    def test_delete(self):
        entityToDelete = instrument()
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE INSTRUMENT'

    def test_newData(self):
        entity = instrument()
        data = entity.newData('Test', 'numeric', 13, 'oC')
        assert data.name == 'Test' \
            and data.type == 'numeric' \
            and data.number == 13, \
            'FAILED TO CREATE DATA'

    def test_getData(self):
        entity = instrument()
        first_data = entity.newData('Test', text='Words')
        data = entity.getData(search_query='Test')
        assert data[0].id - first_data.id
