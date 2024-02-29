#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from labstep.entities.protocol.model import Protocol
import pytest
from ..fixtures import fixtures, proseMirrorState
from ..shared import helperMethods

entityParams = {'name': 'Test'}


class TestProtocolPermissions:

    @pytest.fixture
    def admin(self):
        return fixtures.new_user()

    @pytest.fixture
    def organization_with_users(self, admin):
        return fixtures.organization_with_users(admin)

    @pytest.fixture
    def protocol(self, admin):
        return fixtures.protocol(admin)

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_create(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testCreateAction(
            admin, users[0], org, Protocol, entityParams)

    def test_edit_name(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(admin, users[0], org, Protocol,
                                       entityParams, 'edit', lambda entity: entity.edit(name='name'))

    def test_edit_entry(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(admin, users[0], org, Protocol,
                                       entityParams, 'edit', lambda entity: entity.edit(body=proseMirrorState))

    def test_tables(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            table = entity.addTable('test')
            table.edit(name='edited')
            table.delete()

        helperMethods.testEntityAction(admin, users[0], org, Protocol,
                                       entityParams, 'edit', lambda entity: action(entity))

    def test_files(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            file = entity.addFile(__file__)
            file.delete()

        helperMethods.testEntityAction(admin, users[0], org, Protocol,
                                       entityParams, 'edit', lambda entity: action(entity))

    def test_data(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            data = entity.addDataField('test')
            data.edit(fieldName='edited')
            data.delete()

        helperMethods.testEntityAction(admin, users[0], org, Protocol,
                                       entityParams, 'edit', lambda entity: action(entity))

    def test_inventory(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            inventoryField = entity.addInventoryField('test')
            inventoryField.edit(amount='10')
            inventoryField.delete()

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'edit', action)
    """
    def test_jupyter_notebooks(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            jupyter_notebook = entity.addJupyterNotebook(name="test")
            jupyter_notebook.delete()

        helperMethods.testEntityAction(admin, users[0], org, Protocol,
                                       entityParams, 'edit', lambda entity: action(entity))
    """

    def test_assign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(admin, users[0], org, Protocol,
                                       entityParams, 'assign', lambda entity: entity.assign(users[1].id))

    def test_unassign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_unassign(entity):
            entity.__user__ = admin
            colab = entity.assign(users[1].id)
            colab.__user__ = users[0]
            colab.unassign()

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'assign', action_unassign)

    def test_newVersion(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'edit', lambda entity: entity.newVersion())

    def test_steps(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_steps(entity):
            steps = entity.addSteps(3)
            steps[0].delete()

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'edit', action_steps)

    def test_timers(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_timers(entity):
            timer = entity.addTimer(name='test', minutes=20, seconds=30)
            timer.edit(minutes=17)
            timer.delete()

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'edit', action_timers)

    def test_conditions(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_conditions(entity):
            conditions = entity.addConditions(4)
            conditions[0].delete()

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'edit', action_conditions)

    def test_comment(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_comment(entity):
            com = entity.addComment(body='test')
            com.edit(body='test_edit')
            com.addComment(body='reply')
            com.delete()

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'comment', action_comment)

    def test_delete(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'delete', lambda entity: entity.delete())

    def test_share(self, admin, organization_with_users):
        [org, users] = organization_with_users

        workspace2 = admin.newWorkspace('Workspace 2')

        workspace2.addMember(users[0].id)

        def action_share(entity):
            entity.shareWith(workspace2.id)

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'share', action_share)

    def test_tagging(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_tag(entity):
            workspace = admin.getWorkspace(entity.owner['id'])
            workspace.newTag(f'{entity.id}')
            entity.addTag(f'{entity.id}')

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'tag:add_remove', action_tag)

    def test_collections(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_collection(entity):
            workspace = admin.getWorkspace(entity.owner['id'])
            collection = workspace.newCollection(
                f'{entity.id}', type='protocol')
            entity.addToCollection(collection.id)
            entity.removeFromCollection(collection.id)

        helperMethods.testEntityAction(
            admin, users[0], org, Protocol, entityParams, 'folder:add_remove', action_collection)
