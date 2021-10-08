#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from fixtures import (
    experiment,
    protocol,
    resource,
    workspace,
    proseMirrorState,
    experimentCollection,
    loadFixtures
)

from shared import sharedTests


class TestExperiment:
    @pytest.fixture
    def entity(self):
        return experiment()

    @pytest.fixture
    def protocolToAdd(self):
        return protocol()

    @pytest.fixture
    def resourceToAdd(self):
        return resource()

    @pytest.fixture
    def workspaceToShare(self):
        return workspace()

    @pytest.fixture
    def collection(self):
        return experimentCollection()

    def setup_method(self):
        loadFixtures('Python\\\\Experiment')

    def test_edit(self):
        entity = experiment()
        entity.edit('Pytest Edited', entry=proseMirrorState)
        entity.update()
        assert entity.name == 'Pytest Edited' and \
            entity.getEntry() == proseMirrorState

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_commenting(self, entity):
        assert sharedTests.commenting(entity)

    def test_tagging(self, entity):
        assert sharedTests.tagging(entity)

    def test_sharelink(self, entity):
        assert sharedTests.sharelink(entity)

    def test_sharing(self, entity, workspaceToShare):
        assert sharedTests.sharing(entity, workspaceToShare)

    def test_collections(self, entity, collection):
        assert sharedTests.collections(entity, collection)

    def test_files(self, entity):
        assert sharedTests.files(entity)

    def test_dataFields(self, entity):
        assert sharedTests.dataFields(entity)

    def test_tables(self, entity):
        assert sharedTests.tables(entity)

    def test_protocols(self, entity, protocolToAdd):
        protocolAdded = entity.addProtocol(protocolToAdd)
        result = entity.getProtocols()
        assert result[0].id == protocolAdded.id

    def test_materials(self, entity, resourceToAdd):
        resource_item = resourceToAdd.newItem('test')
        entity.addMaterial('testMaterial',
                           amount=10,
                           units='uL',
                           resource_id=resourceToAdd.id,
                           resource_item_id=resource_item.id)
        material = entity.getMaterials()[0]
        assert material.name == 'testMaterial' \
            and material.amount == '10' \
            and material.units == 'uL' \
            and material.resource['id'] == resourceToAdd.id \
            and material.resource_item['id'] == resource_item.id \


    def test_signatures(self):
        entity = experiment()
        sig = entity.addSignature('test', lock=True)
        sigs = entity.getSignatures()
        sig.revoke()
        assert sig.id == sigs[0].id \
            and sig.statement == 'test' \
            and sig.revoked_at is not None

    def test_signatureRequests(self):
        entity = experiment()
        request = entity.requestSignature(2, message='test')
        requests = entity.getSignatureRequests()
        request.cancel()
        assert request.id == requests[0].id \
            and request.message == 'test' \
            and request.deleted_at is not None