#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from .config import API_ROOT
from .entity import Entity, newEntity, editEntity
from .helpers import (listToClass, url_join, handleError,
                      handleDate, getHeaders)

TYPE_DEFAULT = 'default'
TYPE_NUMERIC = 'numeric'
TYPE_DATE = 'date'
TYPE_FILE = 'file'
TYPE_MOLECULE = 'molecule'
TYPE_SEQUENCE = 'sequence'
TYPE_DATA_TABLE = 'data_table'
TYPE_RICH_TEXT = 'rich_text'
TYPE_OPTIONS = 'options'

FIELDS = [
    TYPE_DEFAULT,
    TYPE_NUMERIC,
    TYPE_DATE,
    TYPE_FILE,
    TYPE_MOLECULE,
    TYPE_SEQUENCE,
    TYPE_DATA_TABLE,
    TYPE_RICH_TEXT,
    TYPE_OPTIONS,
]

ALLOWED_FIELDS = {
    TYPE_DEFAULT: [
        'value',
    ],
    TYPE_NUMERIC: [
        'number',
        'unit',
    ],
    TYPE_DATE: [
        'date',
    ],
    TYPE_FILE: [
        'file',
    ],
    TYPE_MOLECULE: [
        'molecule',
    ],
    TYPE_SEQUENCE: [
        'sequence',
    ],
    TYPE_OPTIONS: [
        'options',
    ],
}

def getMetadata(entity):
    """
    Retrieve the Metadata of a Labstep Entity.

    Parameters
    ----------
    entity (obj)
        The Entity to retrieve the Metadata from.

    Returns
    -------
    metadatas
        An array of Metadata objects for the Entity.
    """
    if 'metadatas' not in entity.metadata_thread:
        entity.update()
    metadatas = entity.metadata_thread['metadatas']
    return listToClass(metadatas, Metadata, entity.__user__)


def addMetadataTo(entity, fieldName, fieldType="default",
                  value=None, date=None,
                  number=None, unit=None,
                  extraParams={}):
    """
    Add Metadata to a Resource.

    Parameters
    ----------
    entity (obj)
        The Resource to add Metadata to.
    fieldName (str)
        The name of the field.
    fieldType (str)
        The Metadata field type. Options are: "default", "date",
        "quantity", or "number". The "default" type is "Text".
    value (str)
        The value accompanying the fieldName entry.
    date (str)
        The date accompanying the fieldName entry. Must be
        in the format of "YYYY-MM-DD HH:MM".
    number (float)
        The quantity.
    unit (str)
        The unit accompanying the number entry.

    Returns
    -------
    metadata
        An object representing the new Labstep Metadata.
    """
    if not fieldType in FIELDS: 
        msg = "Not a supported metadata type '{}'".format(fieldType)
        raise ValueError(msg)

    allowedFieldsForType = set(ALLOWED_FIELDS[fieldType])
    fields = {
        'value': value,
        'date': date,
        'number': number,
        'unit': unit,
    }
    fields = {k: v for k, v in fields.items() if v}
    fields = set(fields.keys())
    violations = fields - allowedFieldsForType
    if violations:
        msg = 'Unallowed fields [{}] for type {}'.format(",".join(violations), fieldtype)
        raise ValueError(msg)

    filterParams = {'metadata_thread_id': entity.metadata_thread['id'],
                    'type': fieldType,
                    'label': fieldName,
                    'value': value,
                    'date': handleDate(date),
                    'number': number,
                    'unit': unit}
    params = {**filterParams, **extraParams}
    return newEntity(entity.__user__, Metadata, params)


def editMetadata(metadata, fieldName=None, value=None, extraParams={}):
    """
    Edit the value of an existing Metadata.

    Parameters
    ----------
    metadata (obj)
        The Metadata to edit.
    fieldName (str)
        The new name of the field.
    value (str)
        The new value of the Metadata.

    Returns
    -------
    metadata
        An object representing the edited Metadata.
    """
    filterParams = {'label': fieldName,
                    'value': value}
    params = {**filterParams, **extraParams}
    return editEntity(metadata, params)


def deleteMetadata(metadata):
    """
    Delete an existing Metadata.

    Parameters
    ----------
    metadata (obj)
        The Metadata to delete.

    Returns
    -------
    None
    """
    headers = getHeaders(metadata.__user__)
    url = url_join(API_ROOT, "/api/generic/metadata/", str(metadata.id))
    r = requests.delete(url, headers=headers)
    handleError(r)
    return None


class Metadata(Entity):
    """
    Represents a single Metadata field attached to a Labstep Entity.

    To see the attributes of the metsdata field run
    ::
        print(my_metadata_field)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_metadata_field.value)
        print(my_metadata_field.id)
    """
    __entityName__ = 'metadata'

    def edit(self, fieldName=None, value=None, extraParams={}):
        """
        Edit the value of an existing Metadata.

        Parameters
        ----------
        fieldName (str)
            The new name of the field.
        value (str)
            The new value of the Metadata.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An object representing the edited Metadata.

        Example
        -------
        ::

            metadata.edit(value='2.50')
        """
        return editMetadata(self, fieldName, value, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Metadata field.

        Example
        -------
        ::

            metadata.delete()
        """
        return deleteMetadata(self)
