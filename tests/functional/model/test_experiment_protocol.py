#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from fixtures import experimentProtocol, proseMirrorState, resource

# Make new entity
experiment_protocol = experimentProtocol()


class TestExperimentProtocol:
    def test_edit(self):
        experiment_protocol.edit(name='Edit Test')
        experiment_protocol.update()
        assert experiment_protocol.name == 'Edit Test'

    def test_edit_body(self):
        experiment_protocol.edit(body=proseMirrorState)
        experiment_protocol.update()
        assert experiment_protocol.getBody() == proseMirrorState

    def test_getDataElements(self):
        dataElements = experiment_protocol.getDataElements()
        assert len(dataElements) == 0

    def test_addDataElementTo(self):
        result = experiment_protocol.addDataElement(
            fieldType="default", fieldName="test")
        assert result.label == 'test'

    def test_addMaterial(self):
        newResource = resource()
        item = newResource.newItem('test')
        material = experiment_protocol.addMaterial('testMaterial',
                                                   amount=10,
                                                   units='uL',
                                                   resource_id=newResource.id,
                                                   resource_item_id=item.id)

        assert material.name == 'testMaterial' \
            and material.amount == '10' \
            and material.units == 'uL' \
            and material.resource['id'] == newResource.id \
            and material.resource_item['id'] == item.id

    def test_editMaterial(self):
        material = experiment_protocol.getMaterials()[0]
        result = material.edit(name='New Sample Name')
        assert result.name == 'New Sample Name',\
            'FAILED TO EDIT MATERIAL'

    # ExperimentStep
    def test_addSteps(self):
        result = experiment_protocol.addSteps(2)
        assert len(result) == 2

    def test_getSteps(self):
        result = experiment_protocol.getSteps()
        assert result[0].id is not None, \
            'FAILED TO GET STEPS'

    def test_completeStep(self):
        steps = experiment_protocol.getSteps()
        result = steps[0].complete()
        assert result.ended_at is not None, \
            'FAILED TO COMPLETE STEP'

    def test_addFile(self):
        entity = experimentProtocol()
        file = entity.addFile('./tests/data/sample.txt')
        files = entity.getFiles()
        assert files[0].id == file.id
