#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import json
import labstep.entities.file.repository as fileRepository
import labstep.generic.entity.repository as entityRepository
from labstep.generic.entityList.model import EntityList
from labstep.service.helpers import formatDate, handleDate, handleString
from labstep.entities.experimentDataField.model import ExperimentDataField
from labstep.entities.experimentProtocol.model import ExperimentProtocol
from labstep.entities.resource.model import Resource
from labstep.entities.resourceItem.model import ResourceItem
from labstep.entities.file.model import File
from labstep.entities.deviceData.model import DeviceData
from labstep.constants import UNSPECIFIED


def getDataFields(entity, count=UNSPECIFIED, extraParams={}):

    params = {}

    if hasattr(entity, 'metadata_thread') is False:
        entity.update()

    if isinstance(entity, ExperimentProtocol):
        params = {
            "metadata_thread_id": entity.metadata_thread["id"]}

    elif isinstance(entity, Resource):
        params = {
            "multiplexing_input_resource_id": entity.id,
            "has_value": True
        }
        dataWhenInput = entityRepository.getEntities(
            entity.__user__, ExperimentDataField, count=count, filterParams={
                **params, **extraParams})

        params = {
            "multiplexing_output_resource_id": entity.id,
            "has_value": True
        }
        dataWhenOutput = entityRepository.getEntities(
            entity.__user__, ExperimentDataField, count=count, filterParams={
                **params, **extraParams})

        return dataWhenInput + dataWhenOutput

    elif isinstance(entity, ResourceItem):
        params = {
            "multiplexing_input_resource_item_id": entity.id,
            "has_value": True
        }
        dataWhenInput = entityRepository.getEntities(
            entity.__user__, ExperimentDataField, count=count, filterParams={
                **params, **extraParams})

        params = {
            "multiplexing_output_resource_item_id": entity.id,
            "has_value": True
        }
        dataWhenOutput = entityRepository.getEntities(
            entity.__user__, ExperimentDataField, count=count, filterParams={
                **params, **extraParams})

        return dataWhenInput + dataWhenOutput

    return entityRepository.getEntities(
        entity.__user__, ExperimentDataField, count=count, filterParams={
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

    if hasattr(entity, 'metadata_thread') is False:
        entity.update()

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


def editDataField(dataField, fieldName=UNSPECIFIED, value=UNSPECIFIED, is_variable=UNSPECIFIED, extraParams={}):
    params = {
        "label": handleString(fieldName),
        "value": handleString(value),
        "is_variable": is_variable,
        **extraParams
    }
    return entityRepository.editEntity(dataField, params)


def getDataFieldValue(dataField):

    if dataField.device_data is not None:
        dataField = DeviceData(dataField.device_data, dataField.__user__)

    if dataField.type == 'default':
        return dataField.value

    if dataField.type == 'numeric':
        return dataField.number

    if dataField.type == 'date':
        if dataField.date is None:
            return None
        return formatDate(dataField.date, time=False)

    if dataField.type == 'datetime':
        return formatDate(dataField.date)

    if dataField.type == 'options':
        if dataField.options is None:
            return None

        keys = [k for k, v in dataField.options['values'].items() if v]

        if keys == []:
            return None

        if dataField.options['is_allow_multiple']:
            return keys

        return keys[0]

    if dataField.type == 'file':

        if len(dataField.files) == 1:
            return File(dataField.files[0], dataField.__user__)
        else:
            return EntityList(dataField.files, File, dataField.__user__)

    if dataField.type == 'sequence':
        return json.loads(dataField.sequence['data'])

    return None


def setDataFieldValue(dataField, value, condition_id=None):
    if condition_id is not None:
        if dataField.is_variable is False:
            raise Exception(
                'Cannot set value for conditions on a constant data field')

        conditionDataField = entityRepository.getEntities(
            dataField.__user__, ExperimentDataField, count=UNSPECIFIED, filterParams={
                'protocol_condition_id': condition_id
        }).get(dataField.guid, searchKey='variable_template_guid')

        if conditionDataField is None:
            params = {
                "metadata_thread_id": dataField.metadata_thread["id"],
                "source_id": dataField.id,
                "variable_template_id": dataField.id,
                "protocol_condition_id": condition_id,
            }
            newField = entityRepository.newEntity(dataField.__user__, ExperimentDataField, params)
            setDataFieldValue(newField, value)
        else:
            return setDataFieldValue(conditionDataField,value)


    if condition_id is None and dataField.is_variable is True:
        raise Exception(
            'Please specify a condition ID for variable data fields')


    if dataField.type == 'default':
        return dataField.edit(extraParams={'value': str(value)})

    if dataField.type == 'numeric':
        return dataField.edit(extraParams={'number': float(value)})

    if dataField.type == 'date' or dataField.type == 'datetime':
        return dataField.edit(extraParams={'date': handleDate(value)})

    if dataField.type == 'options':

        if isinstance(value, list) is False:
            value = [str(value)]

        options = dataField.options

        if options is None:
            options = {
                'is_allow_multiple': False,
                'is_allow_add': True,
                'values': {}
            }

        if options['values'] is None:
            options['values'] = {}

        options['values'] = {key: False for key in options['values'].keys()}

        if options['is_allow_multiple'] is False and len(value) > 1:
            raise Exception(
                'Specifying multiple values for this field is forbidden. ')

        for activeKey in value:
            options['values'][activeKey] = True

        return dataField.edit(extraParams={'options': options})

    if dataField.type == 'file':
        if isinstance(value, File) is False:
            raise Exception(
                'Please specify a Labstep File object as the value')

        return dataField.edit(extraParams={'file_id': value.id})

    return None
