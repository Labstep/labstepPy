#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.resource.model import Resource
from labstep.generic.entity.repository import entityRepository

class ResourceRepository:
    def getResource(self, user, resource_id):
        return entityRepository.getEntity(user, Resource, id=resource_id)

    def getResources(
        self, user, count=100, search_query=None, tag_id=None, extraParams={}
    ):
        params = {"search_query": search_query, "tag_id": tag_id, **extraParams}
        return entityRepository.getEntities(user, Resource, count, params)

    def newResource(self, user, name, extraParams={}):
        params = {"name": name, **extraParams}
        return entityRepository.newEntity(user, Resource, params)

    def editResource(
        self,
        resource,
        name=None,
        deleted_at=None,
        resource_category_id=None,
        extraParams={},
    ):
        params = {
            "name": name,
            "template_id": resource_category_id,
            "deleted_at": deleted_at,
            **extraParams,
        }
        return entityRepository.editEntity(resource, params)


resourceRepository = ResourceRepository()
