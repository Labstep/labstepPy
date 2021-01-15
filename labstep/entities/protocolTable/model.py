#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity


class ProtocolTable(Entity):
    __entityName__ = "protocol-table"

    def edit(self, name=None, data=None, extraParams={}):
        """
        Edit an existing Protocol Table.

        Parameters
        ----------
        name (str)
            The name of the Protocol Table.
        data (str)
            The data of the table in json format.

        Returns
        -------
        :class:`~labstep.entities.protocolTable.model.ProtocolTable`
            An object representing the edited Protocol Table.

        Example
        -------
        ::

            data = {
                "rowCount": 6,
                "columnCount": 6,
                "colHeaderData": {},
                "data": {
                    "dataTable": {
                        0: {
                            0: {
                                "value": 'Cell A1'
                            },
                            1: {
                                "value": 'Cell B1'
                            }
                        }
                    }
                }
            }

            protocol = user.getProtocol(17000)
            protocol_tables = protocol.getTables()
            protocol_tables[0].edit(name='New Table Name', data=data)
        """
        from labstep.generic.entity.repository import entityRepository

        params = {"name": name, "data": data, **extraParams}
        return entityRepository.editEntity(self, params)
