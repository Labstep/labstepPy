#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from .config import API_ROOT
from .entity import Entity, newEntity, editEntity
from .helpers import (listToClass, url_join, handleError,
                      handleDate, getHeaders)


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
    metadatas = entity.metadata_thread['metadatas']
    return listToClass(metadatas, Metadata, entity.__user__)


def addMetadataTo(entity, fieldType="default", fieldName=None,
                  value=None, date=None,
                  quantity_amount=None, quantity_unit=None,
                  extraParams={}):
    """
    Add Metadata to a Resource.

    Parameters
    ----------
    entity (obj)
        The Resource to add Metadata to.
    fieldType (str)
        The Metadata field type. Options are: "default", "date",
        "quantity", or "number". The "default" type is "Text".
    fieldName (str)
        The name of the field.
    value (str)
        The value accompanying the fieldName entry.
    date (str)
        The date accompanying the fieldName entry. Must be
        in the format of "YYYY-MM-DD HH:MM".
    quantity_amount (float)
        The quantity.
    quantity_unit (str)
        The unit accompanying the quantity_amount entry.

    Returns
    -------
    metadata
        An object representing the new Labstep Metadata.
    """
    filterParams = {'metadata_thread_id': entity.metadata_thread['id'],
                    'type': fieldType,
                    'label': fieldName,
                    'value': value,
                    'date': handleDate(date),
                    'quantity_amount': quantity_amount,
                    'quantity_unit': quantity_unit}
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
        return editMetadata(self, fieldName, value, extraParams)

    def delete(self):
        """
        Delete an existing Metadata field.

        Example
        -------
        ::

            metadata.delete()
        """
        return deleteMetadata(self)
