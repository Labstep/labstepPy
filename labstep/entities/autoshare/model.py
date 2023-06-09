#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class Autoshare(Entity):
    """
    Represents an Autosharing rule on Labstep.
    """

    __entityName__ = "security-policy"
    __isLegacy__ = True

    def edit(
        self,
        experiment_sharing=UNSPECIFIED,
        protocol_sharing=UNSPECIFIED,
        resource_sharing=UNSPECIFIED,
        extraParams={},
    ):
        """
        Edit an autosharing policy.

        Parameters
        ----------
        experiment_sharing (str)
            Automatically share experiments
            you create and own with this workspace. Set to True or False

        protocol_sharing (str)
            Automatically share protocols
            you create and own with this workspace. Set to True or False

        resource_sharing (str)
            Automatically share resources
            you create and own with this workspace. Set to True or False


        Returns
        -------
        :class:`~labstep.entities.autoshare.model.Autoshare`
            An object representing the Autosharing policy.

        Example
        -------
        ::

            # Get an workspace
            workspace = user.getExperiment(123)

            # Get the sharelink for the experiment
            sharelink = experiment.getSharelink()

            # Edit the sharelink
            sharelink.edit(type='view')
        """
        from labstep.generic.entity.repository import editEntity

        options = {True: "edit", False: "none", UNSPECIFIED: UNSPECIFIED}

        fields = {
            "experiment_workflow": options[experiment_sharing],
            "protocol_collection": options[protocol_sharing],
            "resource": options[resource_sharing],
            **extraParams,
        }
        return editEntity(self, fields=fields)
