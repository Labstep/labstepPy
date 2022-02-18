#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.service.helpers import (
    handleDate,
)
from labstep.entities.protocol.model import Protocol
from labstep.entities.protocolVersion.model import ProtocolVersion
import labstep.generic.entity.repository as entityRepository
from labstep.service.htmlExport import htmlExportService
from labstep.constants import UNSPECIFIED


def getProtocol(user, protocol_id):
    return entityRepository.getEntity(user, Protocol, id=protocol_id)


def getProtocols(

    user,
    count=100,
    search_query=UNSPECIFIED,
    created_at_from=UNSPECIFIED,
    created_at_to=UNSPECIFIED,
    tag_id=UNSPECIFIED,
    collection_id=UNSPECIFIED,
    extraParams={},
):
    params = {
        "search_query": search_query,
        "created_at_from": handleDate(created_at_from),
        "created_at_to": handleDate(created_at_to),
        "tag_id": tag_id,
        "folder_id": collection_id,
        **extraParams,
    }
    return entityRepository.getEntities(user, Protocol, count, params)


def newProtocol(user, name, extraParams={}):
    params = {"name": name, **extraParams}
    return entityRepository.newEntity(user, Protocol, params)


def editProtocol(
    protocol, name=UNSPECIFIED, body=UNSPECIFIED, deleted_at=UNSPECIFIED, extraParams={}
):
    params = {"name": name, "deleted_at": deleted_at, **extraParams}

    if body is not UNSPECIFIED:
        entityRepository.editEntity(
            ProtocolVersion(protocol.last_version, protocol.__user__),
            {"state": body},
        )
        protocol.update()

    return entityRepository.editEntity(protocol, params)


def exportProtocol(protocol, root_path):

    protocol.update()

    expDir = entityRepository.exportEntity(protocol, root_path)

    # export notes
    notesDir = expDir.joinpath('notes')
    notes = protocol.getComments(count=1000)

    for note in notes:
        note.export(notesDir)

    # save inventory fields
    inventoryFieldsDir = expDir.joinpath('inventory')
    inventoryFields = protocol.getInventoryFields()

    for inventoryField in inventoryFields:
        inventoryField.export(inventoryFieldsDir)

    # save data
    dataDir = expDir.joinpath('data')
    data = protocol.getDataFields()

    for dat in data:
        dat.export(dataDir)

    # get html
    html = htmlExportService.getHTML(protocol)
    html_with_paths = htmlExportService.insertFilepaths(expDir, html)

    with open(expDir.joinpath('entity.html'), 'w') as out:
        out.write(html_with_paths)
