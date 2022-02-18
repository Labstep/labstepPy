#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from .fixtures import orderRequest, workspace, loadFixtures

from .shared import sharedTests


class TestOrderRequest:
    @pytest.fixture
    def entity(self):
        return orderRequest()

    @pytest.fixture
    def workspaceToShare(self):
        return workspace()

    def setup_method(self):
        loadFixtures('Python\\\\OrderRequest')

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
