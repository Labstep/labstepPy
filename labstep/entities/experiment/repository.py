#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import os
import json
from pathlib import Path
from labstep.service.helpers import (
    getTime,
    createdAtFrom,
    createdAtTo,
    handleDate,
    listToClass,
)
from labstep.entities.experiment.model import Experiment, ExperimentProtocol
from labstep.service.request import requestService
from labstep.generic.entity.repository import entityRepository
from labstep.service.htmlExport import htmlExportService


class ExperimentRepository:
    def getExperiment(self, user, experiment_id):
        return entityRepository.getEntity(user, Experiment, id=experiment_id)

    def getExperiments(
        self,
        user,
        count=100,
        search_query=None,
        created_at_from=None,
        created_at_to=None,
        tag_id=None,
        collection_id=None,
        extraParams={},
    ):
        params = {
            "search_query": search_query,
            "created_at_from": createdAtFrom(created_at_from),
            "created_at_to": createdAtTo(created_at_to),
            "tag_id": tag_id,
            "folder_id": collection_id,
            **extraParams,
        }
        return entityRepository.getEntities(user, Experiment, count, params)

    def newExperiment(self, user, name, entry=None, extraParams={}):
        params = {"name": name, **extraParams}

        experiment = entityRepository.newEntity(user, Experiment, params)

        if entry is not None:
            experiment = experiment.edit(entry=entry)

        return experiment

    def addProtocolToExperiment(self, experiment, protocol):
        params = {
            "experiment_workflow_id": experiment.id,
            "protocol_id": protocol.last_version["id"],
        }
        return entityRepository.newEntity(
            experiment.__user__, ExperimentProtocol, params
        )

    def editExperiment(
        self,
        experiment,
        name=None,
        entry=None,
        started_at=None,
        deleted_at=None,
        extraParams={},
    ):
        params = {
            "name": name,
            "started_at": handleDate(started_at),
            "deleted_at": deleted_at,
            **extraParams,
        }

        if entry is not None:
            experiment.root_experiment.edit(body=entry)
            experiment.update()

        return entityRepository.editEntity(experiment, params)

    def exportExperiment(self, experiment, root_path):

        expDir = entityRepository.exportEntity(experiment, root_path)

        # export entry
        entryDir = expDir.joinpath('entry')
        experiment.update().root_experiment.update().export(entryDir)

        # export protocols
        protocolsDir = expDir.joinpath('protocols')
        protocols = experiment.getProtocols(count=100)

        for protocol in protocols:
            protocol.export(protocolsDir)

        # export notes
        notesDir = expDir.joinpath('notes')
        notes = experiment.getComments(count=1000)

        for note in notes:
            note.export(notesDir)

        # get html
        html = htmlExportService.getHTML(experiment)
        html_with_paths = htmlExportService.insertFilepaths(expDir, html)

        with open(expDir.joinpath('entity.html'), 'w') as out:
            out.write(html_with_paths)


experimentRepository = ExperimentRepository()
