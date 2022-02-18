#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from .fixtures import workspace, resource, resourceCategory, authUser, testString, loadFixtures
from .shared import sharedTests


class TestResource:
    @pytest.fixture
    def entity(self):
        return resource()

    @pytest.fixture
    def category(self):
        return resourceCategory()

    @pytest.fixture
    def workspaceToShare(self):
        return workspace()

    def setup_method(self):
        loadFixtures('Python\\\\Resource')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_commenting(self, entity):
        assert sharedTests.commenting(entity)

    def test_metadata(self, entity):
        assert sharedTests.metadata(entity)

    def test_tagging(self, entity):
        assert sharedTests.tagging(entity)

    def test_sharelink(self, entity):
        assert sharedTests.sharelink(entity)

    def test_sharing(self, entity, workspaceToShare):
        assert sharedTests.sharing(entity, workspaceToShare)

    def test_setResourceCategory(self, entity, category):
        entity.setResourceCategory(category.id)
        resourceCategoryFromGet = entity.getResourceCategory()
        assert resourceCategoryFromGet.id == category.id

    def test_newOrderRequest(self, entity):
        result = entity.newOrderRequest()
        assert result.status

    def test_getData(self, entity):
        user = authUser()
        exp = user.newExperiment('Test')
        data = exp.addDataField('Test', value='test')
        inventoryField = exp.addInventoryField(resource_id=entity.id)
        data.linkToInventoryField(inventoryField)
        result = entity.getData()
        assert result[0].id == data.id

    def test_newItem(self, entity):
        result = entity.newItem(name=testString)
        assert result.id

    def test_getItems(self, entity):
        item = entity.newItem()
        result = entity.getItems()
        assert result[0].id == item.id

    def test_enableItemTemplate(self, entity):
        entity.enableCustomItemTemplate()
        itemTemplate = entity.getItemTemplate()
        assert itemTemplate.deleted_at is None

    def test_disableItemTemplate(self, entity):
        entity.enableCustomItemTemplate()
        entity.disableCustomItemTemplate()
        itemTemplate = entity.getItemTemplate()
        assert itemTemplate.deleted_at is not None
