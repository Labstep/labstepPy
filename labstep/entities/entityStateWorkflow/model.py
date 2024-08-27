#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from deprecated import deprecated

from labstep.generic.entityWithSharing.model import EntityWithSharing
from labstep.generic.entityWithAssign.model import EntityWithAssign
from labstep.service.helpers import getTime, handleDate
from labstep.constants import UNSPECIFIED


class EntityStateWorkflow(EntityWithSharing,EntityWithAssign):
    """
    Represents a series of states an entity must go through, including who needs to sign / be assigned at each stage.

    """

    __entityName__='entity-state-workflow'
    __hasParentGroup__ = True

    def edit(self, name=UNSPECIFIED, extraParams={}):
        """
        Edit an existing EntityStateWorkflow.

        Parameters
        ----------
        name (str)
            The new name of the EntityStateWorkflow.

        Returns
        -------
        :class:`~labstep.entities.EntityStateWorkflow.model.EntityStateWorkflow`
            An object representing the edited EntityStateWorkflow.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            my_entity_state_workflow.edit(name='A New EntityStateWorkflow Name')
        """
        import labstep.entities.entityStateWorkflow.repository as entityStateWorkflowRepository

        return entityStateWorkflowRepository.editEntityStateWorkflow(self, name=name, extraParams=extraParams)


    def newEntityState(self, name, color='#0057dd', type='unstarted', extraParams={}):
        """
        Add an EntityState to an EntityStateWorkflow.

        Parameters
        ----------
        name (str)
            The name of the EntityState.

        color in HEX value(str)
            The color of the EntityState.

        type(str)
            The type of the EntityState. It can be one of the following: 'unstarted',
            'started', and 'complete'.


        Returns
        -------
        :class:`~labstep.entities.entityState.model.EntityState`
            An object representing the EntityState.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            my_entity_state_workflow.newEntityState(name='A New EntityState Name')
        """
        import labstep.entities.entityState.repository as entityStateRepository
        return entityStateRepository.addEntityState(self.__user__, name, color, type,  self.id, extraParams=extraParams)

    def getEntityState(self, entity_state_id):
        """
        Get an EntityState in an EntityStateWorkflow.

        Parameters
        ----------
        entity_state_id(int)
            The ID of the EntityState.

        Returns
        -------
        :class:`~labstep.entities.entityState.model.EntityState`
            An object representing the EntityState.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            my_entity_state_workflow.getEntityState(17000)
        """
        import labstep.entities.entityState.repository as entityStateRepository
        return entityStateRepository.getEntityState(self.__user__, entity_state_id, entity_state_workflow_id=self.id)

    def getEntityStates(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
        """
        Get all EntityStates in an EntityStateWorkflow.

        Parameters
        ----------

        count(int)
            The number of EntityStates to return.

        search_query(str)
            The search query to filter EntityStates.

        Returns
        -------
        :class:`~labstep.entities.entityState.model.EntityState`
            An object representing the EntityState.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            my_entity_state_workflow.getEntityStates()
        """
        import labstep.entities.entityState.repository as entityStateRepository

        return entityStateRepository.getEntityStates(self.__user__, self.id, count=count, search_query=search_query, extraParams=extraParams)
