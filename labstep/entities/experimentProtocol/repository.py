#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.repository import entityRepository


class ExperimentProtocolRepository:
    def exportExperimentProtocol(self, experimentProtocol, rootPath):

        expDir = entityRepository.exportEntity(experimentProtocol, rootPath)

        # save materials
        materialsDir = expDir.joinpath('materials')
        materials = experimentProtocol.getMaterials()

        for material in materials:
            material.export(materialsDir)

        # save data
        dataDir = expDir.joinpath('data')
        data = experimentProtocol.getDataElements()

        for dat in data:
            dat.export(dataDir)


experimentProtocolRepository = ExperimentProtocolRepository()
