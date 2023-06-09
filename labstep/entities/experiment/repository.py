#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.service.helpers import (
    handleDate,
)
from labstep.entities.experiment.model import Experiment, ExperimentProtocol
import labstep.generic.entity.repository as entityRepository
from labstep.service.htmlExport import htmlExportService
from labstep.service.htmlToPDF import htmlToPDF
from labstep.constants import UNSPECIFIED
from labstep.config.export import includePDF


def getExperiment(user, experiment_id):
    return entityRepository.getEntity(user, Experiment, id=experiment_id)


def getExperiments(

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
        **extraParams,
    }
    return entityRepository.getEntities(user, Experiment, count, params)


def newExperiment(user, name, entry=UNSPECIFIED, extraParams={}):
    params = {"name": name, **extraParams}

    experiment = entityRepository.newEntity(user, Experiment, params)

    if entry is not UNSPECIFIED:
        experiment = experiment.edit(entry=entry)

    return experiment


def addProtocolToExperiment(experiment, protocol):
    params = {
        "experiment_workflow_id": experiment.id,
        "protocol_id": protocol.last_version["id"],
    }
    return entityRepository.newEntity(
        experiment.__user__, ExperimentProtocol, params
    )


def editExperiment(

    experiment,
    name=UNSPECIFIED,
    entry=UNSPECIFIED,
    started_at=UNSPECIFIED,
    deleted_at=UNSPECIFIED,
    extraParams={},
):
    params = {
        "name": name,
        "started_at": handleDate(started_at),
        "deleted_at": deleted_at,
        **extraParams,
    }

    if entry is not UNSPECIFIED:
        experiment.root_experiment.edit(body=entry)
        experiment.update()

    return entityRepository.editEntity(experiment, params)


def exportExperiment(experiment, root_path):

    experiment.update()

    expDir = entityRepository.exportEntity(
        experiment, root_path)

    # export entry
    experiment.root_experiment.export(expDir, folderName='entry')

    # export protocols
    protocolsDir = expDir.joinpath('protocols')
    protocols = experiment.getProtocols(count=UNSPECIFIED)

    for protocol in protocols:
        protocol.export(protocolsDir)

    # export notes
    notesDir = expDir.joinpath('notes')
    notes = experiment.getComments(count=UNSPECIFIED)

    for note in notes:
        note.export(notesDir)

    # get html
    html = htmlExportService.getHTML(experiment, withImages=includePDF)
    html_with_paths = htmlExportService.insertFilepaths(expDir, html)

    with open(expDir.joinpath(f'{expDir.name}.html'), 'w', encoding="utf-8") as out:
        out.write(html_with_paths)

    # get pdf
    if includePDF:
        pdf = htmlToPDF(experiment.__user__, html)
        with open(expDir.joinpath(f'{expDir.name}.pdf'), 'wb') as out:
            out.write(pdf)
