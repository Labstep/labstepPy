from labstep.generic.entity.repository import getEntities, newEntity
from labstep.entities.experimentLink.model import ExperimentLink


def newExperimentLink(user, src_experiment_id, dest_experiment_id):

    return newEntity(user, ExperimentLink, {'src_id': src_experiment_id, 'dest_id': dest_experiment_id})


def getExperimentLinks(user, experiment_id, direction='forward'):

    if direction == 'forward':

        return getEntities(user, ExperimentLink, count=1000,
                           filterParams={'src_id': experiment_id})

    if direction == 'backwards':
        return getEntities(user, ExperimentLink, count=1000,
                           filterParams={'dest_id': experiment_id})
