#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from .shared import sharedTests


class TestEnitytState:
    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def entity(self):
        return fixtures.entity_state()

    @pytest.fixture
    def collaborator_role(self):
        return fixtures.collaborator_role()

    @pytest.fixture
    def setup_method(self):
        fixtures.loadFixtures('Python\\\\EntityState')

    def test_edit(self, entity):
        entity = entity.edit(name='A new State name')
        assert entity['name'] == 'A new State name'

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_newRoleRequirement(self, entity, collaborator_role):
        role_requirement=entity.addRoleRequirement(collaborator_role_id=collaborator_role.id)
        assert role_requirement.id

    def test_getRoleRequirements(self, entity, collaborator_role):
        role_requirement=entity.addRoleRequirement(collaborator_role_id=collaborator_role.id)
        role_requirements=entity.getCollaboratorRoleRequirements()

        assert role_requirement.id == role_requirements.id