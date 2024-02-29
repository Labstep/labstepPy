#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures

from .shared import sharedTests


class TestOrderRequest:
    @pytest.fixture
    def entity(self):
        return fixtures.orderRequest()

    @pytest.fixture
    def workspaceToShare(self):
        return fixtures.workspace()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\OrderRequest')

    def test_edit(self, entity):
        result = entity.edit(status="Back orDEred")
        assert result.status == 'back_ordered'

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

    def test_assign(self, entity):
        assert sharedTests.assign(entity)
