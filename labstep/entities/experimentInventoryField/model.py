#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class ExperimentInventoryField(Entity):
    __entityName__ = "experiment-value"

    def __init__(self, data, user):
        super().__init__(data, user)
        self.amount = self.value

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
