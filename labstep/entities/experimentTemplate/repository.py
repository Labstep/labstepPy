#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep.generic.entity.repository as entityRepository
from labstep.config.export import includePDF
from labstep.constants import UNSPECIFIED
from labstep.entities.experimentTemplate.model import (ExperimentProtocol,
                                                       ExperimentTemplate)
from labstep.service.helpers import handleDate
from labstep.service.htmlExport import htmlExportService
from labstep.service.htmlToPDF import htmlToPDF


def getExperimentTemplate(user, experiment_template_id):
    return entityRepository.getEntity(user, ExperimentTemplate, id=experiment_template_id)


def getExperimentTemplates(

    user,
    count=UNSPECIFIED,
    search_query=UNSPECIFIED,
    created_at_from=UNSPECIFIED,
    created_at_to=UNSPECIFIED,
    tag_id=UNSPECIFIED,
    collection_id=UNSPECIFIED,
    extraParams={},
):
    params = {
        "search_query": search_query,
        "created_at_from": handleDate(created_at_from),
        "created_at_to": handleDate(created_at_to),
        "tag_id": tag_id,
        "folder_id": collection_id,
        'is_template':True,
        **extraParams,
    }
    return entityRepository.getEntities(user, ExperimentTemplate, count, params)


def newExperimentTemplate(user, name, entry=UNSPECIFIED,entity_state_workflow_id=UNSPECIFIED, extraParams={}):
    params = {"name": name, **extraParams, "is_template": 1, "entity_state_workflow_id": entity_state_workflow_id}

    experimentTemplate = entityRepository.newEntity(user, ExperimentTemplate, params)

    if entry is not UNSPECIFIED:
        experimentTemplate = experimentTemplate.edit(entry=entry)

    return experimentTemplate


def addProtocolToExperimentTemplate(experimentTemplate, protocol):
    params = {
        "experiment_workflow_id": experimentTemplate.id,
        "protocol_id": protocol.last_version["id"],
    }
    return entityRepository.newEntity(
        experimentTemplate.__user__, ExperimentProtocol, params
    )