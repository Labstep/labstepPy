#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import requests
from labstep.generic.entity.model import Entity
from labstep.service.config import configService
from labstep.service.helpers import url_join, getHeaders
from labstep.constants import UNSPECIFIED


class Sharelink(Entity):
    """
    Represents a Sharelink on Labstep.
    """

    __entityName__ = "share-link"
    __isLegacy__ = True

    def edit(self, permission=UNSPECIFIED, extraParams={}):
        """
        Edit a sharelink.

        Parameters
        ----------
        permission (str)
            Set the permission granted by the sharelink
            can be either 'view' or 'edit'

        Returns
        -------
        :class:`~labstep.entities.sharelink.model.Sharelink`
            An object representing the edited Sharelink.

        Example
        -------
        ::

            # Get an experiment
            experiment = user.getExperiment(123)

            # Get the sharelink for the experiment
            sharelink = experiment.getSharelink()

            # Edit the sharelink
            sharelink.edit(type='view')
        """
        import labstep.generic.entity.repository as entityRepository

        fields = {
            "type": permission,
            **extraParams,
        }
        return entityRepository.editEntity(self, fields=fields)

    def sendEmails(self, emails, message=UNSPECIFIED):
        """
        Send sharelinks to collaborators via email.

        Parameters
        ----------
        emails (list)
            A list of the emails to send the invite to.
        message (str)
            A message to send with the invite.


        Example
        -------
        ::

            sharelink.sendEmails(emails=['collegue1@labstep.com','collegue2@labstep.com'],
                message='Hi, please collaborate with me on Labstep!')
        """
        headers = getHeaders(self.__user__)

        url = url_join(configService.getHost(), "api/generic/share-link/email")
        fields = {"emails": emails, "message": message, "id": self.id}
        r = requests.post(url, json=fields, headers=headers)
