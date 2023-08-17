#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Reynol Diaz <reynol.diaz@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.generic.entity.repository import getEntities
from labstep.entities.experimentDataField.model import ExperimentDataField
from labstep.entities.experimentInventoryField.model import ExperimentInventoryField

from labstep.constants import UNSPECIFIED

class ExperimentCondition(Entity):
    __entityName__ = "protocol-condition"
    __unSearchable__=True

                                                        
    def getDataFields(self):
        """
        Returns the variable data fields associated with this condition.
        Returns
        -------
        List[:class:`~labstep.entities.experimentDataField.model.ExperimentDataField`]
            An array of objects representing the Labstep Data Fields on an Experiment Protocol.
        Example
        -------
        ::
            experiment = user.getExperiment(17000)
            condition = experiment.getConditions()[0]
            dataFields = condition.getDataFields()
        """
        from labstep.generic.entityList.model import EntityList

        return EntityList(self.metadatas, ExperimentDataField,self.__user__)
    

    def getInventoryFields(self):
        """
        Returns the variable inventory fields associated with this condition.
        Returns
        -------
        List[:class:`~labstep.entities.experimentInventoryField.model.ExperimentInventoryField`]
            An array of objects representing the Labstep Inventory Fields on an Experiment Protocol.
        Example
        -------
        ::
            experiment = user.getExperiment(17000)
            condition = experiment.getConditions()[0]
            inventoryFields = condition.getInventoryFields()
        """
        from labstep.generic.entityList.model import EntityList

        return EntityList(self.protocol_values, ExperimentInventoryField,self.__user__)
       