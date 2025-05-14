#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.constants import UNSPECIFIED
from labstep.generic.entity.model import Entity


class JupyterInstance(Entity):
    """
    Represents an JupyterInstance on Labstep.
    """

    __entityName__ = "jupyter-instance"
    __hasGuid__ = True

    def edit(self, startedAt=UNSPECIFIED, endedAt=UNSPECIFIED, status=UNSPECIFIED, data=UNSPECIFIED, errorMessage=UNSPECIFIED):
        """
        Edit an existing JupyterInstance.

        Parameters
        ----------
        startedAt (datetime, optional)
            Start date.
        endedAt (datetime, optional)
            End date.
        status (string, optional)
            Status can be 'success' or 'error'.
        errorMessage (string, optional)
            Error message.

        Returns
        -------
        :class:`~labstep.entities.jupyterInstance.model.Device`
            An object representing the edited Device.

        Example
        -------
        ::

            myJuyterInstance = user.getJupyterInstance('943fe3f3-a50e-40a0-9b91-a0fa5675b9ac)
            myJuyterInstance.edit(startedAt='2024-01-01T00:00:00+0000')
        """
        import labstep.entities.jupyterInstance.repository as jupyterInstanceRepository

        return jupyterInstanceRepository.editJupyterInstance(
            self,
            startedAt,
            endedAt,
            status,
            data,
            errorMessage
        )
