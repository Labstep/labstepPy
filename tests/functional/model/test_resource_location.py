#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from fixtures import resourceLocation, testString, loadFixtures, resourceItem
from shared import sharedTests


class TestResourceLocation:

    @pytest.fixture
    def entity(self):
        return resourceLocation()

    @pytest.fixture
    def item(self):
        return resourceItem()

    def setup_method(self):
        loadFixtures('Python')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_commenting(self, entity):
        assert sharedTests.commenting(entity)

    def test_metadata(self, entity):
        assert sharedTests.metadata(entity)

    def test_getItems(self, entity, item):
        item.edit(resource_location_id=entity.id)
        items = entity.getItems()
        assert items[0].id == item.id
