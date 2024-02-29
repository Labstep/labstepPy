from labstep.entities.notification.model import Notification
from labstep.generic.entity.repository import getEntities, newEntity, editEntity, getEntity
from labstep.constants import UNSPECIFIED


def getNotification(user,
                    guid,):
    return getEntity(user, Notification, guid=guid)


def getNotifications(user,
                     count=UNSPECIFIED,
                     type=UNSPECIFIED,
                     extraParams={},):

    params = {
        'type': type,
        **extraParams,
    }
    return getEntities(user, Notification, count, params)
