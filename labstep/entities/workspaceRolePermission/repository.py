#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.workspaceRolePermission.model import WorkspaceRolePermission
from labstep.generic.entity.repository import getEntities, newEntity, editEntity, deleteEntity
from labstep.constants import UNSPECIFIED
from labstep.service.request import requestService
from labstep.service.helpers import url_join, getHeaders, handleString
from labstep.service.config import configService
import json


def revokeWorkspaceRolePermission(workspaceRolePermission: WorkspaceRolePermission):

    deleteEntity(workspaceRolePermission)

    return None


def setWorkspaceRolePermission(workspaceRole, entityClass, action, permission_setting='all'):
    entityName = entityClass.__entityName__.replace("-", "_")

    if hasattr(entityClass, '__isTemplate__'):
        entityName = f'{entityName}_template'

    if action == 'create':
        params = {'entity_name': 'group',
                  'action': f'{entityName}:create'}
    elif action == 'assign':
        params = {'entity_name': entityName,
                  'action': 'entity_user:*'}
    elif action == 'share':
        params = {'entity_name': entityName,
                  'action': 'permission:*'}
    elif action == 'comment':
        params = {'entity_name': entityName,
                  'action': 'comment:*'}
    elif action == 'create_bookings':
        params = {'entity_name': entityName,
                  'action': 'device_booking:*'}
    elif action == 'send_data':
        params = {'entity_name': entityName,
                  'action': 'device_data:*'}
    elif action == 'sign':
        params = {'entity_name': entityName,
                  'action': 'signature:*'}
    elif action in ['lock', 'unlock', 'edit', 'delete', 'tag:add_remove', 'folder:add_remove', 'resource_item:create']:
        params = {'entity_name': entityName, 'action': action}
    else:
        raise Exception(
            f'{action} is not a valid action for which permission can be granted')

    if permission_setting == 'if_assigned':
        permission_setting = 'custom'

    params = {**params,
              'permission_role_id': workspaceRole.guid,
              'type': permission_setting
              }

    headers = getHeaders(workspaceRole.__user__)
    url = url_join(
        configService.getHost(),
        "api/generic/",
        WorkspaceRolePermission.__entityName__,
    )
    response = requestService.post(url, json=params, headers=headers)
    json_response = json.loads(response.content)

    return WorkspaceRolePermission(json_response, workspaceRole.__user__)
