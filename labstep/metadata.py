#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from .config import API_ROOT
from .entity import newEntity, editEntity
from .helpers import (listToClass, url_join, handleError, handleDate,
                      update, showAttributes)


def getMetadatas(entity):
    """
    Retrieve the Metadatas of a Labstep Resource.

    Parameters
    ----------
    entity (obj)
        The entity Resource to retrieve the Metadatas from.

    Returns
    -------
    metadatas
        An object representing the Metadatas of the Resource.
    """
    metadatas = entity.metadata_thread['metadatas']
    return listToClass(metadatas, Metadata, entity.__user__)


def addMetadataTo(entity, fieldType="default", fieldName=None,
                  value=None, date=None,
                  quantity_amount=None, quantity_unit=None):
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
    fields = {'metadata_thread_id': entity.metadata_thread['id'],
              'type': fieldType,
              'label': fieldName,
              'value': value,
              'date': handleDate(date),
              'quantity_amount': quantity_amount,
              'quantity_unit': quantity_unit}
    return newEntity(entity.__user__, Metadata, fields)


def editMetadata(metadata, fieldName=None, value=None):
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
    fields = {'label': fieldName,
              'value': value}
    return editEntity(metadata, fields)


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
    headers = {'apikey': metadata.__user__.api_key}
    url = url_join(API_ROOT, "/api/generic/metadata/", str(metadata.id))
    r = requests.delete(url, headers=headers)
    handleError(r)
    return None


class Metadata:
    __entityName__ = 'metadata'

    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    # functions()
    def attributes(self):
        """
        Show all attributes of a Metadata.

        Example
        -------
        .. code-block::

            # Add metadata to a resource
            my_resource = user.getResource(17000)
            metadata = my_resource.addMetadata(fieldName="Refractive Index",
                                               value="1.73")

            # Show attributes
            metadata.attributes()

        The output should look something like this:

        .. program-output:: python ../labstep/attributes/metadata_attributes.py

        To inspect specific attributes of a metadata,
        for example, the metadata 'label', 'value', etc.:

        .. code-block::

            print(metadata.label)
            print(metadata.value)
        """
        return showAttributes(self)

    def edit(self, fieldName=None, value=None):
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
        .. code-block::

            metadata.edit(value='2.50')
        """
        return editMetadata(self, fieldName, value)

    def delete(self):
        """
        Delete an existing Metadata field.

        Example
        -------
        .. code-block::

            metadata.delete()
        """
        return deleteMetadata(self)
