#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures, proseMirrorState, testString
from .shared import sharedTests


class TestExperimentTemplate:
    @pytest.fixture
    def entity(self):
        return fixtures.experiment_template()

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

    @pytest.fixture
    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self):
        entity = fixtures.experiment_template()
        entity.edit('Pytest Edited', entry=proseMirrorState)
        entity.update()
        assert entity.name == 'Pytest Edited' and \
            entity.getEntry() == proseMirrorState

    def test_locking(self, entity):
        lockedEntity = entity.lock()
        assert lockedEntity.locked_at is not None
        unlockedEntity = entity.unlock()
        assert unlockedEntity.locked_at is None

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

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
        entity.addInventoryField('testInventoryField',
                                 amount=10,
                                 units='uL',
                                 resource_id=resourceToAdd.id,
                                )
        inventoryField = entity.getInventoryFields()[0]
        assert inventoryField.name == 'testInventoryField' \
            and inventoryField.amount == '10' \
            and inventoryField.units == 'uL' \
            and inventoryField.resource['id'] == resourceToAdd.id \

    def test_jupyter_notebooks(self, entity):
        assert sharedTests.jupyterNotebooks(entity)

    def test_experiment_conditions(self, entity):
        assert sharedTests.experimentConditions(entity)

    def test_assign(self, entity):
        assert sharedTests.assign(entity)

    def test_getEntityStateWorkflow(self, entity):
        entityStateWorkflow=entity.__user__.newEntityStateWorkflow(name='test')
        entity.edit(entity_state_workflow_id=entityStateWorkflow.id)
        entity.update()
        get_state_workflow = entity.getStateWorkflow()

        assert get_state_workflow.id == entityStateWorkflow.id

    def test_set_state(self, entity):
        stateWorkflow = entity.__user__.newEntityStateWorkflow(testString)
        state_entity=stateWorkflow.newEntityState(testString)
        entity=entity.edit(entity_state_id=state_entity.id)
        assert entity['entity_state']['id'] == state_entity.id
