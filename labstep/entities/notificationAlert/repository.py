#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.notificationAlert.model import NotificationAlert
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getNotificationAlert(user, guid):
    return entityRepository.getEntity(user, NotificationAlert, id=guid)


def newNotificationAlert(user, metadata_guid, message=UNSPECIFIED, minutes_before=0, extraParams={}):
    params = {
        "metadata_guid": metadata_guid,
        "message": message,
        "minutes_before": minutes_before,
        **extraParams
    }
    return entityRepository.newEntity(user, NotificationAlert, params)


def editNotificationAlert(notificationAlert, message=UNSPECIFIED, minutes_before=UNSPECIFIED, extraParams={}):
    params = {"message": message,
              "minutes_before": minutes_before, **extraParams}
    return entityRepository.editEntity(notificationAlert, params)


def setNotificationAlert(metadata, message, minutes_before):
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
        resource_item = user.getResourceItem(17000)
        expiry_date = resource_item.getMetadata().get('Expiry Date')
        expiry_date.setNotificationAlert(
            message='This item is expired', minutes_before=0)
    """
    if metadata.type not in ['date', 'datetime']:
        raise Exception(
            'Can only set alerts for metadata types: date or datetime')

    notificationAlert = metadata.getNotificationAlert()

    if notificationAlert is not None:

        return notificationAlert.edit(
            message=message, minutes_before=minutes_before, extraParams={'deleted_at': None})

    return newNotificationAlert(metadata.__user__, metadata_guid=metadata.guid, message=message, minutes_before=minutes_before)
