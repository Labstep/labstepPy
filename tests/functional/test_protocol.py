# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import (
    workspace,
    protocol,
    tableData,
    testString,
    proseMirrorState,
    protocolCollection,
    loadFixtures
)
from .shared import sharedTests


class TestProtocol:

    @pytest.fixture
    def entity(self):
        return protocol()

    @pytest.fixture
    def collection(self):
        return protocolCollection()

    @pytest.fixture
    def workspaceToShare(self):
        return workspace()

    def setup_method(self):
        loadFixtures('Python\\\\Protocol')

    def test_edit(self, entity):
        result = entity.edit(name=testString, body=proseMirrorState)
        assert result.getBody() == proseMirrorState \
            and result.name == testString

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_commenting(self, entity):
        assert sharedTests.commenting(entity)

    def test_tagging(self, entity):
        assert sharedTests.tagging(entity)

    def test_sharelink(self, entity):
        assert sharedTests.sharelink(entity)

    def test_sharing(self, entity, workspaceToShare):
        assert sharedTests.sharing(entity, workspaceToShare)

    def test_steps(self, entity):
        assert sharedTests.steps(entity)

    def test_inventory_fields(self, entity):
        assert sharedTests.inventoryFields(entity)

    def test_timers(self, entity):
        assert sharedTests.timers(entity)

    def test_tables(self, entity):
        assert sharedTests.tables(entity)

    def test_dataFields(self, entity):
        assert sharedTests.dataFields(entity)

    def test_files(self, entity):
        assert sharedTests.files(entity)

    def test_collections(self, entity, collection):
        assert sharedTests.collections(entity, collection)

    def test_new_version(self, entity):
        oldId = entity.last_version['id']
        result = entity.newVersion()
        assert result.id == entity.id \
            and result.last_version['id'] != oldId
    
    def test_jupyter_notebooks(self, entity):
        assert sharedTests.jupyterNotebooks(entity)
