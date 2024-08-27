#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from .shared import sharedTests


class TestEnitytStateWorkflow:
    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def entity(self):
        return fixtures.entity_state_workflow()

    @pytest.fixture
    def setup_method(self):
        fixtures.loadFixtures('Python\\\\EntityStateWorkflow')

    def test_edit(self, entity):
        entity = entity.edit(name='A new Workflow name')
        assert entity['name'] == 'A new Workflow name'

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_newEntityState(self, entity):
        entity_state=entity.newEntityState(name='Test')
        assert entity_state.id

    def test_getEntityStates(self, entity):
        entity_state=entity.newEntityState(name='Test')
        entity_states=entity.getEntityStates()
        assert entity_state.id == entity_states[0].id

    def test_getEntityState(self, entity):
        entity_state=entity.newEntityState(name='Test')
        entity_state_from_get=entity.getEntityState(entity_state.id)
        assert entity_state.id == entity_state_from_get.id