#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>

from labstep.entities.jupyterInstance.repository import jupyterInstanceRepository


def editJupyterInstance(
    jupyterInstance, startedAt=None, endedAt=None
):
    """
    Edit an existing JupyterInstance.

    Parameters
    ----------
    jupyterInstance (obj)
        The JupyterInstance to edit.
    startedAt (str)
        The date the instance was started and ready
        in the format of "YYYY-MM-DD HH:MM".
    endedAt (str)
        The date the instance was shutdown
        in the format of "YYYY-MM-DD HH:MM".

    Returns
    -------
    jupyterInstance
        An object representing the edited JupyterInstance.
    """
    return jupyterInstanceRepository.editJupyterInstance(
        jupyterInstance, startedAt, endedAt
    )
