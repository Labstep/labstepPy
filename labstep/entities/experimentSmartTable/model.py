#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class ExperimentSmartTable(Entity):
    __entityName__ = "entity-view"

    def edit(self, name=UNSPECIFIED, columns=UNSPECIFIED):
        """
        Edit an existing Experiment Step.

        Parameters
        ----------
        completed_at (str)
            The datetime at which the Experiment Step was completed.

        Returns
        -------
        :class:`~labstep.entities.experimentStep.model.ExperimentStep`
            An object representing the edited Experiment Step.
        """
        import labstep.generic.entity.repository as entityRepository

        params = {"name": name, "column_definition_ids": columns}
        return entityRepository.editEntity(self, params)
