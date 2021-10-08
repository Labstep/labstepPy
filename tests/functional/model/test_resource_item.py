#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from fixtures import resourceItem, loadFixtures, authUser
from shared import sharedTests


class TestResourceItem:

    @pytest.fixture
    def entity(self):
        return resourceItem()

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
        material = exp.addMaterial(
            resource_id=entity.resource['id'], resource_item_id=entity.id)
        data.linkToMaterial(material)
        result = entity.getData()
        assert result[0].id == data.id
