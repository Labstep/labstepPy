#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from labstep.entities.resourceCategory.model import ResourceCategory
import pytest
from ..fixtures import fixtures
from ..shared import helperMethods

entityParams = {'name': 'Test'}


class TestResourceCategoryPermissions:

    @pytest.fixture
    def admin(self):
        return fixtures.new_user()

    @pytest.fixture
    def organization_with_users(self, admin):
        return fixtures.organization_with_users(admin)

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_create(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testCreateAction(
            admin, users[0], org, ResourceCategory, entityParams)

    def test_edit_name(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(admin, users[0], org, ResourceCategory,
                                       entityParams, 'edit', lambda entity: entity.edit(name='name'))

    def test_metadata(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_metadata(entity):
            template = entity.getResourceTemplate()
            metadata = template.addMetadata('test')
            metadata.edit(fieldName='test_edit')
            metadata.delete()

        helperMethods.testEntityAction(admin, users[0], org, ResourceCategory,
                                       entityParams, 'edit', lambda entity: action_metadata(entity))

    def test_assign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(admin, users[0], org, ResourceCategory,
                                       entityParams, 'assign', lambda entity: entity.assign(users[1].id))

    def test_unassign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_unassign(entity):
            entity.__user__ = admin
            colab = entity.assign(users[1].id)
            colab.__user__ = users[0]
            colab.unassign()

        helperMethods.testEntityAction(
            admin, users[0], org, ResourceCategory, entityParams, 'assign', action_unassign)
    """
    def test_comment(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_comment(entity):
            com = entity.addComment(body='test')
            com.edit(body='test_edit')
            com.addComment(body='reply')
            com.delete()

        helperMethods.testEntityAction(
            admin, users[0], org, ResourceCategory, entityParams, 'comment', action_comment)
    """

    def test_delete(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(
            admin, users[0], org, ResourceCategory, entityParams, 'delete', lambda entity: entity.delete())

    def test_share(self, admin, organization_with_users):
        [org, users] = organization_with_users

        workspace2 = admin.newWorkspace('Workspace 2')

        workspace2.addMember(users[0].id)

        def action_share(entity):
            entity.shareWith(workspace2.id)

        helperMethods.testEntityAction(
            admin, users[0], org, ResourceCategory, entityParams, 'share', action_share)
