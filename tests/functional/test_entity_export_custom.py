#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from labstep.entities.export.repository import getExports, newExport


class TestEntityExportCustom:
    @pytest.fixture
    def testWorkspace(self):
        return fixtures.workspace()

    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\EntityExportCustom')

    def test_custom_export(self, user, testWorkspace):
        file = user.newFile(__file__)

        exportFromCreate = newExport(
            user,
            testWorkspace,
            type='custom',
            extraParams={
                'file_id': file.id,
                'group_id': testWorkspace.id
            }
        )
        exportFromGet = getExports(
            user,
            type='custom',
            extraParams={
                'group_id': testWorkspace.id
            }
        )[0]

        assert exportFromCreate.id == exportFromGet.id

    def test_get_processed_at_from(self, user):
        notFoundExports = getExports(
            user,
            type='custom',
            extraParams={
                'group_id': 1,
                'processed_at_from': '2023-01-01T00:00:00+0000'
            }
        )
        assert len(notFoundExports) == 0

        allExports = getExports(
            user,
            type='custom',
            extraParams={
                'group_id': 1
            }
        )
        assert len(allExports) == 2

        foundExports = getExports(
            user,
            type='custom',
            extraParams={
                'group_id': 1,
                'processed_at_from': '2022-01-01T00:00:00+0000'
            }
        )
        assert len(foundExports) == 1
