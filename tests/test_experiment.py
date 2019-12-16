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
get_protocol = testUser.getProtocols()[0]
exp_prot = entity.addProtocol(get_protocol)


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
        get_protocol = testUser.getProtocols()[0]
        result = entity.addProtocol(get_protocol)
        assert result, \
            'FAILED TO ADD PROTOCOL TO EXPERIMENT'

    def test_getProtocols(self):
        result = entity.getProtocols()
        assert result[0].id is not None, \
            'FAILED TO GET PROTOCOLS'

    def test_addComment(self):
        result = entity.addComment(testName, './tests/test_experiment.py')
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result[0].id is not None, \
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result[0].id is not None, \
            'FAILED TO GET TAGS'
    
    def test_getSteps(self):
        exp_prot = entity.getProtocols()[0]
        result = exp_prot.getSteps()
        assert result is not None, \
            'FAILED TO GET STEPS'

    def test_completeStep(self):
        result = exp_prot.getSteps()
        completedStep = result[0].complete()
        assert completedStep is not None, \
            'FAILED TO COMPLETE STEP'

    """ def test_addMaterial(self):
        result = entity.addMaterial()
        assert result is not None, \
            'FAILED TO ADD MATERIAL' """

    def test_getMaterials(self):
        result = exp_prot.getMaterials() 
        assert result is not None, \
            'FAILED TO GET MATERIALS'

    """ def test_addTimer(self):
        result = entity.addTimer()
        assert result is not None, \
            'FAILED TO ADD TIMER' """

    def test_getTimers(self):
        result = exp_prot.getTimers() 
        assert result is not None, \
            'FAILED TO GET TIMERS'

    """ def test_addTable(self):
        result = entity.addTable()
        assert result is not None, \
            'FAILED TO ADD TABLE' """
    
    def test_getTables(self):
        result = exp_prot.getTables() 
        assert result is not None, \
            'FAILED TO GET TABLES'