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
protocol.addComment(testName)
protocol.addComment(testName)
data = {
    "rowCount": 6,
    "columnCount": 6,
    "colHeaderData": {},
    "data": {
        "dataTable": {
            0: {
                0: {
                    "value": 'Cell A1'
                },
                1: {
                    "value": 'Cell B1'
                }
            }
        }
    }
}
protocol.addTable(name=testName, data=data)
protocol = testUser.getProtocol(protocol.id)
exp_protocol = entity.addProtocol(protocol)
entity = testUser.getExperiment(entity.id)


class TestExperiment:
    def test_edit(self):
        result = entity.edit('Pytest Edited', 'Description Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT EXPERIMENT'

    def test_delete(self):
        entityToDelete = testUser.newExperiment(testName)
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE EXPERIMENT'

    def test_addProtocol(self):
        get_protocol = testUser.newProtocol('Test')
        result = entity.addProtocol(get_protocol)
        assert result is not None, \
            'FAILED TO ADD PROTOCOL TO EXPERIMENT'

    def test_getProtocols(self):
        result = entity.getProtocols()
        assert result[0].id is not None, \
            'FAILED TO GET PROTOCOLS'

    def test_addComment(self):
        result = entity.addComment(testName, './tests/test_experiment.py')
        assert result is not None, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result is not None, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result[0].id is not None, \
            'FAILED TO GET TAGS'

    # ExperimentStep
    def test_getSteps(self):
        result = exp_protocol.getSteps()
        assert result[0].id is not None, \
            'FAILED TO GET STEPS'

    def test_completeStep(self):
        steps = exp_protocol.getSteps()
        result = steps[0].complete()
        assert result.ended_at is not None, \
            'FAILED TO COMPLETE STEP'

    def test_commenting_on_comments(self):
        comment = entity.getComments()[0]
        comment.addComment('test')
        comment = comment.getComments()[0]
        assert comment.body == 'test',\
            'FAILED COMMENT COMMENTING TEST'

    def test_getDataElements(self):
        dataElements = entity.getDataElements()
        assert len(dataElements) == 0

    def test_addDataElementTo(self):
        entity.addDataElement('testField', fieldType="default",)
        newEntity = testUser.getExperiment(entity.id)
        dataElements = newEntity.getDataElements()
        assert len(dataElements) == 1

    def test_addMaterial(self):
        resource = testUser.newResource('test')
        resource_item = resource.newItem('test')
        entity.addMaterial('testMaterial',
                           amount=10,
                           units='uL',
                           resource_id=resource.id,
                           resource_item_id=resource_item.id)
        material = entity.getMaterials()[0]
        assert material.name == 'testMaterial' \
            and material.amount == '10' \
            and material.units == 'uL' \
            and material.resource['id'] == resource.id \
            and material.resource_item['id'] == resource_item.id \


    def test_signatures(self):
        sig = entity.addSignature('test', lock=True)
        sigs = entity.getSignatures()
        sig.revoke()
        assert sig.id == sigs[0].id \
            and sig.statement == 'test' \
            and sig.revoked_at is not None, \
            'FAILED SIGNATURES TEST'
