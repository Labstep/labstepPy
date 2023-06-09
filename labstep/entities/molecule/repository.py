#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.molecule.model import Molecule
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getMolecule(user, guid, extraParams={}):
    return entityRepository.getEntity(user, Molecule, guid, extraParams)


def editMolecule(molecule, deleted_at=UNSPECIFIED, name=UNSPECIFIED, data=UNSPECIFIED, inchis=UNSPECIFIED, extraParams={}):
    params = {
        "name": name,
        "data": data,
        "inchis": inchis,
        "deleted_at": deleted_at,
        **extraParams,
    }
    return entityRepository.editEntity(molecule, params)


def newMolecule(user, experimentId, extraParams={}):
    params = {
        "name": 'Untitled',
        "experiment_id": experimentId,
        "data": "",
        "pubchem":  None,
        "svg": "",
        **extraParams,
    }

    return entityRepository.newEntity(user, Molecule, params)
