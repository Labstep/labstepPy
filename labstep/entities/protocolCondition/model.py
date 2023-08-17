#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Reynol Diaz <reynol.diaz@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.generic.entityList.model import EntityList
from labstep.generic.entity.repository import getEntities
from labstep.entities.protocolDataField.model import ProtocolDataField
from labstep.entities.protocolInventoryField.model import ProtocolInventoryField
from labstep.constants import UNSPECIFIED

class ProtocolCondition(Entity):
    __entityName__ = "protocol-condition"
    __unSearchable__=True

    def getDataFields(self):
        """
        Returns the variable data fields associated with this condition.
        Returns
        -------
        List[:class:`~labstep.entities.protocolDataField.model.ProtocolDataField`]
            An array of objects representing the Labstep Data Fields on an Protocol.
        Example
        -------
        ::
            protocol = user.getProtocol(17000)
            condition = protocol.getConditions()[0]
            dataFields = condition.getDataFields()
        """
        from labstep.generic.entityList.model import EntityList

        return EntityList(self.metadatas, ProtocolDataField,self.__user__)
    

    def getInventoryFields(self):
        """
        Returns the variable inventory fields associated with this condition.
        Returns
        -------
        List[:class:`~labstep.entities.protocolInventoryField.model.ProtocolInventoryField`]
            An array of objects representing the Labstep Inventory Fields on an Protocol.
        Example
        -------
        ::
            protocol = user.getProtocol(17000)
            condition = protocol.getConditions()[0]
            inventoryFields = condition.getInventoryFields()
        """
        from labstep.generic.entityList.model import EntityList

        return EntityList(self.protocol_values, ProtocolInventoryField,self.__user__)
       