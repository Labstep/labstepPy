#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from labstep.entities.experiment.model import Experiment
import pytest
from ..fixtures import fixtures, proseMirrorState
from ..shared import helperMethods

entityParams = {'name': 'Test'}


class TestExperimentPermissions:

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
            admin, users[0], org, Experiment, entityParams)

    def test_edit_name(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'edit', lambda entity: entity.edit(name='name'))

    def test_edit_date(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'edit', lambda entity: entity.edit(started_at='2024-02-01'))

    def test_edit_entry(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'edit', lambda entity: entity.edit(entry=proseMirrorState))

    def test_tables(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            table = entity.addTable('test')
            table.edit(name='edited')
            table.delete()

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'edit', lambda entity: action(entity))

    def test_files(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            file = entity.addFile(__file__)
            file.delete()

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'edit', lambda entity: action(entity))

    def test_protocols(self, admin, organization_with_users, protocol):
        [org, users] = organization_with_users

        def action(entity):
            p = entity.addProtocol(protocol)
            p.edit(name='edited')
            p.delete()

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'edit', lambda entity: action(entity))

    def test_data(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            data = entity.addDataField('test')
            data.edit(fieldName='edited')
            data.delete()

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'edit', lambda entity: action(entity))

    def test_inventory(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            inventoryField = entity.addInventoryField('test')
            inventoryField.edit(amount='10')
            inventoryField.delete()

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'edit', action)

    def test_signatures(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            sig = entity.addSignature('test')
            sig.revoke()

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'sign', lambda entity: action(entity))

    """
    def test_jupyter_notebooks(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action(entity):
            jupyter_notebook = entity.addJupyterNotebook(name="test")
            jupyter_notebook.delete()

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'edit', lambda entity: action(entity))
    """

    def test_assign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(admin, users[0], org, Experiment,
                                       entityParams, 'assign', lambda entity: entity.assign(users[1].id))

    def test_unassign(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_unassign(entity):
            entity.__user__ = admin
            colab = entity.assign(users[1].id)
            colab.__user__ = users[0]
            colab.unassign()

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'assign', action_unassign)

    def test_lock(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'lock', lambda entity: entity.lock())

    def test_unlock(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_unlock(entity):
            entity.__user__ = admin
            entity.lock()
            entity.__user__ = users[0]
            entity.unlock()

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'unlock', action_unlock)

    def test_comment(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_comment(entity):
            com = entity.addComment(body='test')
            com.edit(body='test_edit')
            com.addComment(body='reply')
            com.delete()

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'comment', action_comment)

    def test_delete(self, admin, organization_with_users):
        [org, users] = organization_with_users

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'delete', lambda entity: entity.delete())

    def test_share(self, admin, organization_with_users):
        [org, users] = organization_with_users

        workspace2 = admin.newWorkspace('Workspace 2')

        workspace2.addMember(users[0].id)

        def action_share(entity):
            entity.shareWith(workspace2.id)

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'share', action_share)

    def test_tagging(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_tag(entity):
            workspace = admin.getWorkspace(entity.owner['id'])
            workspace.newTag(f'{entity.id}')
            entity.addTag(f'{entity.id}')

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'tag:add_remove', action_tag)

    def test_collections(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_collection(entity):
            workspace = admin.getWorkspace(entity.owner['id'])
            collection = workspace.newCollection(f'{entity.id}')
            entity.addToCollection(collection.id)
            entity.removeFromCollection(collection.id)

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'folder:add_remove', action_collection)

    def test_conditions(self, admin, organization_with_users):
        [org, users] = organization_with_users

        def action_conditions(entity):
            conditions = entity.addConditions(4)
            conditions[0].delete()

        helperMethods.testEntityAction(
            admin, users[0], org, Experiment, entityParams, 'edit', action_conditions)
