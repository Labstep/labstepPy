#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from deprecated import deprecated
from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime, handleDate
from labstep.constants import UNSPECIFIED


class EntityState(Entity):
    """
    Represents an Entity State Workflow on Labstep.

    """

    __entityName__ = "entity-state"
    __unSearchable__ = True
    __noDelete__ = True

    def edit(self, name=UNSPECIFIED, color=UNSPECIFIED, state_type=UNSPECIFIED, extraParams={}):
        """
        Edit an existing EntityState.

        Parameters
        ----------
        name (str)
            The new name of the EntityState.

        color in HEX vaue(str)
            The new color of the EntityState.

        type(str)
            The new type of the EntityState. It can be one of the following: 'unstarted',
            'started', and 'complete'.

        Returns
        -------
        :class:`~labstep.entities.entityState.model.EntityState`
            An object representing the edited EntityState.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            my_entity_state = my_entity_state_workflow.getEntityState(17000)
            my_entity_state.edit(name='A New EntityState Name')
        """
        import labstep.entities.entityState.repository as entityStateRepository

        return entityStateRepository.editEntityState(self, name=name, color=color, state_type=state_type, extraParams=extraParams)



    def addRoleRequirement(self, collaborator_role_id, number_required=1, extraParams={}):
        """
        Create a new RoleRequirement.

        Parameters
        ----------
        collaborator_rol_id (int)
            ID of the collaborator role.

        number_required(int)
            Number of collaborators required.


        Returns
        -------
        :class:`~labstep.entities.collaboratorRoleRequirement.model.CollaboratorRoleRequirement`
            An object representing the edited CollaboratorRoleRequirement.

        Example
        -------
        ::
            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            collaborator_role = workspace.getCollaboratorRole(17000)
            my_entity_state = my_entity_state_workflow.getEntityStates()
            my_entity_state[0].addRoleRequirement(entity_user_role_id=collaborator_role.id, number_required=2)
        """
        import labstep.entities.collaboratorRoleRequirement.repository as collaboratorRoleRequirementRepository

        return collaboratorRoleRequirementRepository.addCollaboratorRoleRequirement(self.__user__,
                                                                                    entity_state= self,
                                                                                    entity_user_role_id=collaborator_role_id,
                                                                                    number_required=number_required,
                                                                                    extraParams=extraParams)

    def getCollaboratorRoleRequirements(self):
        """
        Get all RoleRequirements of an EntityState.

        Returns
        -------
        List[:class:`~labstep.entities.collaboratorRoleRequirement.model.CollaboratorRoleRequirement`]
            A list of objects representing CollaboratorRoleRequirements.

        Example
        -------
        ::

            my_entity_state = entityWorkflow.getEntityState(17000)
            role_requirements = my_entity_state.getCollaboratorRoleRequirements()
        """
        import labstep.entities.collaboratorRoleRequirement.repository as collaboratorRoleRequirementRepository

        return collaboratorRoleRequirementRepository.getCollaboratorRoleRequirements(self.__user__, self)