#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import json
from labstep.entities.collection.model import Collection
from labstep.service.request import requestService
from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import configService
from labstep.generic.entity.repository import entityRepository

class CollectionRepository:
    def getCollections(
        self, user, count=1000, type=None, search_query=None, extraParams={}
    ):
        types = {
            "experiment": "experiment_workflow",
            "protocol": "protocol_collection",
            None: None,
        }
        params = {"search_query": search_query, "type": types[type], **extraParams}
        return entityRepository.getEntities(user, Collection, count, params)

    def getAttachedCollections(self, entity, count=100):
        key = entity.__entityName__.replace("-", "_") + "_id"
        filterParams = {key: entity.id, "group_id": entity.__user__.activeWorkspace}
        return entityRepository.getEntities(
            entity.__user__, Collection, count=count, filterParams=filterParams
        )

    def newCollection(self, user, name, type, extraParams={}):
        types = {"experiment": "experiment_workflow", "protocol": "protocol_collection"}
        params = {"name": name, "type": types[type], **extraParams}
        return entityRepository.newEntity(user, Collection, params)

    def addToCollection(self, entity, collection_id):
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

    def removeFromCollection(self, entity, collection_id):
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

    def editCollection(self, collection, name, extraParams={}):
        params = {"name": name, **extraParams}
        return entityRepository.editEntity(collection, params)


collectionRepository = CollectionRepository()
