from labstep.entities.notification.model import Notification
from labstep.generic.entity.repository import getEntities, newEntity, editEntity, getEntity
from labstep.constants import UNSPECIFIED


def getNotification(user,
                    id,):
    return getEntity(user, Notification, id=id)


def getNotifications(user,
                     count=UNSPECIFIED,
                     notification_type=UNSPECIFIED,
                     extraParams={},):

    params = {
        'type': notification_type,
        **extraParams,
    }
    return getEntities(user, Notification, count, params)
