#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import json
from pathlib import Path
from labstep.service.config import API_ROOT
from labstep.service.helpers import (
    listToClass,
    url_join,
    getHeaders,
)
from labstep.service.request import requestService


class EntityRepository:
    def getLegacyEntity(self, user, entityClass, id):
        headers = getHeaders(user)
        url = url_join(API_ROOT, "/api/generic/",
                       entityClass.__entityName__, str(id))
        response = requestService.get(url, headers=headers)
        return entityClass(json.loads(response.content), user)

    def getEntity(self, user, entityClass, id, isDeleted="both"):
        if hasattr(entityClass, "__isLegacy__"):
            return self.getLegacyEntity(user, entityClass, id)
        else:
            params = {"is_deleted": isDeleted, "get_single": 1, "id": id}
            headers = getHeaders(user)
            url = url_join(API_ROOT, "/api/generic/",
                           entityClass.__entityName__)
            response = requestService.get(url, headers=headers, params=params)
            return entityClass(json.loads(response.content), user)

    def getEntities(self, user, entityClass, count, filterParams={}):
        countParameter = min(count, 50)
        searchParams = {"search": 1, "cursor": -1, "count": countParameter}

        params = {**searchParams, **filterParams}

        headers = getHeaders(user)
        url = url_join(API_ROOT, "/api/generic/", entityClass.__entityName__)
        response = requestService.get(url, params=params, headers=headers)
        resp = json.loads(response.content)
        items = resp["items"]
        expectedResults = min(resp["total"], count)
        while len(items) < expectedResults:
            params["cursor"] = resp["next_cursor"]
            response = requestService.get(url, headers=headers, params=params)
            resp = json.loads(response.content)
            items.extend(resp["items"])
        return listToClass(items, entityClass, user)

    def newEntity(self, user, entityClass, fields):
        headers = getHeaders(user)
        url = url_join(API_ROOT, "/api/generic/", entityClass.__entityName__)
        fields = dict(
            filter(lambda field: field[1] is not None, fields.items()))

        if "group_id" not in fields and getattr(
            entityClass, "__hasParentGroup__", False
        ):
            fields["group_id"] = user.activeWorkspace

        response = requestService.post(url, headers=headers, json=fields)
        return entityClass(json.loads(response.content), user)

    def newEntities(self, user, entityClass, items):
        headers = getHeaders(user)
        url = url_join(API_ROOT, "/api/generic/",
                       entityClass.__entityName__, "batch")
        response = requestService.post(
            url, headers=headers, json={"items": items})
        entities = json.loads(response.content)
        return list(map(lambda entity: entityClass(entity, user), entities))

    def editEntity(self, entity, fields):
        # Filter the 'fields' dictionary by removing {'fields': None}
        # to preserve the existing data in the 'fields', otherwise
        # the 'fields' will be overwritten to 'None'.
        newFields = dict(
            filter(lambda field: field[1] is not None, fields.items()))
        headers = getHeaders(entity.__user__)
        url = url_join(API_ROOT, "/api/generic/",
                       entity.__entityName__, str(entity.id))
        response = requestService.put(url, json=newFields, headers=headers)
        entity.__init__(json.loads(response.content), entity.__user__)
        return entity

    def exportEntity(self, entity, rootPath):
        from labstep.entities.file.model import File

        entityDir = Path(rootPath).joinpath(
            f'{entity.id}')
        entityDir.mkdir(parents=True, exist_ok=True)
        infoFile = entityDir.joinpath('entity.json')

        with open(infoFile, 'w') as out:
            json.dump(entity.__data__, out, indent=2)

        if hasattr(entity, 'file') and entity.file is not None:
            lsFile = entity.file
            fileDir = entityDir.joinpath(f'files/{str(lsFile["id"])}')
            fileDir.mkdir(parents=True, exist_ok=True)
            File(lsFile, entity.__user__).save(fileDir)

        if hasattr(entity, 'files') and entity.files is not None:
            for lsFile in entity.files:
                fileDir = entityDir.joinpath(f'files/{str(lsFile["id"])}')
                fileDir.mkdir(parents=True, exist_ok=True)
                File(lsFile, entity.__user__).save(fileDir)

        return entityDir


entityRepository = EntityRepository()
