#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED
from labstep.service.helpers import getTime


class NotificationAlert(Entity):
    """
    Represents an Alert on a date-based metadata field on Labstep.
    """

    __entityName__ = "notification-alert"
    __hasGuid__ = True

    def edit(self, message=UNSPECIFIED, minutes_before=UNSPECIFIED, extraParams={}):
        """
        Update the notification alert

        Parameters
        ----------
        message (str)
            The message to display when the alert triggers
        minutes_before (int)
            The number of minutes before the date on the metadata field that the notification should trigger

        Returns
        -------
        :class:`~labstep.entities.notficationAlert.model.NotificationAlert`
            An object representing the NotificationAlert

        Example
        -------
        ::
            resource_item = user.getResourceItem(17000)
            expiry_date = resource_item.getMetadata().get('Expiry Date')
            notification_alert = expiry_date.getNotificationAlert()
            notifcation_alert.edit(message='This item has expired')

        """
        from labstep.entities.notificationAlert.repository import editNotificationAlert

        return editNotificationAlert(self, message=message, minutes_before=minutes_before, extraParams=extraParams)

    def enable(self):
        """
        Enables the notification alert

        Returns
        -------
        :class:`~labstep.entities.notficationAlert.model.NotificationAlert`
            An object representing the NotificationAlert

        Example
        -------
            resource_item = user.getResourceItem(17000)
            expiry_date = resource_item.getMetadata().get('Expiry Date')
            notification_alert = expiry_date.getNotificationAlert()
            notification_alert.enable()
        """

        return self.edit(extraParams={'deleted_at': None})

    def disable(self):
        """
        Disables the notification alert

        Returns
        -------
        :class:`~labstep.entities.notficationAlert.model.NotificationAlert`
            An object representing the NotificationAlert

        Example
        -------
            resource_item = user.getResourceItem(17000)
            expiry_date = resource_item.getMetadata().get('Expiry Date')
            notification_alert = expiry_date.getNotificationAlert()
            notification_alert.disable()
        """

        return self.edit(extraParams={'deleted_at': getTime()})
