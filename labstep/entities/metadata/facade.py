#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.metadata.repository import metadataRepository


def getMetadata(entity, count=1000, extraParams={}):
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
    return metadataRepository.getMetadata(entity, count, extraParams)


def addMetadataTo(
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
        "numeric", or "file". The "default" type is "Text".
    value (str)
        The value accompanying the fieldName entry.
    date (str)
        The date accompanying the fieldName entry. Must be
        in the format of "YYYY-MM-DD HH:MM".
    number (float)
        The quantity.
    unit (str)
        The unit accompanying the number entry.
    filepath (str)
        Local path to the file to upload for type 'file'

    Returns
    -------
    metadata
        An object representing the new Labstep Metadata.
    """
    return metadataRepository.addMetadataTo(
        entity, fieldName, fieldType, value, date, number, unit, filepath, extraParams
    )


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
    return metadataRepository.editMetadata(metadata, fieldName, value, extraParams)
