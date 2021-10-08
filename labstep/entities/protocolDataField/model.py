#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.generic.entity.repository import entityRepository
from labstep.service.helpers import getTime


class ProtocolDataField(Entity):
    """
    Represents a data field on a Labstep Protocol.

    To see the attributes of the data field run
    ::
        print(my_data_field)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_data_field.value)
        print(my_data_field.id)
    """

    __entityName__ = "metadata"

    def edit(self, fieldName=None, value=None, extraParams={}):
        """
        Edit the value of an existing data field.

        Parameters
        ----------
        fieldName (str)
            The new name of the field.
        value (str)
            The new value of the data.

        Returns
        -------
        :class:`~labstep.entities.protocolDataField.model.ProtocolDataField`
            An object representing the edited data field.

        Example
        -------
        ::

            data.edit(value='2.50')
        """
        from labstep.entities.protocolDataField.repository import protocolDataFieldRepository

        return protocolDataFieldRepository.editDataField(
            self, fieldName, value, extraParams=extraParams
        )

    def delete(self):
        """
        Delete an existing Data field.

        Example
        -------
        ::

            data.delete()
        """
        from labstep.entities.protocolDataField.repository import protocolDataFieldRepository

        return protocolDataFieldRepository.editDataField(
            self, extraParams={"deleted_at": getTime()}
        )

    def linkToMaterial(self, material):
        """
        Link a data field to a material.

        Parameters
        ----------
        material :class:`~labstep.entities.protocolMaterial.model.ProtocolMaterial`
            The material to link the data field to.

        Example
        -------
        ::

            material = protocol.addMaterial('Sample')
            data = protocol.addDataField('Concentration')
            data.linkToMaterial(material)
        """
        return entityRepository.linkEntities(self.__user__, self, material)

    def getLinkedMaterials(self):
        """
        Returns the materials linked to this data field..

        Parameters
        ----------
        List[:class:`~labstep.entities.protocolMaterial.model.ProtocolMaterial`]
            The material link the data field to.

        Example
        -------
        ::

            material = protocol.addMaterial('Sample')
            data = protocol.addDataField('Concentration')
            data.linkToMaterial(material)
        """
        from labstep.entities.protocolMaterial.repository import protocolMaterialRepository

        if self.protocol_id is not None:

            return protocolMaterialRepository.getProtocolMaterials(
                user=self.__user__,
                protocol_id=self.protocol_id,
                extraParams={'metadata_id': self.id}
            )
