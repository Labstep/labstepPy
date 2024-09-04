#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from deprecated import deprecated
from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime, handleDate
from labstep.constants import UNSPECIFIED


class CollaboratorRoleRequirement(Entity):
    """
    Represents a requirement for a particular Collaborator role to be assigned at a particular state an the EntityStateWorkflow.

    """

    __entityName__ = "entity-user-role-requirement"

    # @property
    # def signature_requirement(self):
    #     from labstep.generic.entity.repository import getEntityProperty
    #     from labstep.entities.signatureRequirement.model import SignatureRequirement

    #     return SignatureRequirement(self.__data__['signature_requirement'], self.__user__)
    #     #return getEntityProperty(self,'signature_requirement',SignatureRequirement)

    def edit(self, number_required=UNSPECIFIED, collaborator_role_id=UNSPECIFIED, auto_assign=UNSPECIFIED, extraParams={}):
        """
        Edit an existing CollaboratorRoleRequirement.

        Parameters
        ----------
        number_required (int)
            The new number of CollaboratorRoleRequirement.

        Returns
        -------
        :class:`~labstep.entities.collaboratorRoleRequirement.model.CollaboratorRoleRequirement`
            An object representing the edited CollaboratorRoleRequirement.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            my_entity_state = my_entity_state_workflow.newEntityState(name='A New EntityState Name')
            collaborator_requirements=my_entity_state.addRoleRequirement(collaborator_role_id=17000, number_required=4)
            collaborator_requirements.edit(number_required=2)
        """
        import labstep.entities.collaboratorRoleRequirement.repository as collaboratorRoleRequirementRepository

        return collaboratorRoleRequirementRepository.editCollaboratorRoleRequirement(self, number_required=number_required, collaborator_role_id=collaborator_role_id, auto_assign=auto_assign, extraParams=extraParams)



    def getSignatureRequirement(self):
        """
        Get a SignatureRequirement of a Collaborator Role Requirement.


        Returns
        -------
        :class:`~labstep.entities.signatureRequirement.model.SignatureRequirement`
            An object representing the SignatureRequirement.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            my_entity_state = my_entity_state_workflow.newEntityState(name='A New EntityState Name')
            collaborator_req=my_entity_state.addRoleRequirement(collaborator_role_id=17000,
                                                                         number_required=2
                                                                         )
            signature_requirement = collaborator_req.getSignatureRequirement()
        """
        import labstep.entities.signatureRequirement.repository as signatureRequirementRepository

        return signatureRequirementRepository.getSignatureRequirement(self.__user__, self)

    def setSignatureRequirement(self, statement=UNSPECIFIED, days_to_sign=UNSPECIFIED, reject_entity_state_id=UNSPECIFIED, extraParams={}):
        """
        Set SignatureRequirement of a Collaborator Role Requirement.

        Parameters
        ----------
        required (bool)
            If the SignatureRequirement is required.

        default_statement (str)
            The default statement of the SignatureRequirement.

        days_to_sign(int)
            The days to sign of the SignatureRequirement.

        reject_entity_state_id(int)
            The ID of the entity state on reject of the SignatureRequirement.

        Returns
        -------
        :class:`~labstep.entities.signatureRequirement.model.SignatureRequirement`
            An object representing the edited SignatureRequirement.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            my_entity_state = my_entity_state_workflow.newEntityState(name='A New EntityState Name')
            collaborator_requirements=my_entity_state.addRoleRequirement(collaborator_role_id=17000, number_required=2)
            my_signature_requirement = collaborator_requirements.setSignatureRequirement(default_statement='A New SignatureRequirement Default Statement')
        """
        import labstep.entities.signatureRequirement.repository as signatureRequirementRepository

        return signatureRequirementRepository.setSignatureRequirement(self.__user__, self, statement=statement, days_to_sign=days_to_sign, reject_entity_state_id=reject_entity_state_id, extraParams=extraParams)