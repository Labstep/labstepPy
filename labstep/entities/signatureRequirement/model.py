#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from deprecated import deprecated
from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime, handleDate
from labstep.constants import UNSPECIFIED


class SignatureRequirement(Entity):
    """
    Represents a Signature Requirement on Labstep.

    """

    __entityName__ = "signature-requirement"

    def edit(self, statement=UNSPECIFIED, days_to_sign=UNSPECIFIED, reject_entity_state_id=UNSPECIFIED, extraParams={}):
        """
        Edit an existing SignatureRequirement.

        Parameters
        ----------
        default_statement (str)
            The new default statement of the SignatureRequirement.

        days_to_sign(int)
            The new days to sign of the SignatureRequirement.

        reject_entity_state_id(int)
            The entity state ID on reject of the SignatureRequirement.

        Returns
        -------
        :class:`~labstep.entities.signatureRequirement.model.SignatureRequirement`
            An object representing the edited SignatureRequirement.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            collaborator_role = workspace.getCollaboratorRole(17000)
            my_entity_state = my_entity_state_workflow.getEntityStates()
            collaboratorRoleRequirement = my_entity_state[0].addRoleRequirement(entity_user_role_id=collaborator_role.id, number_required=2)
            my_signature_requirements = collaboratorRoleRequirement.getSignatureRequirements()
            my_signature_requirements.edit(statement='A New SignatureRequirement Default Statement')
        """
        import labstep.entities.signatureRequirement.repository as signatureRequirementRepository

        return signatureRequirementRepository.editSignatureRequirement(self, statement=statement, days_to_sign=days_to_sign, reject_entity_state_id=reject_entity_state_id, extraParams=extraParams)

    def disableSignatureRequirement(self, extraParams={}):
        """
        Disable an existing SignatureRequirement.

        Returns
        -------
        :class:`~labstep.entities.signatureRequirement.model.SignatureRequirement`
            An object representing the edited SignatureRequirement.

        Example
        -------
        ::

            my_entity_state_workflow = user.getEntityStateWorkflow(17000)
            collaborator_role = workspace.getCollaboratorRole(17000)
            my_entity_state = my_entity_state_workflow.getEntityStates()
            collaboratorRoleRequirement = my_entity_state[0].addRoleRequirement(entity_user_role_id=collaborator_role.id, number_required=2)
            my_signature_requirements = collaboratorRoleRequirement.getSignatureRequirements()
            my_signature_requirements.disableSignatureRequirement()
        """
        return self.delete()