#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from labstep.entities.orderRequest.model import OrderRequest
import pytest
from ..fixtures import fixtures
from ..shared import helperMethods


class TestOrderRequestPermissions:

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

        resource = admin.newResource('Test')
        entityParams = {'resource_id': resource.id, 'quantity': 1}

        helperMethods.testCreateAction(
            admin, users[0], org, OrderRequest, entityParams)

    def test_edit_status(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')
        entityParams = {'resource_id': resource.id, 'quantity': 1}

        helperMethods.testEntityAction(admin, users[0], org, OrderRequest,
                                       entityParams, 'edit', lambda entity: entity.edit(status='ordered'))

    def test_metadata(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')
        entityParams = {'resource_id': resource.id, 'quantity': 1}

        def action_metadata(entity):
            metadata = entity.addMetadata('test')
            metadata.edit(fieldName='test_edit')
            metadata.delete()

        helperMethods.testEntityAction(admin, users[0], org, OrderRequest,
                                       entityParams, 'edit', lambda entity: action_metadata(entity))

    def test_assign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')
        entityParams = {'resource_id': resource.id, 'quantity': 1}

        helperMethods.testEntityAction(admin, users[0], org, OrderRequest,
                                       entityParams, 'assign', lambda entity: entity.assign(users[1].id))

    def test_unassign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')
        entityParams = {'resource_id': resource.id, 'quantity': 1}

        def action_unassign(entity):
            entity.__user__ = admin
            colab = entity.assign(users[1].id)
            colab.__user__ = users[0]
            colab.unassign()

        helperMethods.testEntityAction(
            admin, users[0], org, OrderRequest, entityParams, 'assign', action_unassign)

    def test_comment(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')
        entityParams = {'resource_id': resource.id, 'quantity': 1}

        def action_comment(entity):
            com = entity.addComment(body='test')
            com.edit(body='test_edit')
            com.addComment(body='reply')
            com.delete()

        helperMethods.testEntityAction(
            admin, users[0], org, OrderRequest, entityParams, 'comment', action_comment)

    def test_delete(self, admin, organization_with_users):
        [org, users] = organization_with_users

        resource = admin.newResource('Test')
        entityParams = {'resource_id': resource.id, 'quantity': 1}

        helperMethods.testEntityAction(
            admin, users[0], org, OrderRequest, entityParams, 'delete', lambda entity: entity.delete())

    def test_share(self, admin, organization_with_users):
        [org, users] = organization_with_users

        workspace2 = admin.newWorkspace('Workspace 2')

        workspace2.addMember(users[0].id)

        resource = admin.newResource('Test')
        entityParams = {'resource_id': resource.id, 'quantity': 1}

        def action_share(entity):
            entity.shareWith(workspace2.id)

        helperMethods.testEntityAction(
            admin, users[0], org, OrderRequest, entityParams, 'share', action_share)
