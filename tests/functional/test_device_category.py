#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
# pylama:ignore=E501
import pytest
from .fixtures import deviceCategory, workspace, loadFixtures
from .shared import sharedTests


class TestDeviceCategory:

    @pytest.fixture
    def entity(self):
        return deviceCategory()

    @pytest.fixture
    def workspaceToShare(self):
        return workspace()

    def setup_method(self):
        loadFixtures('Python')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_metadata(self, entity):
        assert sharedTests.metadata(entity.getDeviceTemplate())