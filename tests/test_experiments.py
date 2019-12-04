#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from random import randrange

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Variables as in setup for test
testName = 'Api Default Name'
testComment = 'Api Default Comment'
testFilePath = './tests/test_experiments.py'

# Get the entity
experiment = testUser.getExperiment(24495)

# Set variables for editting
randomNum = randrange(1, 9)
editName = 'Api Pytest Name Edit {n}'.format(n=randomNum)
editDescription = 'Api Pytest Description Edit {n}'.format(n=randomNum)


class TestExperiment:
    def test_edit(self):
        result = experiment.edit(editName, editDescription)
        assert result.name == editName, \
            'INCORRECT EDITTED EXPERIMENT NAME!'
        assert result.description == editDescription, \
            'INCORRECT EDITTED EXPERIMENT DESCRIPTION!'

    def test_delete(self):
        experimentToDelete = testUser.newExperiment('testDelete')
        result = experimentToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE EXPERIMENT'

    def test_addProtocol(self):
        get_protocol = testUser.getProtocol(4926)
        result = experiment.addProtocol(get_protocol)
        assert result, \
            'FAILED TO ADD PROTOCOL TO EXPERIMENT'

    def test_comment(self):
        result = experiment.addComment(testComment, testFilePath)
        assert result, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = experiment.addTag(testName)
        assert result, \
            'FAILED TO ADD TAG'
