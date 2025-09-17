#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

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

    def edit(self, fieldName=UNSPECIFIED, value=UNSPECIFIED, is_variable=UNSPECIFIED, extraParams={}):
        """
        Edit the value of an existing data field.

        Parameters
        ----------
        fieldName (str)
            The new name of the field.
        value (str)
            The new value of the data.
        is_variable (boolean)
            Whether or not the field is a variable

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
            self, fieldName=fieldName, value=value, is_variable=is_variable, extraParams=extraParams
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

    def setValue(self, value, condition_id=None):
        """
        Sets the value of the data field.

        Parameters
        ----------
        value
            The value to set, depends on the type of the data field.

        condition_id (int, optional)
            The ID of the condition to set the value for (variable data fields only).

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

        return experimentDataFieldRepository.setDataFieldValue(self, value,condition_id=condition_id)

    def getNotificationAlert(self):
        """
        Retrieve the Notification Alert of a date type metadata field.

        Returns
        -------
        :class:`~labstep.entities.notificationAlert.model.notificationAlert`
            An object representing the notification alert of a
            metadata field of type Date or Date / Time.

        Example
        -------
        ::
            experiment = user.getExperiment(49574)
            dataField = experiment.getDataFields()[0]
            notification_alert = dataField.getNotificationAlert()
        """
        from labstep.entities.notificationAlert.model import NotificationAlert

        if self.notification_alert is None:
            return None

        return NotificationAlert(self.notification_alert, self.__user__)

    def setNotificationAlert(self, message, minutes_before):
        """
        Set the Notification Alert of a date type metadata field.

        Returns
        -------
        :class:`~labstep.entities.notificationAlert.model.notificationAlert`
            An object representing the notification alert of a
            metadata field of type Date or Date / Time.

        Example
        -------
        ::
            experiment = user.getExperiment(49574)
            dataField = experiment.getDataFields()[0]
            dataField.setNotificationAlert(message='Overdue', minutes_before=0)
        """
        from labstep.entities.notificationAlert.repository import setNotificationAlert

        return setNotificationAlert(self, message=message, minutes_before=minutes_before)

