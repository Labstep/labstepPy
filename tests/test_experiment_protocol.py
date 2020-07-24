#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import user, experimentProtocol

# Make new entity
experiment_protocol = experimentProtocol(user)


class TestExperimentProtocol:
    def test_edit(self):
        experiment_protocol.edit(name='Edit Test')
        experiment_protocol.update()
        assert experiment_protocol.name == 'Edit Test'

    def test_getDataElements(self):
        dataElements = experiment_protocol.getDataElements()
        assert len(dataElements) == 0

    def test_addDataElementTo(self):
        result = experiment_protocol.addDataElement(
            fieldType="default", fieldName="test")
        assert result.label == 'test'

    def test_addMaterial(self):
        resource = user.newResource('test')
        item = resource.newItem('test')
        material = experiment_protocol.addMaterial('testMaterial',
                                                   amount=10,
                                                   units='uL',
                                                   resource_id=resource.id,
                                                   resource_item_id=item.id)

        assert material.name == 'testMaterial' \
            and material.amount == '10' \
            and material.units == 'uL' \
            and material.resource['id'] == resource.id \
            and material.resource_item['id'] == item.id
