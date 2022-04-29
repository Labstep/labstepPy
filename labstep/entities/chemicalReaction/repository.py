#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.chemicalReaction.model import ChemicalReaction
import labstep.generic.entity.repository as entityRepository
from labstep.constants import PLACEHOLDER_SVG, UNSPECIFIED


def getChemicalReaction(user, guid, extraParams={}):
    return entityRepository.getEntity(user, ChemicalReaction, guid, extraParams)


def editChemicalReaction(chemicalReaction, deleted_at=UNSPECIFIED, name=UNSPECIFIED, data=UNSPECIFIED, inchis=UNSPECIFIED, extraParams={}):
    params = {
        "name": name,
        "data": data,
        "inchis": inchis,
        "deleted_at": deleted_at,
        **extraParams,
    }
    return entityRepository.editEntity(chemicalReaction, params)


def newChemicalReaction(user, experimentId, extraParams={}):
    params = {
        "name": 'Untitled',
        "experiment_id": experimentId,
        "data": "",
        "pubchem":  None,
        **extraParams,
    }

    if 'svg' not in params:
        params['svg'] = PLACEHOLDER_SVG

    return entityRepository.newEntity(user, ChemicalReaction, params)
