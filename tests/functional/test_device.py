#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from .fixtures import device, loadFixtures

from .shared import sharedTests


class TestDevice:
    @pytest.fixture
    def entity(self):
        return device()

    def setup_method(self):
        loadFixtures('Python\\\\Device')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_addDataNumber(self, entity):
        data = entity.addData('Test', 'numeric', number=13, unit='oC')
        assert data.name == 'Test' \
            and data.type == 'numeric' \
            and data.number == 13, \
            'FAILED TO CREATE DATA'

    def test_addDataFile(self, entity):
        data = entity.addData(
            'Test', 'file', filepath='./tests/data/sample.txt')
        assert data.name == 'Test' \
            and data.files is not None, \
            'FAILED TO CREATE DATA'

    def test_addDataText(self, entity):
        data = entity.addData('Test', 'text', text='Testings')
        assert data.name == 'Test' \
            and data.type == 'default' \
            and data.value == 'Testings', \
            'FAILED TO CREATE DATA'

    def test_getData(self, entity):
        first_data = entity.addData('Test', text='Words')
        data = entity.getData(search_query='Test')
        assert data[0].id == first_data.id
