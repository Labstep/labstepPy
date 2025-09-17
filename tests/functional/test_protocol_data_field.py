#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures
from .shared import sharedTests


class TestDataField:

    @pytest.fixture
    def entity(self):
        return fixtures.protocolDataField()

    @pytest.fixture
    def inventoryField(self):
        return fixtures.experimentInventoryField()
    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Metadata')

    def test_edit(self, entity):
        result = entity.edit(fieldName='Pytest Edited')
        assert result.label == 'Pytest Edited'

    def test_delete(self, entity):
        assert sharedTests.delete(entity)
