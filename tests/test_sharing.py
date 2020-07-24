#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import (workspace, experiment, protocol,
                      resource, resourceCategory, orderRequest)
# Make new entity


class TestSharing:
    def test_share_experiment(self):
        entity = experiment()
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
        entity = protocol()
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
        entity = resource()
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
        entity = resourceCategory()
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
        entity = orderRequest()
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
