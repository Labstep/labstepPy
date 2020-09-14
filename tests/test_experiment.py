#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import (experiment, protocol, resource,
                      testString, proseMirrorState)

entity = experiment()


class TestExperiment:
    def test_edit(self):

        entity.edit('Pytest Edited', entry=proseMirrorState)
        entity.update()
        assert entity.name == 'Pytest Edited' and \
            entity.entry == proseMirrorState,\
            'FAILED TO EDIT EXPERIMENT'

    def test_delete(self):
        entityToDelete = experiment()
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE EXPERIMENT'

    def test_addProtocol(self):
        get_protocol = protocol(empty=True)
        result = entity.addProtocol(get_protocol)
        assert result is not None, \
            'FAILED TO ADD PROTOCOL TO EXPERIMENT'

    def test_getProtocols(self):
        result = entity.getProtocols()
        assert result[0].id is not None, \
            'FAILED TO GET PROTOCOLS'

    def test_addComment(self):
        result = entity.addComment(testString, './tests/test_experiment.py')
        assert result is not None, \
            'FAILED TO ADD COMMENT AND FILE'

    def test_addTag(self):
        result = entity.addTag(testString)
        assert result is not None, \
            'FAILED TO ADD TAG'

    def test_getTags(self):
        result = entity.getTags()
        assert result[0].id is not None, \
            'FAILED TO GET TAGS'

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
        entity.addDataElement('testField', fieldType="default")
        entity.update()
        dataElements = entity.getDataElements()
        assert len(dataElements) == 1

    def test_addMaterial(self):
        test_resource = resource()
        resource_item = test_resource.newItem('test')
        entity.addMaterial('testMaterial',
                           amount=10,
                           units='uL',
                           resource_id=test_resource.id,
                           resource_item_id=resource_item.id)
        material = entity.getMaterials()[1]
        assert material.name == 'testMaterial' \
            and material.amount == '10' \
            and material.units == 'uL' \
            and material.resource['id'] == test_resource.id \
            and material.resource_item['id'] == resource_item.id \


    def test_signatures(self):
        sig = entity.addSignature('test', lock=True)
        sigs = entity.getSignatures()
        sig.revoke()
        assert sig.id == sigs[0].id \
            and sig.statement == 'test' \
            and sig.revoked_at is not None, \
            'FAILED SIGNATURES TEST'

    def test_getSharelink(self):
        sharelink = entity.getSharelink()
        assert sharelink is not None
