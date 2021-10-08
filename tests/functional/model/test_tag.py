#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from fixtures import tag, loadFixtures

from shared import sharedTests


class TestTag:
    @pytest.fixture
    def entity(self):
        return tag()

    def setup_method(self):
        loadFixtures('Python')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert entity.delete() is None
