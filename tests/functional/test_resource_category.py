#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
# pylama:ignore=E501
import pytest

from .fixtures import fixtures
from .shared import sharedTests


class TestResourceCategory:

    @pytest.fixture
    def entity(self):
        return fixtures.resourceCategory()

    @pytest.fixture
    def workspaceToShare(self):
        return fixtures.workspace()
    def setup_method(self):
        fixtures.loadFixtures('Python\\\\ResourceCategory')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_metadata(self, entity):
        assert sharedTests.metadata(entity.getResourceTemplate())

    def test_sharelink(self, entity):
        assert sharedTests.sharelink(entity)

    def test_sharing(self, entity, workspaceToShare):
        assert sharedTests.sharing(entity, workspaceToShare)

    def test_itemTemplate(self, entity):
        entity.enableItemTemplate()
        enabledItemTemplate = entity.getItemTemplate()
        entity.disableItemTemplate()
        disabledItemTemplate = entity.getItemTemplate()
        assert enabledItemTemplate.deleted_at is None \
            and disabledItemTemplate.deleted_at is not None
