#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.service.helpers import (
    createdAtFrom,
    createdAtTo,
)
from labstep.entities.protocol.model import Protocol
from labstep.entities.protocolVersion.model import ProtocolVersion
from labstep.generic.entity.repository import entityRepository
from labstep.service.htmlExport import htmlExportService


class ProtocolRepository:
    def getProtocol(self, user, protocol_id):
        return entityRepository.getEntity(user, Protocol, id=protocol_id)

    def getProtocols(
        self,
        user,
        count=100,
        search_query=None,
        created_at_from=None,
        created_at_to=None,
        tag_id=None,
        collection_id=None,
        extraParams={},
    ):
        params = {
            "search_query": search_query,
            "created_at_from": createdAtFrom(created_at_from),
            "created_at_to": createdAtTo(created_at_to),
            "tag_id": tag_id,
            "folder_id": collection_id,
            **extraParams,
        }
        return entityRepository.getEntities(user, Protocol, count, params)

    def newProtocol(self, user, name, extraParams={}):
        params = {"name": name, **extraParams}
        return entityRepository.newEntity(user, Protocol, params)

    def editProtocol(
        self, protocol, name=None, body=None, deleted_at=None, extraParams={}
    ):
        params = {"name": name, "deleted_at": deleted_at, **extraParams}

        if body is not None:
            entityRepository.editEntity(
                ProtocolVersion(protocol.last_version, protocol.__user__),
                {"state": body},
            )
            protocol.update()

        return entityRepository.editEntity(protocol, params)

    def exportProtocol(self, protocol, root_path):

        protocol.update()

        expDir = entityRepository.exportEntity(protocol, root_path)

        # export notes
        notesDir = expDir.joinpath('notes')
        notes = protocol.getComments(count=1000)

        for note in notes:
            note.export(notesDir)

        # save materials
        materialsDir = expDir.joinpath('materials')
        materials = protocol.getMaterials()

        for material in materials:
            material.export(materialsDir)

        # save data
        dataDir = expDir.joinpath('data')
        data = protocol.getDataElements()

        for dat in data:
            dat.export(dataDir)

        # get html
        html = htmlExportService.getHTML(protocol)
        html_with_paths = htmlExportService.insertFilepaths(expDir, html)

        with open(expDir.joinpath('entity.html'), 'w') as out:
            out.write(html_with_paths)


protocolRepository = ProtocolRepository()
