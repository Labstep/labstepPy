#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

testUser = labstep.login('apitest@labstep.com', 'apitestpass')

# Set variables
testName = labstep.helpers.getTime()

# Make new entity
workspace = testUser.newWorkspace(testName)


class TestSharing:
    def test_share_experiment(self):
        entity = testUser.newExperiment(testName)
        entity.shareWith(workspace.id, 'view')
        permission = entity.getPermissions()[0]
        permission.set('edit')
        new_permission = entity.getPermissions()[0]
        new_permission.revoke()
        final_permissions = entity.getPermissions()
        assert permission.permission == 'view' \
            and new_permission.permission == 'edit' \
            and len(final_permissions) == 1, \
            'FAILED TO SHARE EXPERIMENT'

    def test_share_protocol(self):
        entity = testUser.newProtocol(testName)
        entity.shareWith(workspace.id, 'view')
        permission = entity.getPermissions()[0]
        permission.set('edit')
        new_permission = entity.getPermissions()[0]
        new_permission.revoke()
        final_permissions = entity.getPermissions()
        assert permission.permission == 'view' \
            and new_permission.permission == 'edit' \
            and len(final_permissions) == 1, \
            'FAILED TO SHARE PROTOCOL'

    def test_share_resource(self):
        entity = testUser.newResource(testName)
        entity.shareWith(workspace.id, 'view')
        permission = entity.getPermissions()[0]
        permission.set('edit')
        new_permission = entity.getPermissions()[0]
        new_permission.revoke()
        final_permissions = entity.getPermissions()
        assert permission.permission == 'view' \
            and new_permission.permission == 'edit' \
            and len(final_permissions) == 1, \
            'FAILED TO SHARE RESOURCE'

    def test_share_resourceCategory(self):
        entity = testUser.newResourceCategory(testName)
        entity.shareWith(workspace.id, 'view')
        permission = entity.getPermissions()[0]
        permission.set('edit')
        new_permission = entity.getPermissions()[0]
        new_permission.revoke()
        final_permissions = entity.getPermissions()
        assert permission.permission == 'view' \
            and new_permission.permission == 'edit' \
            and len(final_permissions) == 1, \
            'FAILED TO SHARE RESOURCE CATEGORY'

    def test_share_orderRequest(self):
        entity = testUser.newResource(testName).newOrderRequest()
        entity.shareWith(workspace.id, 'view')
        permission = entity.getPermissions()[0]
        permission.set('edit')
        new_permission = entity.getPermissions()[0]
        new_permission.revoke()
        final_permissions = entity.getPermissions()
        assert permission.permission == 'view' \
            and new_permission.permission == 'edit' \
            and len(final_permissions) == 1, \
            'FAILED TO SHARE ORDER REQUEST'
