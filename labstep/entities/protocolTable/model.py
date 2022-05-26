#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import dataTableToDataFrame
from labstep.constants import UNSPECIFIED


class ProtocolTable(Entity):
    __entityName__ = "protocol-table"
    __hasGuid__ = True

    def edit(self, name=UNSPECIFIED, data=UNSPECIFIED, extraParams={}):
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
        import labstep.generic.entity.repository as entityRepository

        params = {"name": name, "data": data, **extraParams}
        return entityRepository.editEntity(self, params)

    def getDataTable(self):
        return self.data['data']['dataTable']

    def getDataFrame(self):
        """
        Converts a Labstep Table to a Pandas DataFrame.

        The first row of the Labstep Table is used as the column names for the DataFrame.

        Returns
        -------
        DataFrame
            A pandas dataframe.

        Example
        -------
        ::

            data = {
                "rowCount": 2,
                "columnCount": 2,
                "data": {
                    "dataTable": {
                        0: {
                            0: {
                                "value": 'Column A'
                            },
                            1: {
                                "value": 'Column B'
                            }
                        },
                        1: {
                            0: {
                                "value": "A1"
                            },
                            1: {
                                "value": "B1"
                            }
                        }
                    }
                }
            }

            protocol = user.getProtocol(17000)
            protocol_table = protocol.addTable(name='Test Table', data=data)
            dataFrame = protocol_table.getDataFrame()
            print(dataFrame['Column A'][0])
        """
        return dataTableToDataFrame(self.getDataTable())
