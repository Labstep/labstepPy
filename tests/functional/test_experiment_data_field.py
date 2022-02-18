#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from .fixtures import experimentDataField, experimentInventoryField, loadFixtures, authUser
from .shared import sharedTests


class TestExperimentDataField:

    @pytest.fixture
    def entity(self):
        return experimentDataField()

    @pytest.fixture
    def inventoryField(self):
        return experimentInventoryField()

    def setup_method(self):
        loadFixtures('Python\\\\Metadata')

    def test_edit(self, entity):
        result = entity.edit(fieldName='Pytest Edited')
        assert result.label == 'Pytest Edited'

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_link_to_inventory_field(self):
        user = authUser()
        exp = user.newExperiment('Test')
        data = exp.addDataField('Test')
        inventoryField = exp.addInventoryField('Test')
        data.linkToInventoryField(inventoryField)
        linkedInventoryFields = data.getLinkedInventoryFields()
        assert linkedInventoryFields[0].id == inventoryField.id

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
                                 'options': {
                                     "values": {
                                         "A": False,
                                         "B": True,
                                         "C": False
                                     },
                                     "is_allow_add": False,
                                     "is_allow_multiple": False
                                 }})
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
        file = entity.__user__.newFile('./tests/data/sample.txt')
        entity.edit(extraParams={'type': 'file'})
        fileValue = entity.setValue(file).getValue()
        assert defaultValue == 'New' \
            and numericValue == float(450) \
            and dateValue == "2021-10-28" \
            and dateTimeValue == "2021-10-28 18:09:00" \
            and singleOptions == 'A' \
            and multiOptions == ['B', 'C'] \
            and fileValue.id == file.id
