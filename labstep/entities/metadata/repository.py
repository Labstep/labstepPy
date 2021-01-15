#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.file.repository import fileRepository
from labstep.generic.entity.repository import entityRepository
from labstep.service.helpers import handleDate
from labstep.entities.metadata.model import Metadata, FIELDS, ALLOWED_FIELDS


class MetadataRepository:
    def getMetadata(self, entity, count=1000, extraParams={}):
        if hasattr(entity, 'metadata_thread') is False:
            entity.update()
        params = {
            "metadata_thread_id": entity.metadata_thread["id"], **extraParams}
        return entityRepository.getEntities(
            entity.__user__, Metadata, count=count, filterParams=params
        )

    def addMetadataTo(
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
        fields = {k: v for k, v in fields.items() if v}
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
            "label": fieldName,
            "value": value,
            "date": handleDate(date),
            "number": number,
            "unit": unit,
            "file_id": fileId,
            **extraParams,
        }

        return entityRepository.newEntity(entity.__user__, Metadata, params)

    def editMetadata(self, metadata, fieldName=None, value=None, extraParams={}):
        params = {"label": fieldName, "value": value, **extraParams}
        return entityRepository.editEntity(metadata, params)


metadataRepository = MetadataRepository()
