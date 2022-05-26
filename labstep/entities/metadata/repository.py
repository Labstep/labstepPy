#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import labstep.entities.file.repository as fileRepository
import labstep.generic.entity.repository as entityRepository
from labstep.generic.entityList.model import EntityList
from labstep.service.helpers import handleDate, handleString
from labstep.entities.metadata.model import Metadata, FIELDS, ALLOWED_FIELDS
from labstep.constants import UNSPECIFIED


def getMetadata(entity, count=1000, extraParams={}):
    if hasattr(entity, 'metadata_thread') is False:
        entity.update()
    if 'metadatas' in entity.metadata_thread:
        return EntityList(entity.metadata_thread['metadatas'], Metadata, entity.__user__)
    params = {
        "metadata_thread_id": entity.metadata_thread["id"], **extraParams}
    return entityRepository.getEntities(
        entity.__user__, Metadata, count=count, filterParams=params
    )


def addMetadataTo(

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

    if fieldType not in FIELDS:
        msg = "Not a supported metadata type '{}'".format(fieldType)
        raise ValueError(msg)

    allowedFieldsForType = set(ALLOWED_FIELDS[fieldType])
    fields = {
        "value": value,
        "date": date,
        "number": number,
        "unit": unit,
        "file_id": fileId,
    }
    fields = {k: v for k, v in fields.items() if v is not UNSPECIFIED}
    fields = set(fields.keys())
    violations = fields - allowedFieldsForType
    if violations:
        msg = "Unallowed fields [{}] for type {}".format(
            ",".join(violations), fieldType
        )
        raise ValueError(msg)

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

    return entityRepository.newEntity(entity.__user__, Metadata, params)


def editMetadata(metadata, fieldName=UNSPECIFIED, value=UNSPECIFIED, extraParams={}):
    params = {
        "label": handleString(fieldName),
        "value": handleString(value),
        **extraParams
    }
    return entityRepository.editEntity(metadata, params)
