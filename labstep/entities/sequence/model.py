#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED
from labstep.service.helpers import getTime

class Sequence(Entity):
    """
    Represents a sequence in an Experiment

    """
    __entityName__ = "sequence"
    __hasGuid__ = False

    def edit(self, data=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Sequence entity.

        Parameters
        ----------
        name (str)
            Sequence name
        data (str)
            JSON data for the reaction

        Returns
        -------
        :class:`~labstep.entities.sequence.model.Sequence`
            An object representing the edited sequence.


        Example
        -------
        ::

            
        """
        import labstep.generic.entity.repository as entityRepository

        params = {
            
            "data": data,
            **extraParams
        }
        return entityRepository.editEntity(self, params)

    def delete(self):
        """
        Delete the sequence.

        Example
        -------
        ::

        """
        import labstep.entities.sequence.repository as sequenceRepository

        return sequenceRepository.editSequence(self, deleted_at=getTime())
    