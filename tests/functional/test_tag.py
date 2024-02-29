#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures

from .shared import sharedTests


class TestTag:
    @pytest.fixture
    def entity(self):
        return fixtures.tag()

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert entity.delete() is None
