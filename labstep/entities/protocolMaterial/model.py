#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity


class ProtocolMaterial(Entity):
    __entityName__ = "protocol-value"

    def __init__(self, data, user):
        super().__init__(data, user)
        self.amount = self.value

    def edit(
        self, name=None, amount=None, units=None, resource_id=None, extraParams={}
    ):
        """
        Edit an existing Protocol Material.

        Parameters
        ----------
        name (str)
            The name of the Protocol Material.
        amount (str)
            The amount of the Protocol Material.
        units (str)
            The units of the amount.
        resource_id (Resource)
            The id of the :class:`~labstep.entities.resource.model.Resource` of
            the Protocol Material.

        Returns
        -------
        :class:`~labstep.entities.protocolMaterial.model.ProtocolMaterial`
            An object representing the edited Protocol Material.

        Example
        -------
        ::

            protocol = user.getProtocol(17000)
            protocol_materials = exp_protocol.getMaterials()
            protocol_materials[0].edit(value=1.7, units='ml')
        """
        from labstep.entities.protocolMaterial.repository import protocolMaterialRepository

        return protocolMaterialRepository.editProtocolMaterial(self,
                                                               name=name,
                                                               amount=amount,
                                                               units=units,
                                                               resource_id=resource_id,
                                                               extraParams=extraParams)
