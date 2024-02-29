#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
import labstep
from .fixtures import fixtures
from .shared import sharedTests


class TestWorkspaceRole:

    @pytest.fixture
    def user(self):
        return fixtures.new_user()

    @pytest.fixture
    def workspace_role(self, user):
        return fixtures.workspace_role(user)

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit_permission_role(self, workspace_role):
        workspace_role.edit(name='Change name')
        assert workspace_role.name == 'Change name'

    def test_workspace_role_type(self, workspace_role):
        workspace_role_type = 'owner'
        user = workspace_role.__user__.update()
        workspace = user.getWorkspaces()[0]
        member = workspace.getMembers().get('Team Labstep')
        member.setWorkspaceRole(role_name=workspace_role_type)
        assert member.type == workspace_role_type

    def test_set_workspace_role(self, workspace_role):
        user = workspace_role.__user__.update()
        workspace = user.getWorkspaces()[0]
        members = workspace.getMembers()
        member = members[0]
        member.setWorkspaceRole(role_name=workspace_role.name)
        assert member.permission_role['guid'] == workspace_role.guid

    def test_grant_workspace_role_permission(self, workspace_role):
        from labstep.entities.experiment.model import Experiment
        user = workspace_role.__user__.update()
        workspace_role_permission = workspace_role.setPermission(
            Experiment, 'create')

        workspace_role_permissions = workspace_role.getPermissions()

        assert workspace_role_permission.guid == workspace_role_permissions[0].guid
        assert workspace_role_permissions[0]['action'] == 'experiment_workflow:create'
        assert workspace_role_permissions[0]['entity_name'] == 'group'
        assert workspace_role_permissions[0]['type'] == 'all'
