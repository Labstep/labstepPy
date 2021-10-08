#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.generic.entity.repository import entityRepository
from labstep.service.helpers import getTime


class ExperimentDataField(Entity):
    """
    Represents a single data field attached to a Labstep Experiment.

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
        :class:`~labstep.entities.experimentDataField.model.ExperimentDataField`
            An object representing the edited data field.

        Example
        -------
        ::

            data.edit(value='2.50')
        """
        from labstep.entities.experimentDataField.repository import experimentDataFieldRepository

        return experimentDataFieldRepository.editDataField(
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
        from labstep.entities.experimentDataField.repository import experimentDataFieldRepository

        return experimentDataFieldRepository.editDataField(
            self, extraParams={"deleted_at": getTime()}
        )

    def linkToMaterial(self, material):
        """
        Link a data field to a material.

        Parameters
        ----------
        material
            The :class:`~labstep.entities.experimentMaterial.model.ExperimentMaterial` to link the data field to.

        Example
        -------
        ::

            material = experiment.addMaterial('Sample')
            data = experiment.addDataField('Concentration')
            data.linkToMaterial(material)
        """
        return entityRepository.linkEntities(self.__user__, self, material)

    def getLinkedMaterials(self):
        """
        Returns the materials linked to this data field..

        Returns
        ----------
        List[:class:`~labstep.entities.experimentMaterial.model.ExperimentMaterial`]
            The material link the data field to.

        Example
        -------
        ::

            material = experiment.addMaterial('Sample')
            data = experiment.addDataField('Concentration')
            data.linkToMaterial(material)
        """
        from labstep.entities.experimentMaterial.repository import experimentMaterialRepository

        if self.experiment_id is not None:

            return experimentMaterialRepository.getExperimentMaterials(
                user=self.__user__,
                experiment_id=self.experiment_id,
                extraParams={'metadata_id': self.id}
            )
