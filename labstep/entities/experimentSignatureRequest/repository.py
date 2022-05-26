
from labstep.entities.experimentSignatureRequest.model import ExperimentSignatureRequest
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def newExperimentSignatureRequest(user, experiment_id, user_id, message=UNSPECIFIED):
    fields = {
        "experiment_workflow_id": experiment_id,
        "message": message,
        "user_id": user_id
    }
    return entityRepository.newEntity(user, ExperimentSignatureRequest, fields=fields)


def getExperimentSignatureRequests(user, experiment_id):
    params = {
        "experiment_workflow_id": experiment_id,
        "search": None,
    }
    return entityRepository.getEntities(user, ExperimentSignatureRequest, filterParams=params, count=100)
