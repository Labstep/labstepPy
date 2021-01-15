#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity


class ExperimentTable(Entity):
    __entityName__ = "experiment-table"

    def edit(self, data=None):
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
        from labstep.generic.entity.repository import entityRepository

        params = {"data": data}
        return entityRepository.editEntity(self, params)
