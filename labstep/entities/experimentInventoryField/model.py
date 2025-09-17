#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.generic.entity.repository import getEntityProperty
from labstep.entities.resource.model import Resource
from labstep.entities.resourceItem.model import ResourceItem
from labstep.constants import UNSPECIFIED
import labstep.generic.entity.repository as entityRepository



class ExperimentInventoryField(Entity):
    __entityName__ = "protocol-value"
    __hasGuid__ = True

    def __init__(self, data, user):
        super().__init__(data, user)
        self.amount = self.value

    @property
    def resource(self):
        return getEntityProperty(self, 'resource', Resource)

    @property
    def resource_item(self):
        return getEntityProperty(self, 'resource_item', ResourceItem)

    def edit(self, name=UNSPECIFIED, amount=UNSPECIFIED, units=UNSPECIFIED, resource_id=UNSPECIFIED, resource_item_id=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Experiment Inventory Field.

        Parameters
        ----------
        amount (str)
            The amount used / produced in the experiment.
        units (str)
            The units of the amount.
        resource_id (int)
            The :class:`~labstep.entities.resource.model.Resource` of the Experiment Inventory Field.
        resource_item_id (int)
            The id of the :class:`~labstep.entities.resource.model.ResourceItem`
            of the Experiment Inventory Field.

        Returns
        -------
        :class:`~labstep.entities.experimentInventoryField.model.ExperimentInventoryField`
            An object representing the edited Experiment Inventory Field.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_inventory = exp_protocol.getInventoryFields()
            exp_protocol_inventory[0].edit(amount=1.7, units='ml')
        """
        import labstep.entities.experimentInventoryField.repository as experimentInventoryFieldRepository

        return experimentInventoryFieldRepository.editExperimentInventoryField(self,
                                                                               name=name,
                                                                               amount=amount,
                                                                               units=units,
                                                                               resource_id=resource_id,
                                                                               resource_item_id=resource_item_id,
                                                                               extraParams=extraParams)

    def setValue(self,amount,resource_item_id,condition_id=UNSPECIFIED):
        """
        Sets the amount associated with this inventory field.

        Parameters
        ----------
        amount : float
            The amount to set.
        """
        import labstep.entities.experimentInventoryField.repository as experimentInventoryFieldRepository

        return experimentInventoryFieldRepository.setValue(self, amount=amount, resource_item_id=resource_item_id,condition_id=condition_id)