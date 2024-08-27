#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from .shared import sharedTests


class TestSignatureRequirement:
    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def entity(self):
        return fixtures.signature_requirement()

    @pytest.fixture
    def setup_method(self):
        fixtures.loadFixtures('Python\\\\SignatureRequirement')

    def test_edit(self, entity):
        entity_state_workflow=entity.__user__.newEntityStateWorkflow('test workflow')
        entity_state=entity_state_workflow.newEntityState('test state')
        entity = entity.edit(statement='Reviewer please say yes', days_to_sign=3, reject_entity_state_id=entity_state.id)

        assert entity['statement'] == 'Reviewer please say yes' and \
               entity['days_to_sign'] == 3 and \
               entity['reject_entity_state']['id'] == entity_state.id

    def test_disable(self, entity):
        assert entity.disableSignatureRequirement()


