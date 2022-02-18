#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime


class ExperimentSignatureRequest(Entity):
    __entityName__ = "signature-request"

    def cancel(self):
        """
        Cancels the signature request.

        Returns
        -------
        :class:`~labstep.entities.experimentSignatureRequest.model.ExperimentSignatureRequest`
            An object representing the revoked signature.
        """
        import labstep.generic.entity.repository as entityRepository

        fields = {"deleted_at": getTime()}
        return entityRepository.editEntity(self, fields)
