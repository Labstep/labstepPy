#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures


class TestWorkspaceRole:

    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\WorkspaceRole')

    def test_edit_permission_role(self, user):
        org = user.getOrganization()
        workspace_role = org.newWorkspaceRole('New Role')
        workspace_role.edit(name='Updated name')
        assert workspace_role.name == 'Updated name'

    def test_workspace_role_type(self, user):
        org = user.getOrganization()
        workspace_role = org.newWorkspaceRole('New Role')
        workspace_role_type = 'owner'
        user = workspace_role.__user__.update()
        workspace = user.getWorkspaces()[0]
        members = workspace.getMembers()
        member = members[0]
        member.setWorkspaceRole(role_name=workspace_role_type)
        assert member.type == workspace_role_type

    def test_set_workspace_role(self, user):
        org = user.getOrganization()
        workspace_role = org.newWorkspaceRole('New Role')
        user = workspace_role.__user__.update()
        workspace = user.getWorkspaces()[0]
        members = workspace.getMembers()
        member = members[0]
        member.setWorkspaceRole(role_name=workspace_role.name)
        assert member.permission_role['guid'] == workspace_role.guid

    def test_grant_workspace_role_permission(self, user):
        org = user.getOrganization()
        workspace_role = org.newWorkspaceRole('New Role')
        from labstep.entities.experiment.model import Experiment
        workspace_role.__user__.update()
        workspace_role_permission = workspace_role.setPermission(
            Experiment, 'view')

        workspace_role_permissions = workspace_role.getPermissions()

        assert workspace_role_permission.guid == workspace_role_permissions[0].guid
        assert workspace_role_permissions[0]['action'] == 'view'
        assert workspace_role_permissions[0]['entity_name'] == 'experiment_workflow'
        assert workspace_role_permissions[0]['type'] == 'all'
