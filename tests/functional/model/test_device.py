#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from fixtures import newString, device

class TestDevice:
    def test_edit(self):
        entity = device()
        newName = newString()
        result = entity.edit(newName)
        assert result.name == newName, \
            'FAILED TO EDIT DEVICE NAME'

    def test_delete(self):
        entityToDelete = device()
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE DEVICE'

    def test_addData_Number(self):
        entity = device()
        data = entity.addData('Test', 'numeric', number=13, unit='oC')
        assert data.name == 'Test' \
            and data.type == 'numeric' \
            and data.number == 13, \
            'FAILED TO CREATE DATA'

    def test_addData_File(self):
        entity = device()
        data = entity.addData('Test', 'file', filepath='./tests/data/sample.txt')
        assert data.name == 'Test' \
            and data.file is not None, \
            'FAILED TO CREATE DATA'

    def test_addData_Text(self):
        entity = device()
        data = entity.addData('Test', 'text', text='Testings')
        assert data.name == 'Test' \
            and data.type == 'default' \
            and data.value == 'Testings', \
            'FAILED TO CREATE DATA'

    def test_getData(self):
        entity = device()
        first_data = entity.addData('Test', text='Words')
        data = entity.getData(search_query='Test')
        assert data[0].id == first_data.id
