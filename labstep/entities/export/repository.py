#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.export.model import Export
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getExport(user, export_id):
    return entityRepository.getEntity(user, Export, id=export_id)


def getExports(user, count=UNSPECIFIED, type=UNSPECIFIED, extraParams={}):
    params = {"type": type, **extraParams}
    return entityRepository.getEntities(user, Export, count, params)


def newExport(user, entity, type, extraParams={}):
    params = {
        "query_entity_name": entity.__entityName__,
        "query_parameters": {'id': entity.id},
        "type": type,
        **extraParams
    }
    return entityRepository.newEntity(user, Export, params)
