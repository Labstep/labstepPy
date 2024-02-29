#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures

# __tracebackhide__ = True


class TestCollaborator:
    @pytest.fixture
    def user(self):
        return fixtures.new_user()

    @pytest.fixture
    def collaborator(self, user):
        return fixtures.collaborator(user)

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_unassign(self, collaborator):
        collab = collaborator.unassign()
        assert collab['is_assigned'] == False
