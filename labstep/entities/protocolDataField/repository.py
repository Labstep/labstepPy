#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.file.repository import fileRepository
from labstep.generic.entity.repository import entityRepository
from labstep.service.helpers import handleDate, handleString
from labstep.entities.protocolDataField.model import ProtocolDataField
from labstep.entities.protocolVersion.model import ProtocolVersion


class ProtocolDataFieldRepository:
    def getDataFields(self, entity, count=1000, extraParams={}):

        if isinstance(entity, ProtocolVersion):
            params = {
                "metadata_thread_id": entity.metadata_thread["id"]}

            return entityRepository.getEntities(
                entity.__user__, ProtocolDataField, count=count, filterParams={
                    **params, **extraParams}
            )

    def addDataFieldTo(
        self,
        entity,
        fieldName,
        fieldType="default",
        value=None,
        date=None,
        number=None,
        unit=None,
        filepath=None,
        extraParams={},
    ):
        if filepath is not None:
            fileId = fileRepository.newFile(entity.__user__, filepath).id
        else:
            fileId = None

        params = {
            "metadata_thread_id": entity.metadata_thread["id"],
            "type": fieldType,
            "label": handleString(fieldName),
            "value": handleString(value),
            "date": handleDate(date),
            "number": number,
            "unit": unit,
            "file_id": fileId,
            **extraParams,
        }

        dataField = entityRepository.newEntity(
            entity.__user__, ProtocolDataField, params)

        dataField.protocol_id = entity.id

        return dataField

    def editDataField(self, dataField, fieldName=None, value=None, extraParams={}):
        params = {
            "label": handleString(fieldName),
            "value": handleString(value),
            **extraParams
        }
        return entityRepository.editEntity(dataField, params)


protocolDataFieldRepository = ProtocolDataFieldRepository()
