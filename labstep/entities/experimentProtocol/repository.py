#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.repository import entityRepository
from labstep.entities.experiment.model import ExperimentProtocol

class ExperimentProtocolRepository:
    def getExperimentProtocolByGuid(self, user, guid):
        return entityRepository.getEntityByGuid(user, ExperimentProtocol, guid=guid)

    def exportExperimentProtocol(self, experimentProtocol, rootPath, folderName):

        experimentProtocol.update()

        expDir = entityRepository.exportEntity(
            experimentProtocol, rootPath, folderName=folderName)

        # save materials
        materialsDir = expDir.joinpath('materials')
        materials = experimentProtocol.getMaterials()

        for material in materials:
            material.export(materialsDir)

        # save data
        dataDir = expDir.joinpath('data')
        data = experimentProtocol.getDataFields()

        for dat in data:
            dat.export(dataDir)


experimentProtocolRepository = ExperimentProtocolRepository()
