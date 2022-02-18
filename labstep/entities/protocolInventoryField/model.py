#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class ProtocolInventoryField(Entity):
    __entityName__ = "protocol-value"

    def __init__(self, data, user):
        super().__init__(data, user)
        self.amount = self.value

    def edit(
        self, name=UNSPECIFIED, amount=UNSPECIFIED, units=UNSPECIFIED, resource_id=UNSPECIFIED, extraParams={}
    ):
        """
        Edit an existing Protocol Inventory Field.

        Parameters
        ----------
        name (str)
            The name of the Protocol Inventory Field.
        amount (str)
            The amount of the Protocol Inventory Field.
        units (str)
            The units of the amount.
        resource_id (Resource)
            The id of the :class:`~labstep.entities.resource.model.Resource` of
            the Protocol InventoryField.

        Returns
        -------
        :class:`~labstep.entities.protocolInventoryField.model.ProtocolInventoryField`
            An object representing the edited Protocol Inventory Field.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_inventory_fields = exp_protocol.getInventoryFields()
            protocol_inventory_fields[0].edit(value=1.7, units='ml')
        """
        import labstep.entities.protocolInventoryField.repository as protocolInventoryFieldRepository

        return protocolInventoryFieldRepository.editProtocolInventoryField(self,
                                                                           name=name,
                                                                           amount=amount,
                                                                           units=units,
                                                                           resource_id=resource_id,
                                                                           extraParams=extraParams)
