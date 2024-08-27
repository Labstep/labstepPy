#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures


class TestOrganization:
    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Organization')

    def test_edit(self, user):
        organization = user.getOrganization()
        result = organization.edit(name='Edited Org Name')
        assert result.name == 'Edited Org Name'

    def test_getWorkspaces(self, user):
        organization = user.getOrganization()
        workspaces = organization.getWorkspaces()
        assert len(workspaces) > 0

    def test_getUsers(self, user):
        organization = user.getOrganization()
        users = organization.getUsers()
        assert len(users) > 0

    def test_workspace_roles(self, user):
        organization = user.getOrganization()
        newRole = organization.newWorkspaceRole('Intern')
        roles = organization.getWorkspaceRoles()
        assert roles[0].guid == newRole.guid
