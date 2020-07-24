#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

from fixtures import protocolWithElements, tableData, contentStateEmpty

testUser = labstep.login('apitest@labstep.com', 'apitestpass')
testName = labstep.helpers.getTime()

entity = protocolWithElements(testUser)


class TestProtocol:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited',\
            'FAILED TO EDIT PROTOCOL'

    def test_delete(self):
        entityToDelete = testUser.newProtocol(testName)
        result = entityToDelete.delete()
        assert result.deleted_at is not None,\
            'FAILED TO DELETE PROTOCOL'

    def test_addComment(self):
        result = entity.addComment(testName, './tests/test_protocol.py')
        assert result is not None,\
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result[0].id is not None,\
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testName)
        assert result is not None,\
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result[0].id is not None,\
            'FAILED TO GET TAGS'

    def test_addSteps(self):
        result = entity.addSteps(2)
        assert len(result) == 2

    def test_getSteps(self):
        result = entity.getSteps()
        assert result[0].id is not None,\
            'FAILED TO GET STEPS'

    def test_addMaterial(self):
        result = entity.addMaterial(name=testName, amount='2.0', units='ml')
        assert result is not None,\
            'FAILED TO ADD MATERIAL'

    def test_getMaterials(self):
        result = entity.getMaterials()
        assert result[0].id is not None,\
            'FAILED TO GET MATERIALS'

    def test_editMaterial(self):
        material = entity.getMaterials()[0]
        result = material.edit(name='New Sample Name')
        assert result.name == 'New Sample Name',\
            'FAILED TO EDIT MATERIAL'

    def test_addTimer(self):
        result = entity.addTimer(name=testName, minutes=20, seconds=30)
        assert result is not None,\
            'FAILED TO ADD TIMER'

    def test_getTimers(self):
        result = entity.getTimers()
        assert result[0].id is not None,\
            'FAILED TO GET TIMERS'

    def test_editTimer(self):
        timer = entity.getTimers()[0]
        result = timer.edit(minutes=17)
        assert result.minutes == 17,\
            'FAILED TO EDIT TIMER'

    def test_addTable(self):
        result = entity.addTable(name=testName, data=tableData)
        assert result is not None,\
            'FAILED TO ADD TABLE'

    def test_getTables(self):
        result = entity.getTables()
        assert result[0].id is not None,\
            'FAILED TO GET TABLES'

    def test_editTable(self):
        table = entity.getTables()[0]
        result = table.edit(name=testName)
        assert result.name == testName,\
            'FAILED TO EDIT TABLE'

    def test_getDataElements(self):
        dataElements = entity.getDataElements()
        assert len(dataElements) == 0

    def test_addDataElement(self):
        entity.addDataElement(fieldType="default", fieldName="test")
        newEntity = testUser.getProtocol(entity.id)
        dataElements = newEntity.getDataElements()
        assert len(dataElements) == 1

    def test_edit_content_state(self):
        result = entity.edit(name='updated', content_state=contentStateEmpty)
        assert result.last_version['content_state'] == contentStateEmpty,\
            'FAILED TO EDIT PROTOCOL CONTENT STATE'

    def test_new_version(self):
        oldId = entity.last_version['id']
        result = entity.newVersion()
        assert result.id == entity.id \
            and result.last_version['id'] != oldId,\
            'FAILED TO EDIT PROTOCOL'
