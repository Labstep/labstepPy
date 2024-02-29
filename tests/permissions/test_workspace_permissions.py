#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from labstep.entities.workspace.model import Workspace
from labstep.entities.tag.model import Tag
from labstep.entities.collection.model import Collection
import pytest
from ..fixtures import fixtures
from ..shared import helperMethods

entityParams = {'name': 'Test', 'type': 'experiment_workflow'}


class TestWorkspacePermissions:

    @pytest.fixture
    def admin(self):
        return fixtures.new_user()

    @pytest.fixture
    def organization_with_users(self, admin):
        return fixtures.organization_with_users(admin)

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_create_tags(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testCreateAction(
            admin, users[0], org, Tag, entityParams)

    def test_edit_tag(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityActionNoAssign(admin, users[0], org, Tag,
                                               entityParams, 'edit', lambda entity: entity.edit(name='name'))

    def test_delete_tag(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityActionNoAssign(admin, users[0], org, Tag,
                                               entityParams, 'delete', lambda entity: entity.delete())

    def test_create_collection(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testCreateAction(
            admin, users[0], org, Collection, entityParams)

    def test_edit_collection(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityActionNoAssign(admin, users[0], org, Collection,
                                               entityParams, 'edit', lambda entity: entity.edit(name='name'))

    def test_delete_collection(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityActionNoAssign(admin, users[0], org, Collection,
                                               entityParams, 'delete', lambda entity: entity.delete())

    def test_comment(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_comment(entity):
            com = entity.addComment(body='test')
            com.edit(body='test_edit')
            com.addComment(body='reply')
            com.delete()

        helperMethods.testEntityActionNoAssign(
            admin, users[0], org, Workspace, {'name': 'Test'}, 'comment', action_comment)
