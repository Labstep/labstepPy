#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime


class ExperimentSignature(Entity):
    __entityName__ = "signature"

    def revoke(self):
        """
        Revokes the signature.

        Returns
        -------
        :class:`~labstep.entities.experimentSignature.model.ExperimentSignature`
            An object representing the revoked signature.
        """
        import labstep.generic.entity.repository as entityRepository

        fields = {"revoked_at": getTime()}
        return entityRepository.editEntity(self, fields)
