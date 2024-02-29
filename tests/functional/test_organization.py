#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures


class TestOrganization:
    @pytest.fixture
    def user(self):
        return fixtures.new_user()

    @pytest.fixture
    def organization(self, user):
        [org, users] = fixtures.organization_with_users(user)
        return org

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self, organization):
        result = organization.edit(name='Edited Org Name')
        assert result.name == 'Edited Org Name'

    def test_getWorkspaces(self, organization):
        workspaces = organization.getWorkspaces()
        assert len(workspaces) > 0

    def test_getUsers(self, organization):
        users = organization.getUsers()
        assert len(users) > 0

    def test_workspace_roles(self, organization):

        newRole = organization.newWorkspaceRole('Intern')
        roles = organization.getWorkspaceRoles()
        assert roles[0].guid == newRole.guid
