#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED
from labstep.entities.protocolTemplate.model import ProtocolTemplate
from labstep.entities.protocolVersion.model import ProtocolVersion
from labstep.service.helpers import handleDate

def getProtocolTemplate(user, protocol_template_id):
    return entityRepository.getEntity(user, ProtocolTemplate, id=protocol_template_id)


def getProtocolTemplates(
    user,
    count=UNSPECIFIED,
    search_query=UNSPECIFIED,
    created_at_from=UNSPECIFIED,
    created_at_to=UNSPECIFIED,
    extraParams={},
):
    params = {
        "search_query": search_query,
        "created_at_from": handleDate(created_at_from),
        "created_at_to": handleDate(created_at_to),
        "is_template": True,  # Filter to only get protocol templates
        **extraParams,
    }
    return entityRepository.getEntities(user, ProtocolTemplate, count, params)


def newProtocolTemplate(user, name, extraParams={}):
    params = {"name": name, **extraParams, "is_template": True}
    return entityRepository.newEntity(user, ProtocolTemplate, params)


def editProtocolTemplate(
    protocol_template, name=UNSPECIFIED, body=UNSPECIFIED, deleted_at=UNSPECIFIED, extraParams={}
):
    params = {"name": name, "deleted_at": deleted_at, **extraParams}

    if body is not UNSPECIFIED:
        entityRepository.editEntity(protocol_template.getCurrentVersion(), {"state": body})
        protocol_template.update()

    return entityRepository.editEntity(protocol_template, params)


def exportProtocolTemplate(protocol_template, root_path):

    protocol_template.update()

    expDir = entityRepository.exportEntity(protocol_template, root_path)

    # export latest version
    protocol_template.last_version.export(expDir)

    # export notes
    notesDir = expDir.joinpath('notes')
    notes = protocol_template.getComments(count=UNSPECIFIED)

    for note in notes:
        note.export(notesDir)
