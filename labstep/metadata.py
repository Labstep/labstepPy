#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .entity import getEntities, newEntity, editEntity
from .helpers import url_join, handleError, update


def addMetadataTo(entity, fieldName, value, fieldType="default"):
    """
    Create a new Metadata.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Metadata.
        Must have property 'api_key'. See 'login'.
    fieldName (str)
        Name of the new Metadata.
    value (obj)
        Value of the metadata.
    fieldType (str)
        Metadata field type. Defaults to Text


    Returns
    -------
    metadata
        An object representing the new Labstep Metadata.
    """
    fields = {'label': fieldName, 'metadata_thread_id': entity.metadata_thread_id, 'type': fieldType, 'value': value}
    return newEntity(entity.__user__, Metadata, fields)


def editMetadata(metadata, value):
    """
    Edit the name of an existing Metadata.

    Parameters
    ----------
    metadata (obj)
        The Metadata to edit.
    value (str)
        The new value of the Metadata.

    Returns
    -------
    metadata
        An object representing the edited Metadata.
    """
    fields = {'value': value}
    return editEntity(metadata, fields)


def deleteMetadata(metadata):
    """
    Delete an existing metadata.

    Parameters
    ----------
    metadata (obj)
        The metadata to delete.

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
    def edit(self, value):
        """
        Edit the name of an existing Metadata.

        Parameters
        ----------
        value (str)
            The new value of the Metadata.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An object representing the edited Metadata.

        Example
        -------
        .. code-block::

            # Get metadata for a resource
            # Edit
            metdata.edit(value='A New Metadata Value')
        """
        return editMetadata(self, value)

    def delete(self):
        """
        Delete an existing Metadata field.

        Example
        -------
        .. code-block::

            # Get metadata for a resource
            # Delete
            metdata.delete(name='A New Metadata Name')
        """
        return deleteMetadata(self)
