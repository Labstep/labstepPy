#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Onoufrios Malikkides <onoufrios@labstep.com>

from labstep.entities.chemical.model import Chemical
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getChemical(user, guid):
    return entityRepository.getEntity(user, Chemical, id=guid)


def getChemicals(user, molecule_guid, count=100, extraParams={}):
    params = {
        "molecule_guid": molecule_guid,
        "search": None,
        **extraParams,
    }
    return entityRepository.getEntities(user, Chemical, count, params)

def newChemical(user, protocol_value_id, molecule_guid, extraParams={}):
    params = { "protocol_value_id": protocol_value_id, "molecule_guid": molecule_guid, **extraParams}
    return entityRepository.newEntity(user, Chemical, params)


def editChemical(chemical, deleted_at=UNSPECIFIED, extraParams={}):
    params = {"deleted_at": deleted_at, **extraParams}
    return entityRepository.editEntity(chemical, params)
