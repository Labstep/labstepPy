#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class ProtocolSmartTable(Entity):
    __entityName__ = "entity-view"

    def edit(self, name=UNSPECIFIED, columns=UNSPECIFIED):
        """
        Edit an existing Protocol Smart Table.

        Parameters
        ----------
        name (str)
            The name of the smart table.
        columns (list)
            List of column definition IDs.

        Returns
        -------
        :class:`~labstep.entities.protocolSmartTable.model.ProtocolSmartTable`
            An object representing the edited Protocol Smart Table.
        """
        import labstep.generic.entity.repository as entityRepository

        params = {"name": name, "column_definition_ids": columns}
        return entityRepository.editEntity(self, params)
