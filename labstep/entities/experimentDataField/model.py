#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from deprecated import deprecated
from labstep.generic.entityWithComments.model import EntityWithComments
import labstep.generic.entity.repository as entityRepository
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class ExperimentDataField(EntityWithComments):
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
    __searchKey__ = 'label'

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
        :class:`~labstep.entities.experimentDataField.model.ExperimentDataField`
            An object representing the edited data field.

        Example
        -------
        ::

            data.edit(value='2.50')
        """
        import labstep.entities.experimentDataField.repository as experimentDataFieldRepository

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
        import labstep.entities.experimentDataField.repository as experimentDataFieldRepository

        return experimentDataFieldRepository.editDataField(
            self, extraParams={"deleted_at": getTime()}
        )

    def linkToInventoryField(self, inventoryField):
        """
        Link a data field to an inventory field.

        Parameters
        ----------
        inventoryField
            The :class:`~labstep.entities.experimentInventoryField.model.ExperimentInventoryField` to link the data field to.

        Example
        -------
        ::

            inventoryField = experiment.addInventoryField('Sample')
            data = experiment.addDataField('Concentration')
            data.linkToInventoryField(inventoryField)
        """
        return entityRepository.linkEntities(self.__user__, self, inventoryField)

    def getLinkedInventoryFields(self):
        """
        Returns the inventory fields linked to this data field..

        Returns
        ----------
        List[:class:`~labstep.entities.experimentInventoryField.model.ExperimentInventoryField`]
            The inventory field link the data field to.

        Example
        -------
        ::

            inventoryField = experiment.addInventoryField('Sample')
            data = experiment.addDataField('Concentration')
            data.linkToInventoryField(inventoryField)
        """
        import labstep.entities.experimentInventoryField.repository as experimentInventoryFieldRepository

        if self.experiment_id is not None:

            return experimentInventoryFieldRepository.getExperimentInventoryFields(
                user=self.__user__,
                experiment_id=self.experiment_id,
                extraParams={'metadata_id': self.id}
            )

    def getValue(self):
        """
        Returns the value of the data field.

        Returns
        ----------
        Return type depends on the data type of the data field

        Example
        -------
        ::

            dataField = experiment.getDataFields()[0]
            value = dataField.getValue()
        """

        import labstep.entities.experimentDataField.repository as experimentDataFieldRepository

        return experimentDataFieldRepository.getDataFieldValue(self)

    def setValue(self, value):
        """
        Sets the value of the data field.

        Parameters
        ----------
        value 
            The value to set, depends on the type of the data field. 

        Returns
        ----------
        Return type depends on the data type of the data field

        Example
        -------
        ::

            dataFields = experiment.getDataFields()
            textField = dataFields.get('My text field')
            textField.setValue('Some String')

            numericField = dataFields.get('My numeric field')
            numericField.setValue(56534)

            dateField = dataFields.get('My date field')
            dateField.setValue('2021-10-28')

            singleOptionsField = dataFields.get('My single options field')
            singleOptionsField.setValue('Option 1')

            multiOptionsField = dataFields.get('My multi options field')
            multiOptionsField.setValue(['Option 1','Option 2'])

            fileField = dataFields.get('My file field')
            file = user.newFile('/path/to/file')
            fileField.setValue(file)

        """

        import labstep.entities.experimentDataField.repository as experimentDataFieldRepository

        return experimentDataFieldRepository.setDataFieldValue(self, value)

    @deprecated(version='3.12.0', reason="You should use linkToInventoryField instead")
    def linkToMaterial(self, *args, **kwargs):
        return self.linkToInventoryField(*args, **kwargs)
