#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Variables as in setup for test
testName = 'Api Default Name'
testDescription = 'Api Default Description'
testFilePath = './tests/test_user.py'

# New variables for this script
testNewName = 'Api Pytest New Name'
testNewDescription = 'Api Pytest New Description'
testSearch = 'api'


class TestUser:
    # getSingle()
    def test_getExperiment(self):
        result = testUser.getExperiment(23973)
        assert result.name == testName, \
            'INCORRECT EXPERIMENT NAME!'
        assert result.description == testDescription, \
            'INCORRECT EXPERIMENT DESCRIPTION!'

    def test_getProtocol(self):
        result = testUser.getProtocol(10918)
        assert result.name == testName, \
            'INCORRECT PROTOCOL NAME!'

    def test_getResource(self):
        result = testUser.getResource(405412)
        assert result.name == testName, \
            'INCORRECT RESOURCE NAME!'

    def test_getWorkspace(self):
        result = testUser.getWorkspace(11339)
        assert result.name == testName, \
            'INCORRECT WORKSPACE NAME!'

    # getMany()
    def test_getExperiments(self):
        result = testUser.getExperiments(search_query=testSearch)
        assert result[0].name, \
            'FAILED TO GET EXPERIMENTS!'

    def test_getProtocols(self):
        result = testUser.getProtocols(search_query=testSearch)
        assert result[0].name, \
            'FAILED TO GET PROTOCOLS!'

    def test_getResources(self):
        result = testUser.getResources(search_query=testSearch)
        assert result[0].name, \
            'FAILED TO GET RESOURCES!'

    def test_getTags(self):
        result = testUser.getTags(search_query=testSearch)
        assert result[0].name, \
            'FAILED TO GET TAGS!'

    def test_getWorkspaces(self):
        result = testUser.getWorkspaces(name=testSearch)
        assert result[0].name, \
            'FAILED TO GET WORKSPACES!'

    # newEntity()
    def test_newExperiment(self):
        result = testUser.newExperiment(testNewName, testNewDescription)
        assert result.name == testNewName, \
            'INCORRECT NEW EXPERIMENT NAME!'
        assert result.description == testNewDescription, \
            'INCORRECT NEW EXPERIMENT DESCRIPTION!'

    def test_newProtocol(self):
        result = testUser.newProtocol(testNewName)
        assert result.name == testNewName, \
            'INCORRECT NEW PROTOCOL NAME!'

    def test_newResource(self):
        result = testUser.newResource(testNewName)
        assert result.name == testNewName, \
            'INCORRECT NEW RESOURCE NAME!'

    """ def test_newTag(self):
        result = testUser.newTag(testNewName)
        result.delete()
        assert result.name == testNewName, \
            'INCORRECT NEW TAG NAME!' """

    def test_newWorkspace(self):
        result = testUser.newWorkspace(testNewName)
        assert result.name == testNewName, \
            'INCORRECT NEW WORKSPACE NAME!'

    def test_newFile(self):
        result = testUser.newFile(testFilePath)
        assert result, \
            'FAILED TO ADD NEW FILE!'
