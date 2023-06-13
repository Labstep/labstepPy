#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep.entities.file.repository as fileRepository
import labstep.generic.entity.repository as entityRepository
from labstep.service.helpers import handleDate, handleString
from labstep.entities.protocolDataField.model import ProtocolDataField
from labstep.entities.protocolVersion.model import ProtocolVersion
from labstep.constants import UNSPECIFIED


def getDataFields(entity, count=UNSPECIFIED, extraParams={}):
    if hasattr(entity, 'metadata_thread') is False:
        entity.update()
        
    if isinstance(entity, ProtocolVersion):
        params = {
            "metadata_thread_id": entity.metadata_thread["id"]}

        return entityRepository.getEntities(
            entity.__user__, ProtocolDataField, count=count, filterParams={
                **params, **extraParams}
        )


def addDataFieldTo(

    entity,
    fieldName,
    fieldType="default",
    value=UNSPECIFIED,
    date=UNSPECIFIED,
    number=UNSPECIFIED,
    unit=UNSPECIFIED,
    filepath=UNSPECIFIED,
    extraParams={},
):
    if filepath is not UNSPECIFIED:
        fileId = fileRepository.newFile(entity.__user__, filepath).id
    else:
        fileId = UNSPECIFIED

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


def editDataField(dataField, fieldName=UNSPECIFIED, value=UNSPECIFIED, extraParams={}):
    params = {
        "label": handleString(fieldName),
        "value": handleString(value),
        **extraParams
    }
    return entityRepository.editEntity(dataField, params)
