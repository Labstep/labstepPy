#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import json
from pathlib import Path
from pathvalidate import sanitize_filepath
from labstep.entities.export.model import Export
from labstep.generic.entityList.model import EntityList
from labstep.service.config import configService
from labstep.service.helpers import (
    filterUnspecified,
    url_join,
    getHeaders,
)
from labstep.service.request import requestService
from labstep.config.export import entityNameInFolderName
from labstep.constants import UNSPECIFIED


def getEntityProperty(entity, attribute, entityClass=None):
    if attribute not in entity.__data__:
        entity.update()

    if entityClass is not None and entity.__data__[attribute] is not None:
        return entityClass(entity.__data__[attribute], entity.__user__)

    return entity.__data__[attribute]


def getLegacyEntity(user, entityClass, id):
    headers = getHeaders(user=user)
    url = url_join(configService.getHost(), "/api/generic/",
                   entityClass.__entityName__, str(id))
    response = requestService.get(url, headers=headers)
    return entityClass(json.loads(response.content), user)


def getEntity(user, entityClass, id, isDeleted="both", useGuid=False, extraParams={}):
    if getattr(entityClass, "__isLegacy__", None):
        return getLegacyEntity(user, entityClass, id)

    identifier = 'guid' if getattr(
        entityClass, "__hasGuid__", None) or useGuid else 'id'

    params = {"is_deleted": isDeleted,
              "get_single": 1, identifier: id, **extraParams}

    headers = getHeaders(user=user)
    url = url_join(configService.getHost(), "/api/generic/",
                   entityClass.__entityName__)
    response = requestService.get(url, headers=headers, params=params)
    return entityClass(json.loads(response.content), user)


def filterEntities(user, entityClass, filter, count=UNSPECIFIED, pageSize=50):
    page = 1
    headers = getHeaders(user=user)
    url = url_join(configService.getHost(), "/api/generic/",
                   entityClass.__entityName__, "filter")
    print(f'Fetching page {page}')
    response = requestService.post(
        url, headers=headers, json={"filter": filter, "page": page, "skip_total": 1, "count": pageSize, "group_id": user.activeWorkspace})

    content = json.loads(response.content)
    entities = content['items']
    entityCount = len(content['items'])

    while (entityCount == pageSize):
        if count is not UNSPECIFIED and entityCount >= count:
            break
        page = page + 1
        print(f'Fetching page {page}')
        response = requestService.post(
            url, headers=headers, json={"filter": filter, "page": page, "count": pageSize, "skip_total": 1, "group_id": user.activeWorkspace})
        content = json.loads(response.content)
        entities.extend(content['items'])
        entityCount = len(content['items'])

    return EntityList(entities, entityClass, user)


def getEntities(user, entityClass, count, filterParams={}):
    countParameter = min(
        count, 50) if count is not UNSPECIFIED else UNSPECIFIED

    if getattr(entityClass, "__unSearchable__", None):
        searchParams = {"cursor": -1, "count": countParameter}
    else:
        searchParams = {"search": 1, "cursor": -1, "count": countParameter}

    params = {**searchParams, **filterParams}

    headers = getHeaders(user=user)
    url = url_join(configService.getHost(), "/api/generic/",
                   entityClass.__entityName__)
    response = requestService.get(url, params=params, headers=headers)
    resp = json.loads(response.content)
    items = resp["items"]

    while resp["next_cursor"] != '-1':
        if count is not UNSPECIFIED:
            remainingItems = count - len(items)
            params["count"] = min(remainingItems, 50)
            if remainingItems <= 0:
                break

        params["cursor"] = resp["next_cursor"]
        response = requestService.get(url, headers=headers, params=params)
        resp = json.loads(response.content)
        items.extend(resp["items"])

    return EntityList(items, entityClass, user)


def newEntity(user, entityClass, fields):
    headers = getHeaders(user=user)
    url = url_join(configService.getHost(), "/api/generic/",
                   entityClass.__entityName__)

    if "group_id" not in fields and getattr(
        entityClass, "__hasParentGroup__", False
    ):
        fields["group_id"] = user.activeWorkspace

    response = requestService.post(url, headers=headers, json=fields)
    return entityClass(json.loads(response.content), user)


def linkEntities(user, entity1, entity2):
    headers = getHeaders(user)
    url = url_join(
        configService.getHost(),
        "api/generic/",
        entity1.__entityName__,
        str(entity1.id),
        entity2.__entityName__,
        str(entity2.id),
    )
    response = requestService.put(url, headers=headers)
    return json.loads(response.content)


def newEntities(user, entityClass, items):
    headers = getHeaders(user=user)
    url = url_join(configService.getHost(), "/api/generic/",
                   entityClass.__entityName__, "batch")
    response = requestService.post(
        url, headers=headers, json={"items": items, "group_id": user.activeWorkspace})
    entities = json.loads(response.content)
    return EntityList(entities, entityClass, user)


def editEntity(entity, fields):
    identifier = entity.guid if getattr(
        entity, "__hasGuid__", None) and hasattr(entity, 'guid') else entity.id

    headers = getHeaders(entity.__user__)
    url = url_join(configService.getHost(), "/api/generic/",
                   entity.__entityName__, str(identifier))
    response = requestService.put(url, json=fields, headers=headers)
    entity.__init__(json.loads(response.content), entity.__user__)
    return entity


def deleteEntity(entity):
    identifier = entity.guid if getattr(
        entity, "__hasGuid__", None) and hasattr(entity, 'guid') else entity.id

    headers = getHeaders(entity.__user__)
    url = url_join(configService.getHost(), "/api/generic/",
                   entity.__entityName__, str(identifier))
    return requestService.delete(url, headers=headers)


def exportEntity(entity, rootPath, folderName=UNSPECIFIED):

    from labstep.entities.file.model import File

    if folderName is UNSPECIFIED:
        if entityNameInFolderName and hasattr(
                entity, 'name') and entity.name is not None:
            santitisedName = sanitize_filepath(
                entity.name.replace('/', ' ').replace('\\', ' '))[:50].strip()
            folderName = f"{entity.id} - {santitisedName}"
            if len(folderName) > 255:
                folderName = str(entity.id)
        else:
            folderName = str(entity.id)

    entityDir = Path(rootPath).joinpath(sanitize_filepath(folderName))
    entityDir.mkdir(parents=True, exist_ok=True)
    infoFile = entityDir.joinpath(f'{folderName}.json')

    with open(infoFile, 'w') as out:
        json.dump(entity.__data__, out, indent=2)

    if hasattr(entity, 'file') and entity.file is not None:
        lsFile = File(entity.file, entity.__user__)
        fileDir = entityDir.joinpath('files')
        lsFile.export(fileDir)

    if hasattr(entity, 'files') and entity.files is not None:
        for file in entity.files:
            lsFile = File(file, entity.__user__)
            fileDir = entityDir.joinpath('files')
            lsFile.export(fileDir)

    return entityDir
