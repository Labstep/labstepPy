#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from .fixtures import metadata, resource, testString, loadFixtures
from .shared import sharedTests


class TestMetadata:

    @pytest.fixture
    def entity(self):
        return metadata()

    def setup_method(self):
        loadFixtures('Python\\\\Metadata')

    def test_edit(self, entity):
        result = entity.edit(fieldName='Pytest Edited')
        assert result.label == 'Pytest Edited'

    def test_delete(self, entity):
        assert sharedTests.delete(entity)
