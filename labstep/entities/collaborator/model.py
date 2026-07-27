#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
import labstep.entities.collaborator.repository as collaboratorRepository

class Collaborator(Entity):
    __entityName__ = "entity-user"
    __unSearchable__=True

    def unassign (self):
        """
        Unassign collabortor.

        Example
        -------
        ::
            experiment = getExperiment(1000)
            collaborators = experiment.getCollaborators()
            collaborators[0].unassign()
        """
        return collaboratorRepository.unassign(self)
        