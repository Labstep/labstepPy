#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from .fixtures import resourceItem, loadFixtures, authUser, resourceLocation
from .shared import sharedTests


class TestResourceItem:

    @pytest.fixture
    def entity(self):
        return resourceItem()

    @pytest.fixture
    def location(self):
        return resourceLocation()

    def setup_method(self):
        loadFixtures('Python\\\\ResourceItem')

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_commenting(self, entity):
        assert sharedTests.commenting(entity)

    def test_metadata(self, entity):
        assert sharedTests.metadata(entity)

    def test_getData(self, entity):
        user = authUser()
        exp = user.newExperiment('Test')
        data = exp.addDataField('Test', value='test')
        inventoryField = exp.addInventoryField(
            resource_id=entity.resource['id'], resource_item_id=entity.id)
        data.linkToInventoryField(inventoryField)
        result = entity.getData()
        assert result[0].id == data.id

    def test_setLocation(self, entity, location):

        entity.setLocation(location['guid'], position=[5, 10])

        loc = entity.getLocation()

        assert loc['resource_location']['guid'] == location['guid']
        assert loc['position'] == [5, 10]
        assert loc['size'] == [1, 1]

    def test_edit_quantity_params(self, entity):
        
        entity.edit(amount=100,unit = 'L')
        
        assert entity.amount == '100.0' and entity.unit == 'L'

        entity.edit(quantity_amount=None,quantity_unit = None)
        
        assert entity.amount == None and entity.unit == None