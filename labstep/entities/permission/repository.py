#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import json
from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import configService
from labstep.service.request import requestService
from labstep.entities.permission.model import Permission
from labstep.generic.entity.repository import getEntities, newEntity, editEntity, deleteEntity
from labstep.constants import UNSPECIFIED


def newPermission(entity, workspace_guid, permission):
    entityName = entity.__entityName__.replace("-", "_")

    params = {
        f'{entityName}_guid': entity.guid,
        "group_guid": workspace_guid,
        "type": permission,
    }
    return newEntity(entity.__user__, Permission, params)


def editPermission(permission, type):
    return editEntity(permission, {'type': type})


def revokePermission(permission):
    return deleteEntity(permission)


def getPermissions(entity, count=UNSPECIFIED):
    entityName = entity.__entityName__.replace("-", "_")

    params = {
        f'{entityName}_id': entity.id
    }

    return getEntities(entity.__user__, Permission, count, params)


def transferOwnership(entity, workspace_id):
    entityName = entity.__entityName__
    headers = getHeaders(entity.__user__)
    url = url_join(
        configService.getHost(), "api/generic/", entityName, str(entity.id), "transfer-ownership"
    )
    params = {"group_id": workspace_id}
    requestService.post(url, headers=headers, json=params)
