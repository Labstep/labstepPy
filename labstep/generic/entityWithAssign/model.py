from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED
import labstep.entities.collaborator.repository as collaboratorRepository


class EntityWithAssign(Entity):
    def assign(self,user_id,extraParams={}):
        """
        Assign a user to a Labstep Entity as a Collaborator.

        Parameters
        ----------
        user_id (int)
            User to be assigned.

        Returns
        -------
        :class:`~labstep.entities.collaborator.model.Collaborator`
            The collaborator added.

        Example
        -------
        ::
            user_id = 120
            experiment= getExperiment(10000)
            collaborator = experiment.assign(user_id)
    
        """
        
        return collaboratorRepository.assign(parent_entity=self,
                                             user_id=user_id,
                                             extraParams=extraParams)
    
    def getCollaborators(self, count=UNSPECIFIED, extraParams={}):
        """
        Get Collaborators assigned into a Labstep Entity.

        Parameters
        ----------
        count (int)
            Number of collaborators to fetch.

        Returns
        -------
        List[:class:`~labstep.entities.collaborator.model.Collaborator`]
            List of the collaborators assigned.

        Example
        -------
        ::
            experiment= getExperiment(10000)
            collaborators = experiment.getCollaborators()
    
        """
        
        return collaboratorRepository.getCollaborators(parent_entity=self,
                                                       count=count,
                                                       extraParams=extraParams)