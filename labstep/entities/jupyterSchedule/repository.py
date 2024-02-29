#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.jupyterSchedule.model import JupyterSchedule
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED

def newJupyterNotebookSchedule(user, jupyter_notebook_guid, frequency, extraParams={}):
    cron_expression=''
    if frequency == 'weekly':
        cron_expression='0 0 * * MON *'
    elif frequency == 'daily':
        cron_expression='0 0 * * ? *'
    elif frequency == 'hourly':
        cron_expression='0 * * * ? *'

    params = {"jupyter_notebook_guid": jupyter_notebook_guid, 
              'cron_expression':cron_expression, **extraParams}
    return entityRepository.newEntity(user, JupyterSchedule, params)

def getJupyterSchedule(user, guid):
    return entityRepository.getEntity(user, JupyterSchedule, id=guid)

def getJupyterSchedules(user,jupyter_notebook_guid, count=UNSPECIFIED, extraParams={}):
    params = {'jupyter_notebook_guid':jupyter_notebook_guid,
              **extraParams}
    return entityRepository.getEntities(user, JupyterSchedule, count, params)

def editJupyterSchedule(jupyter_schedule: JupyterSchedule, 
                    frequency=UNSPECIFIED, 
                    deleted_at=UNSPECIFIED, 
                    extraParams={}
):
    if frequency != UNSPECIFIED:
        cron_expression=''
        if frequency == 'weekly':
            cron_expression='0 0 * * MON *'
        elif frequency == 'daily':
            cron_expression='0 0 * * ? *'
        elif frequency == 'hourly':
            cron_expression='0 * * * ? *'
    else:
        cron_expression=UNSPECIFIED
        
    params = {"cron_expression": cron_expression, 
              "deleted_at": deleted_at, 
              **extraParams}

    return entityRepository.editEntity(jupyter_schedule, params)
