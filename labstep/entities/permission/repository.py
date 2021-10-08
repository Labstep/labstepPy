#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import json
from labstep.service.helpers import listToClass, url_join, getHeaders
from labstep.service.config import configService
from labstep.service.request import requestService
from labstep.entities.permission.model import Permission


class PermissionRepository:
    def newPermission(self, entity, workspace_id, permission):
        entityName = entity.__entityName__

        headers = getHeaders(entity.__user__)
        url = url_join(configService.getHost(), "api/generic/", "acl")

        params = {
            "id": entity.id,
            "entity_class": entityName.replace("-", "_"),
            "action": "grant",
            "group_id": workspace_id,
            "permission": permission,
        }
        requestService.post(url, headers=headers, json=params)
        return entity

    def editPermission(self, entity, workspace_id, permission):
        entityName = entity.__entityName__

        headers = getHeaders(entity.__user__)
        url = url_join(configService.getHost(), "api/generic/", "acl")

        params = {
            "id": entity.id,
            "entity_class": entityName.replace("-", "_"),
            "action": "set",
            "group_id": workspace_id,
            "group_owner_id": workspace_id,
            "permission": permission,
        }
        requestService.post(url, headers=headers, json=params)
        return entity

    def revokePermission(self, entity, workspace_id):
        entityName = entity.__entityName__

        headers = getHeaders(entity.__user__)
        url = url_join(configService.getHost(), "api/generic/", "acl")

        params = {
            "id": entity.id,
            "entity_class": entityName.replace("-", "_"),
            "action": "revoke",
            "group_id": workspace_id,
        }
        requestService.post(url, headers=headers, json=params)
        return entity

    def getPermissions(self, entity):
        entityName = entity.__entityName__
        headers = getHeaders(entity.__user__)
        url = url_join(
            configService.getHost(),
            "api/generic/",
            "acl",
            entityName.replace("-", "_"),
            str(entity.id),
        )
        response = requestService.get(url, headers=headers)
        resp = json.loads(response.content)
        return listToClass(resp["group_permissions"], Permission, entity)

    def transferOwnership(self, entity, workspace_id):
        entityName = entity.__entityName__
        headers = getHeaders(entity.__user__)
        url = url_join(
            configService.getHost(), "api/generic/", entityName, str(entity.id), "transfer-ownership"
        )
        params = {"group_id": workspace_id}
        requestService.post(url, headers=headers, json=params)


permissionRepository = PermissionRepository()
