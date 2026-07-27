from labstep.constants import UNSPECIFIED
from labstep.entities.activityLog.model import ActivityLog
from labstep.service.helpers import handleDate
import labstep.generic.entity.repository as entityRepository



def getActivityLogs(user, author_id=UNSPECIFIED, organization_id=UNSPECIFIED, workspace_id=UNSPECIFIED, count=UNSPECIFIED, created_at_from=UNSPECIFIED, created_at_to=UNSPECIFIED, extraParams={}):
    params = {
        "author_id": author_id,
        "organization_id": organization_id,
        "workspace_id": workspace_id,
        "created_at_from": handleDate(created_at_from),
        "created_at_to": handleDate(created_at_to),
        "action_not": "security",
        "has_request_trace": True,
        **extraParams,
    }
    return entityRepository.getEntities(user, ActivityLog, count, params)