#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from random import randrange

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Get the entity
entity = testUser.getExperiment(23976)
exp = LS.Experiment(entity, testUser)

# Set variables
randomNum = randrange(1, 5)
editName = 'Api Pytest Name Edit {n}'.format(n=randomNum)
editDescription = 'Api Pytest Description Edit {n}'.format(n=randomNum)


class TestExperiment:
    def test_edit(self):
        result = exp.edit(editName, editDescription)
        assert result.name == editName, \
            'INCORRECT EDITTED EXPERIMENT NAME!'
        assert result.description == editDescription, \
            'INCORRECT EDITTED EXPERIMENT DESCRIPTION!'
