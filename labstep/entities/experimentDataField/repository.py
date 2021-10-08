#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.file.repository import fileRepository
from labstep.generic.entity.repository import entityRepository
from labstep.service.helpers import handleDate, handleString
from labstep.entities.experimentDataField.model import ExperimentDataField
from labstep.entities.experimentProtocol.model import ExperimentProtocol
from labstep.entities.resource.model import Resource
from labstep.entities.resourceItem.model import ResourceItem


class ExperimentDataFieldRepository:
    def getDataFields(self, entity, count=1000, extraParams={}):

        params = {}

        if isinstance(entity, ExperimentProtocol):
            params = {
                "metadata_thread_id": entity.metadata_thread["id"]}

        elif isinstance(entity, Resource):
            params = {
                "experiment_value_resource_id": entity.id,
                "has_value": True
            }
        elif isinstance(entity, ResourceItem):
            params = {
                "experiment_value_resource_item_id": entity.id,
                "has_value": True
            }

        return entityRepository.getEntities(
            entity.__user__, ExperimentDataField, count=count, filterParams={
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

        return entityRepository.newEntity(entity.__user__, ExperimentDataField, params)

    def editDataField(self, dataField, fieldName=None, value=None, extraParams={}):
        params = {
            "label": handleString(fieldName),
            "value": handleString(value),
            **extraParams
        }
        return entityRepository.editEntity(dataField, params)


experimentDataFieldRepository = ExperimentDataFieldRepository()
