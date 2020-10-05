#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fixtures import (user, protocol, tableData, testString,
                      proseMirrorState, protocolCollection)

entity = protocol()


class TestProtocol:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited',\
            'FAILED TO EDIT PROTOCOL'

    def test_delete(self):
        entityToDelete = user.newProtocol(testString)
        result = entityToDelete.delete()
        assert result.deleted_at is not None,\
            'FAILED TO DELETE PROTOCOL'

    def test_addComment(self):
        result = entity.addComment(testString, './tests/test_protocol.py')
        assert result is not None,\
            'FAILED TO ADD COMMENT AND FILE'

    def test_getComments(self):
        result = entity.getComments()
        assert result[0].id is not None,\
            'FAILED TO GET COMMENTS'

    def test_addTag(self):
        result = entity.addTag(testString)
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
        result = entity.addMaterial(name=testString, amount='2.0', units='ml')
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
        result = entity.addTimer(name=testString, minutes=20, seconds=30)
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
        result = entity.addTable(name=testString, data=tableData)
        assert result is not None,\
            'FAILED TO ADD TABLE'

    def test_getTables(self):
        result = entity.getTables()
        assert result[0].id is not None,\
            'FAILED TO GET TABLES'

    def test_editTable(self):
        table = entity.getTables()[0]
        result = table.edit(name=testString)
        assert result.name == testString,\
            'FAILED TO EDIT TABLE'

    def test_getDataElements(self):
        dataElements = entity.getDataElements()
        assert len(dataElements) == 0

    def test_addDataElement(self):
        entity.addDataElement(fieldType="default", fieldName="test")
        newEntity = user.getProtocol(entity.id)
        dataElements = newEntity.getDataElements()
        assert len(dataElements) == 1

    def test_edit_body(self):
        result = entity.edit(name='updated', body=proseMirrorState)
        assert result.getBody() == proseMirrorState,\
            'FAILED TO EDIT PROTOCOL STATE'

    def test_new_version(self):
        oldId = entity.last_version['id']
        result = entity.newVersion()
        assert result.id == entity.id \
            and result.last_version['id'] != oldId,\
            'FAILED TO EDIT PROTOCOL'

    def test_getSharelink(self):
        sharelink = entity.getSharelink()
        assert sharelink is not None

    def test_addToCollection(self):
        collection = protocolCollection()
        entity.addToCollection(collection.id)
        result = entity.getCollections()
        assert result[0].id == collection.id

    def test_removeFromCollection(self):
        collection = protocolCollection()
        entity.addToCollection(collection.id)
        entity.removeFromCollection(collection.id)
        result = entity.getCollections()
        assert len(result) == 0
