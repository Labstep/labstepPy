#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.entityImport.model import EntityImport
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getEntityImport(user, guid):
    return entityRepository.getEntity(user, EntityImport, id=guid)


def newEntityImport(user, targetEntity, data, templateGuid=UNSPECIFIED, name=UNSPECIFIED):
    params = {
        "group_id": user.activeWorkspace,
        "target_entity_name": targetEntity.__entityName__,
        'data': data,
        "name": name
    }
    if templateGuid:
        params[targetEntity.__entityName__ + '_template_guid'] = templateGuid
    return entityRepository.newEntity(user, EntityImport, params)


def editEntityImport(
    entityImport,
    name=UNSPECIFIED
):
    params = {
        "name": name,
    }

    return entityRepository.editEntity(entityImport, params)
