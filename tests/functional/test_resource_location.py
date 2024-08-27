#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest

from .fixtures import fixtures
from .shared import sharedTests


class TestResourceLocation:

    @pytest.fixture
    def entity(self):
        return fixtures.resourceLocation()

    @pytest.fixture
    def item(self):
        return fixtures.resourceItem()
    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_commenting(self, entity):
        assert sharedTests.commenting(entity)

    def test_metadata(self, entity):
        assert sharedTests.metadata(entity)

    def test_getItems(self, entity, item):
        item.edit(resource_location_guid=entity.guid)
        items = entity.getItems()
        assert items[0].id == item.id
        assert items[0].guid == item.guid

    def test_innerLocations(self, entity):

        new_location = entity.addInnerLocation('Test')

        assert new_location.outer_location['id'] == entity.id
        assert new_location.name == 'Test'

        inner_locations = entity.getInnerLocations()

        assert inner_locations[0].id == new_location.id
        assert inner_locations[0].guid == new_location.guid

    def test_createPositionMap(self, entity):

        entity.createPositionMap(rowCount=10, columnCount=5)

        entity.update()

        assert entity.map_data == {
            'rowCount': 10,
            'columnCount': 5,
            'data': []
        }

    def test_setOuterLocation(self, entity):

        outer_location = fixtures.resourceLocation()

        entity.setOuterLocation(
            outer_location.guid, position=[1, 3], size=[2, 2])

        entity.update()

        assert entity.outer_location['guid'] == outer_location.guid
