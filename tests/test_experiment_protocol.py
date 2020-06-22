#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

testUser = labstep.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = labstep.helpers.getTime()

# Make new entity
new_entity = testUser.newExperiment(testName)
entity = testUser.getExperiment(new_entity.id)
protocol = testUser.newProtocol('Test')
protocol = testUser.getProtocol(protocol.id)
experiment_protocol = entity.addProtocol(protocol)


class TestExperimentProtocol:
    def test_edit(self):
        experiment_protocol.edit(name='Edit Test')
        experiment_protocol.update()
        assert experiment_protocol.name == 'Edit Test'

    def test_getDataElements(self):
        dataElements = experiment_protocol.getDataElements()
        assert len(dataElements) == 0

    def test_addDataElementTo(self):
        experiment_protocol.addDataElement(
            fieldType="default", fieldName="test")
        newEntity = testUser.getExperiment(entity.id)
        experiment_protocols = newEntity.getProtocols()
        assert len(experiment_protocols) == 1
        refreshed_experiment_protocol = experiment_protocols[0]
        dataElements = refreshed_experiment_protocol.getDataElements()
        assert len(dataElements) == 1

    def test_addMaterial(self):
        resource = testUser.newResource('test')
        resource_item = resource.newItem('test')
        experiment_protocol.addMaterial('testMaterial',
                                        amount=10,
                                        units='uL',
                                        resource_id=resource.id,
                                        resource_item_id=resource_item.id)

        updated_exp = testUser.getExperiment(new_entity.id)
        updated_exp_protocol = updated_exp.getProtocols()[0]
        material = updated_exp_protocol.getMaterials()[0]
        assert material.name == 'testMaterial' \
            and material.amount == '10' \
            and material.units == 'uL' \
            and material.resource['id'] == resource.id \
            and material.resource_item['id'] == resource_item.id
