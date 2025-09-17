#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class ResourceTemplate(Entity):
    __entityName__ = "resource"

    def addMetadata(
        self,
        fieldName,
        fieldType="default",
        value=UNSPECIFIED,
        date=UNSPECIFIED,
        number=UNSPECIFIED,
        unit=UNSPECIFIED,
        filepath=UNSPECIFIED,
        extraParams={},
    ):
        """
        Add Metadata to the Resource Template.

        Parameters
        ----------
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
            The numeric value.
        unit (str)
            The unit accompanying the number entry.
        filepath (str)
            Local path to the file to upload for type 'file'

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        ::

            resource_category = user.getResourceCategory(17000)
            metadata = my_resource_category.addMetadata("Refractive Index",
                                                        value="1.73")
        """
        import labstep.entities.metadata.repository as metadataRepository

        return metadataRepository.addMetadataTo(
            self,
            fieldName,
            fieldType,
            value,
            date,
            number,
            unit,
            filepath=filepath,
            extraParams=extraParams,
        )

    def getMetadata(self):
        """
        Retrieve the Metadata of the Resource Template.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An array of Metadata objects for the Resource.

        Example
        -------
        ::

            entity = user.getResourceCategory(17000)
            metadatas = entity.getMetadata()
        """
        import labstep.entities.metadata.repository as metadataRepository

        return metadataRepository.getMetadata(self)
