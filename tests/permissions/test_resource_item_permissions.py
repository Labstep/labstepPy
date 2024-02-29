#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from labstep.entities.resourceItem.model import ResourceItem
import pytest
from ..fixtures import fixtures
from ..shared import helperMethods


class TestResourceItemPermissions:

    @pytest.fixture
    def admin(self):
        return fixtures.new_user()

    @pytest.fixture
    def organization_with_users(self, admin):
        return fixtures.organization_with_users(admin)

    def setup_method(self):
        fixtures.loadFixtures('Python')

    """ 
    def test_create(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')
        entityParams = {'name': 'Test', 'resource_id': resource.id}

        helperMethods.testCreateAction(
            admin, users[0], org, ResourceItem, entityParams)
    """

    def test_edit_name(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')

        entityParams = {'name': 'Test', 'resource_id': resource.id}

        helperMethods.testEntityAction(admin, users[0], org, ResourceItem,
                                       entityParams, 'edit', lambda entity: entity.edit(name='name'))

    def test_metadata(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')

        entityParams = {'name': 'Test', 'resource_id': resource.id}

        def action_metadata(entity):
            metadata = entity.addMetadata('test')
            metadata.edit(fieldName='test_edit')
            metadata.delete()

        helperMethods.testEntityAction(admin, users[0], org, ResourceItem,
                                       entityParams, 'edit', lambda entity: action_metadata(entity))
    """
    def test_assign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')

        entityParams = {'name': 'Test', 'resource_id': resource.id}

        helperMethods.testEntityAction(admin, users[0], org, ResourceItem,
                                       entityParams, 'assign', lambda entity: entity.assign(users[1].id))
    

    def test_unassign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')

        entityParams = {'name': 'Test', 'resource_id': resource.id}

        def action_unassign(entity):
            entity.__user__ = admin
            colab = entity.assign(users[1].id)
            colab.__user__ = users[0]
            colab.unassign()

        helperMethods.testEntityAction(
            admin, users[0], org, ResourceItem, entityParams, 'assign', action_unassign)

    def test_comment(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')

        entityParams = {'name': 'Test', 'resource_id': resource.id}

        def action_comment(entity):
            com = entity.addComment(body='test')
            com.edit(body='test_edit')
            com.addComment(body='reply')
            com.delete()

        helperMethods.testEntityAction(
            admin, users[0], org, ResourceItem, entityParams, 'comment', action_comment)
    """

    def test_delete(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')

        entityParams = {'name': 'Test', 'resource_id': resource.id}

        helperMethods.testEntityAction(
            admin, users[0], org, ResourceItem, entityParams, 'delete', lambda entity: entity.delete())
