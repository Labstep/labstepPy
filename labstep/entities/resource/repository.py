#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.resource.model import Resource
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getResource(user, resource_id):
    return entityRepository.getEntity(user, Resource, id=resource_id)


def getResources(
    user, count=100, search_query=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}
):
    params = {"search_query": search_query,
              "tag_id": tag_id, **extraParams}
    return entityRepository.getEntities(user, Resource, count, params)


def newResource(user, name, resource_category_id=UNSPECIFIED, extraParams={}):
    params = {
        "name": name,
        "template_id": resource_category_id,
        **extraParams}
    return entityRepository.newEntity(user, Resource, params)


def editResource(

    resource,
    name=UNSPECIFIED,
    deleted_at=UNSPECIFIED,
    resource_category_id=UNSPECIFIED,
    extraParams={},
):
    params = {
        "name": name,
        "template_id": resource_category_id,
        "deleted_at": deleted_at,
        **extraParams,
    }
    return entityRepository.editEntity(resource, params)
