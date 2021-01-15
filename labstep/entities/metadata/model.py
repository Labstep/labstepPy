#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import handleDate, getTime


TYPE_DEFAULT = "default"
TYPE_NUMERIC = "numeric"
TYPE_DATE = "date"
TYPE_FILE = "file"
TYPE_MOLECULE = "molecule"
TYPE_SEQUENCE = "sequence"
TYPE_DATA_TABLE = "data_table"
TYPE_RICH_TEXT = "rich_text"
TYPE_OPTIONS = "options"

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
        "value",
    ],
    TYPE_NUMERIC: [
        "number",
        "unit",
    ],
    TYPE_DATE: [
        "date",
    ],
    TYPE_FILE: [
        "file_id",
    ],
    TYPE_MOLECULE: [
        "molecule",
    ],
    TYPE_SEQUENCE: [
        "sequence",
    ],
    TYPE_OPTIONS: [
        "options",
    ],
}


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

    __entityName__ = "metadata"

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
        :class:`~labstep.entities.metadata.model.Metadata`
            An object representing the edited Metadata.

        Example
        -------
        ::

            metadata.edit(value='2.50')
        """
        from labstep.entities.metadata.repository import metadataRepository

        return metadataRepository.editMetadata(
            self, fieldName, value, extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing Metadata field.

        Example
        -------
        ::

            metadata.delete()
        """
        from labstep.entities.metadata.repository import metadataRepository

        return metadataRepository.editMetadata(
            self, extraParams={"deleted_at": getTime()}
        )
