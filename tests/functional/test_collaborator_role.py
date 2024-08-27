#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from .shared import sharedTests

# __tracebackhide__ = True


class TestCollaboratorRole:
    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def entity(self):
        return fixtures.collaborator_role()


    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self, entity):
        entity = entity.edit(name='A New CollaboratorRole Name', description='A New CollaboratorRole Description')
        assert entity['name'] == 'A New CollaboratorRole Name' and entity['description'] == 'A New CollaboratorRole Description'

    def test_delete(self, entity):
        assert sharedTests.delete(entity)