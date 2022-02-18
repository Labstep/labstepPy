#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class EntityWithMetadata(Entity):
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
        Add Metadata to a Labstep Entity.

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

            resource = user.getResource(17000)
            metadata = resource.addMetadata("Refractive Index",
                                               value="1.73")
        """
        import labstep.entities.metadata.repository as metadataRepository

        return metadataRepository.addMetadataTo(
            self,
            fieldName=fieldName,
            fieldType=fieldType,
            value=value,
            date=date,
            number=number,
            unit=unit,
            filepath=filepath,
            extraParams=extraParams,
        )

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep Entity.

        Returns
        -------
        :class:`~labstep.entities.metadata.model.Metadata`
            An array of Metadata objects for the Entity.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            metadatas = my_resource.getMetadata()
        """
        import labstep.entities.metadata.repository as metadataRepository

        return metadataRepository.getMetadata(self)
