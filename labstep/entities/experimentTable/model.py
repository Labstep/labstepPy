#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import dataTableToDataFrame
from labstep.constants import UNSPECIFIED


class ExperimentTable(Entity):
    __entityName__ = "protocol-table"
    __hasGuid__ = True

    def edit(self, name=UNSPECIFIED, data=UNSPECIFIED):
        """
        Edit an existing Experiment Table.

        Parameters
        ----------
        name (str)
            The name of the Experiment Table.
        data (str)
            The data of the table.

        Returns
        -------
        :class:`~labstep.entities.experimentTable.model.ExperimentTable`
            An object representing the edited Experiment Table.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            exp_protocol = experiment.getProtocols()[0]
            exp_protocol_tables = exp_protocol.getTables()
            data = {
                "rowCount": 12,
                "columnCount": 12,
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
            exp_protocol_tables[0].edit(data=data)
        """
        import labstep.generic.entity.repository as entityRepository

        params = {"name": name, "data": data}
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

            experiment = user.getExperiment(17000)
            experiment_table = experiment.addTable(name='Test Table', data=data)
            dataFrame = experiment_table.getDataFrame()
            print(dataFrame['Column A'][0])
        """
        return dataTableToDataFrame(self.getDataTable())
