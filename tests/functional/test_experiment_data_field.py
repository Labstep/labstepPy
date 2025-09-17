#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures
from .shared import sharedTests


class TestExperimentDataField:

    @pytest.fixture
    def entity(self):
        return fixtures.experimentDataField()

    @pytest.fixture
    def inventoryField(self):
        return fixtures.experimentInventoryField()

    @pytest.fixture
    def device(self):
        return fixtures.device()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Metadata')

    def test_edit(self, entity):
        result = entity.edit(fieldName='Pytest Edited')
        assert result.label == 'Pytest Edited'

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_device_data(self, entity, device):
        deviceData = device.addData(fieldName='Numeric Test',
                                    fieldType='numeric',
                                    number=10,
                                    unit='K')

        entity.edit(extraParams={'type': 'numeric',
                    'device_data_id': deviceData.id})

        assert entity.getValue() == float(10)

    def test_get_set_value(self, entity):
        entity.edit(extraParams={'type': 'default', 'value': 'Test'})
        defaultValue = entity.setValue('New').getValue()
        entity.edit(extraParams={'type': 'numeric',
                                 'number': 45, 'unit': 'mL'})
        numericValue = entity.setValue(450).getValue()
        entity.edit(extraParams={'type': 'date',
                                 'date': "2021-10-20T16:09:00+01:00"})
        dateValue = entity.setValue("2021-10-28").getValue()
        entity.edit(extraParams={'type': 'datetime',
                                 'date': "2021-10-20T16:09:00+01:00"})
        dateTimeValue = entity.setValue("2021-10-28 18:09").getValue()
        entity.edit(extraParams={'type': 'options',
                                 'options': None})
        singleOptions = entity.setValue('A').getValue()
        entity.edit(extraParams={'type': 'options',
                                 'options': {
                                     "values": {
                                         "A": True,
                                         "B": True,
                                         "C": False
                                     },
                                     "is_allow_add": False,
                                     "is_allow_multiple": True
                                 }})
        multiOptions = entity.setValue(['B', 'C']).getValue()
        file = entity.__user__.newFile(__file__)
        entity.edit(extraParams={'type': 'file'})
        fileValue = entity.setValue(file).getValue()
        assert defaultValue == 'New' \
            and numericValue == float(450) \
            and dateValue == "2021-10-28" \
            and dateTimeValue == "2021-10-28 18:09:00" \
            and singleOptions == 'A' \
            and multiOptions == ['B', 'C'] \
            and fileValue.id == file.id
