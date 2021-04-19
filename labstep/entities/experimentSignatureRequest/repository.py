
from labstep.entities.experimentSignatureRequest.model import ExperimentSignatureRequest
from labstep.generic.entity.repository import entityRepository


class ExperimentSignatureRequestRepository:
    def newExperimentSignatureRequest(self, user, experiment_id, user_id, message=None):
        fields = {
            "experiment_workflow_id": experiment_id,
            "message": message,
            "user_id": user_id
        }
        return entityRepository.newEntity(user, ExperimentSignatureRequest, fields=fields)

    def getExperimentSignatureRequests(self, user, experiment_id):
        params = {
            "experiment_workflow_id": experiment_id,
            "search": None,
        }
        return entityRepository.getEntities(user, ExperimentSignatureRequest, filterParams=params, count=100)


experimentSignatureRequestRepository = ExperimentSignatureRequestRepository()
