#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from deprecated import deprecated
from labstep.generic.entity.model import Entity
import labstep.generic.entity.repository as entityRepository
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


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
    __searchKey__ = "label"

    def edit(self, fieldName=UNSPECIFIED, value=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.protocolDataField.repository as protocolDataFieldRepository

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
        import labstep.entities.protocolDataField.repository as protocolDataFieldRepository

        return protocolDataFieldRepository.editDataField(
            self, extraParams={"deleted_at": getTime()}
        )

    def linkToInventoryField(self, inventoryField):
        """
        Link a data field to an inventory field.

        Parameters
        ----------
        inventoryField :class:`~labstep.entities.protocolInventoryField.model.ProtocolInventoryField`
            The inventory field to link the data field to.

        Example
        -------
        ::

            inventoryField = protocol.addinventoryField('Sample')
            data = protocol.addDataField('Concentration')
            data.linkToInventoryField(inventoryfield)
        """
        return entityRepository.linkEntities(self.__user__, self, inventoryField)

    def getLinkedInventoryFields(self):
        """
        Returns the inventory fields linked to this data field.

        Example
        -------
        ::

            inventoryField = protocol.addInventoryField('Sample')
            data = protocol.addDataField('Concentration')
            data.linkToInventoryField(inventoryField)
            data.getLinkedInventoryFields()
        """
        import labstep.entities.protocolInventoryField.repository as protocolInventoryFieldRepository

        if self.protocol_id is not None:

            return protocolInventoryFieldRepository.getProtocolInventoryFields(
                user=self.__user__,
                protocol_id=self.protocol_id,
                extraParams={'metadata_id': self.id}
            )

    @deprecated(version='3.12.0', reason="You should use linkToInventoryField instead")
    def linkToMaterial(self, *args, **kwargs):
        return self.linkToInventoryField(*args, **kwargs)
