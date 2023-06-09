#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import json
from labstep.entities.collection.model import Collection
from labstep.service.request import requestService
from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import configService
from labstep.generic.entity.repository import getEntities, editEntity, newEntities, newEntity
from labstep.constants import UNSPECIFIED


def getCollections(
    user, count=UNSPECIFIED, type=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}
):
    types = {
        "experiment": "experiment_workflow",
        "protocol": "protocol_collection",
        None: None,
        UNSPECIFIED: UNSPECIFIED,
    }
    params = {"search_query": search_query,
              "type": types[type], 'group_id': user.activeWorkspace, **extraParams}
    return getEntities(user, Collection, count, params)


def getAttachedCollections(entity, count=UNSPECIFIED):
    key = entity.__entityName__.replace("-", "_") + "_id"
    filterParams = {key: entity.id,
                    "group_id": entity.__user__.activeWorkspace}
    return getEntities(
        entity.__user__, Collection, count=count, filterParams=filterParams
    )


def newCollection(user, name, type, extraParams={}):
    types = {"experiment": "experiment_workflow",
             "protocol": "protocol_collection"}
    params = {"name": name, "type": types[type], "group_id": user.activeWorkspace, **extraParams}
    return newEntity(user, Collection, params)


def newCollections(user, names, type, extraParams={}):
    types = {"experiment": "experiment_workflow",
             "protocol": "protocol_collection"}
    params = [{"name": name, "type": types[type], "group_id": user.activeWorkspace, **extraParams}
              for name in names]
    return newEntities(user, Collection, params)


def addToCollection(entity, collection_id):
    entityName = entity.__entityName__

    headers = getHeaders(entity.__user__)
    url = url_join(
        configService.getHost(),
        "api/generic/",
        entityName,
        str(entity.id),
        Collection.__entityName__,
        str(collection_id),
    )
    response = requestService.put(url, headers=headers)
    return json.loads(response.content)


def removeFromCollection(entity, collection_id):
    entityName = entity.__entityName__

    headers = getHeaders(entity.__user__)
    url = url_join(
        configService.getHost(),
        "api/generic/",
        entityName,
        str(entity.id),
        Collection.__entityName__,
        str(collection_id),
    )
    response = requestService.delete(url, headers=headers)
    return json.loads(response.content)


def editCollection(collection, name, extraParams={}):
    params = {"name": name, **extraParams}
    return editEntity(collection, params)
