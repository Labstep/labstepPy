#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.sequence.model import Sequence
import labstep.generic.entity.repository as entityRepository
from labstep.entities.metadata.model import Metadata
from labstep.constants import PLACEHOLDER_SVG, UNSPECIFIED


def getSequence(user, id, extraParams={}):
    return entityRepository.getEntity(user, Sequence, id, extraParams)


def editSequence(sequence, data=UNSPECIFIED, deleted_at=UNSPECIFIED, extraParams={}):
    params = {
        "data": data,
        "deleted_at": deleted_at,
        **extraParams,
    }
    return entityRepository.editEntity(sequence, params)


def newSequence(user, metadata_id, data='{\\"circular\\":true,\\"sequence\\":null}'):

    metadata = Metadata({'id': metadata_id}, user)
    edited = metadata.edit(
        extraParams={'sequence': {'name': 'Untitled Sequence', 'data': data}})
    return Sequence(edited.sequence, user)
