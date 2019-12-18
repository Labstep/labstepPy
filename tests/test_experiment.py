#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = 'Api Pytest'

# Make new entity
new_entity = testUser.newExperiment(testName)
entity = testUser.getExperiment(new_entity.id)
entity.addComment(testName)
exp_protocol = entity.addProtocol(testUser.getProtocol(4926))
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
        get_protocol = testUser.getProtocol(4926)
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

    def test_getComments(self):
        result = entity.getComments()
        assert result[0].id is not None, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result is not None, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result[0].id is not None, \
            'FAILED TO GET TAGS'

    # ExperimentMaterial
    # def test_addMaterial(self):
    #     result = entity.addMaterial()
    #     assert result is not None, \
    #         'FAILED TO ADD MATERIAL'

    def test_getMaterials(self):
        result = exp_protocol.getMaterials()
        assert result[0].id is not None, \
            'FAILED TO GET MATERIALS'

    def test_editMaterial(self):
        material = exp_protocol.getMaterials()[0]
        result = material.edit(amount='0.1', units='ml')
        assert result.value == '0.1', \
            'FAILED TO EDIT MATERIAL'

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

    # ExperimentTable
    # def test_addTable(self):
    #     result = entity.addTable(data=data)
    #     assert result is not None, \
    #         'FAILED TO ADD TABLE'

    def test_getTables(self):
        result = exp_protocol.getTables()
        assert result[0].id is not None, \
            'FAILED TO GET TABLES'

    # ExperimentTimer
    # def test_addTimer(self):
    #     result = entity.addTimer()
    #     assert result is not None, \
    #         'FAILED TO ADD TIMER'

    def test_getTimers(self):
        result = exp_protocol.getTimers()
        assert result[0].id is not None, \
            'FAILED TO GET TIMERS'

    def test_editTimer(self):
        timer = exp_protocol.getTimers()[0]
        result = timer.edit(minutes=17)
        assert result.minutes == 17, \
            'FAILED TO EDIT TIMER'