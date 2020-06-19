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

    def test_getMaterials(self):
        materials = experiment_protocol.getMaterials()
        assert len(materials) == 0

    def test_addMaterial(self):
        resource = testUser.newResource('test')
        resource_item = resource.newItem('test')
        experiment_protocol.addMaterial('testMaterial',
                                        amount=10,
                                        units='uL',
                                        resource=resource,
                                        resource_item=resource_item)
        material = experiment_protocol.getMaterials()[0]
        assert material.name == 'testMaterial' \
            and material.amount == 10 \
            and material.unit == 'uL' \
            and material.resource['id'] == resource.id \
            and material.resource_item['id'] == resource_item.id
