# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures, proseMirrorState, testString
from .shared import sharedTests


class TestProtocol:

    @pytest.fixture
    def entity(self):
        return fixtures.protocol()

    @pytest.fixture
    def protocolWithLastVersion(self):
        return fixtures.protocolWithLastVersion()

    @pytest.fixture
    def collection(self):
        return fixtures.protocolCollection()

    @pytest.fixture
    def workspaceToShare(self):
        return fixtures.workspace()
    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Protocol')

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

    def test_new_version(self, protocolWithLastVersion):
        oldId = protocolWithLastVersion.last_version['id']
        result = protocolWithLastVersion.newVersion()
        assert result.id == protocolWithLastVersion.id \
            and result.draft_version['id'] != oldId

    def test_jupyter_notebooks(self, entity):
        assert sharedTests.jupyterNotebooks(entity)

    def test_protocol_conditions(self, entity):
        assert sharedTests.protocolConditions(entity)

    def test_assign(self, entity):
        assert sharedTests.assign(entity)
