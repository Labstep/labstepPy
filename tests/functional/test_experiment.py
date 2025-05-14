#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures, proseMirrorState, testString
from .shared import sharedTests


class TestExperiment:
    @pytest.fixture
    def entity(self):
        return fixtures.experiment()

    @pytest.fixture
    def protocolToAdd(self):
        return fixtures.protocolWithLastVersion()

    @pytest.fixture
    def resourceToAdd(self):
        return fixtures.resource()

    @pytest.fixture
    def workspaceToShare(self):
        return fixtures.workspace()

    @pytest.fixture
    def collection(self):
        return fixtures.experimentCollection()

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self):
        entity = fixtures.experiment()
        entity.edit('Pytest Edited', entry=proseMirrorState)
        entity.update()
        assert entity.name == 'Pytest Edited' and \
            entity.getEntry() == proseMirrorState

    def test_locking(self, entity):
        lockedEntity = entity.lock()
        assert lockedEntity.locked_at is not None
        unlockedEntity = entity.unlock()
        assert unlockedEntity.locked_at is None

    def test_complete(self, entity):
        entity.complete()
        assert entity.ended_at is not None
        entity.complete('2020-12-01 12:22')
        assert entity.ended_at == '2020-12-01T12:22:00+00:00'

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

    def test_inventory_fields(self, entity, resourceToAdd):
        resource_item = resourceToAdd.newItem('test')
        entity.addInventoryField('testInventoryField',
                                 amount=10,
                                 units='uL',
                                 resource_id=resourceToAdd.id,
                                 resource_item_id=resource_item.id)
        inventoryField = entity.getInventoryFields()[0]
        assert inventoryField.name == 'testInventoryField' \
            and inventoryField.amount == '10' \
            and inventoryField.units == 'uL' \
            and inventoryField.resource['id'] == resourceToAdd.id \
            and inventoryField.resource_item['id'] == resource_item.id \


    def test_signatures(self, entity):
        sig = entity.addSignature('test')
        sigs = entity.getSignatures()
        sig.revoke()
        assert sig.id == sigs[0].id \
            and sig.statement == 'test' \
            and sig.revoked_at is not None

    def test_signatureRequests(self, entity, workspaceToShare):
        sharelink = workspaceToShare.getSharelink()
        otherUser = fixtures.new_user(token=sharelink.token)
        request = entity.requestSignature(otherUser.id, message='test')
        requests = entity.getSignatureRequests()
        request.cancel()
        assert request.id == requests[0].id \
            and request.message == 'test' \
            and request.deleted_at is not None

    def test_experimentLinks(self, entity):
        otherExperiment = fixtures.experiment()
        link = entity.addExperimentLink(otherExperiment.id)
        links = entity.getExperimentLinks()
        backlinks = otherExperiment.getExperimentLinks(direction='backwards')
        source = link.getSourceExperiment()
        target = link.getTargetExperiment()
        assert link.guid == links[0].guid \
            and backlinks[0].guid == link.guid \
            and source.id == entity.id \
            and target.id == otherExperiment.id

    def test_jupyter_notebooks(self, entity):
        assert sharedTests.jupyterNotebooks(entity)

    def test_experiment_conditions(self, entity):
        assert sharedTests.experimentConditions(entity)

    def test_assign(self, entity):
        assert sharedTests.assign(entity)

    def test_edit_state_workflow(self, entity):
        stateWorkflow = entity.__user__.newEntityStateWorkflow(testString)
        entity.edit(entity_state_workflow_id=stateWorkflow.id)
        get_state_workflow = entity.getStateWorkflow()

        assert get_state_workflow.id == stateWorkflow.id

    def test_set_state(self, entity):
        stateWorkflow = entity.__user__.newEntityStateWorkflow(testString)
        state_entity=stateWorkflow.newEntityState(testString)
        entity=entity.edit(entity_state_id=state_entity.id)
        assert entity['entity_state']['id'] == state_entity.id
