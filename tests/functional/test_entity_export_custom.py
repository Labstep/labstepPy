#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from .fixtures import authUser, workspace, loadFixtures
from labstep.entities.export.repository import getExports, newExport


class TestEntityExportCustom:
    @pytest.fixture
    def testWorkspace(self):
        return workspace()

    @pytest.fixture
    def user(self):
        return authUser()

    def setup_method(self):
        loadFixtures('Python\\\\EntityExportCustom')

    def test_custom_export(self, user, testWorkspace):
        file = user.newFile('./tests/data/sample.txt')

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
