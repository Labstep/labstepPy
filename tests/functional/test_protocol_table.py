#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from labstep.service.helpers import dataFrameToDataTable, dataTableToDataFrame


class TestExperimentTable:
    @pytest.fixture
    def entity(self):
        return fixtures.protocol()

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_getDataFrame(self, entity):
        data = {
            "rowCount": 12,
            "columnCount": 12,
            "colHeaderData": {},
            "data": {
                "dataTable": {
                    0: {
                        0: {
                            "value": 'Column 1'
                        },
                        1: {
                            "value": 'Column 2'
                        }
                    },
                    2: {
                        0: {
                            "value": "A1"
                        },
                        1: {
                            "value": "B1"
                        }
                    }
                }
            }
        }
        table = entity.addTable(name='Test', data=data)
        df = table.getDataFrame()
        assert df['Column 1'][0] == 'A1' \
            and df['Column 2'][0] == 'B1'

    def test_dataFrameToDataTable(self, entity):

        data = {
            "rowCount": 2,
            "columnCount": 2,
            "colHeaderData": {},
            "data": {
                "dataTable": {
                    '0': {
                        '0': {
                            "value": 'Column 1'
                        },
                        '1': {
                            "value": 'Column 2'
                        }
                    },
                    '1': {
                        '0': {
                            "value": "A1"
                        },
                        '1': {
                            "value": "B1"
                        }
                    }
                }
            }
        }

        table = entity.addTable(name='Test', data=data)

        df = table.getDataFrame()

        dt = dataFrameToDataTable(df)

        table = table.edit(data=dt)

        assert dt == data
