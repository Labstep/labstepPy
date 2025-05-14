#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures
from .shared import sharedTests


class TestCollaboratorRoleRequirement:
    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def entity(self):
        return fixtures.collaborator_role_requirements()

    @pytest.fixture
    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self, entity):
        entity = entity.edit(number_required=2)
        assert entity['number_required'] == 2

    def test_edit_autoassign(self, entity):
        entity = entity.edit(auto_assign='creator')
        entity = entity.edit(auto_assign='contributor')
        assert True

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_setSignatureRequirement(self, entity):
        signature_requirement=entity.setSignatureRequirement()
        assert signature_requirement.id

    def test_getSignatureRequirement(self, entity):
        signature_requirement=entity.setSignatureRequirement()
        signature_requirements=entity.getSignatureRequirement()
        assert signature_requirement.id == signature_requirements.id

