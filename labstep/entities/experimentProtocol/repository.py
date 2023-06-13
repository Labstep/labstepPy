#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import labstep.generic.entity.repository as entityRepository


def exportExperimentProtocol(experimentProtocol, rootPath, folderName):

    experimentProtocol.update()

    expDir = entityRepository.exportEntity(
        experimentProtocol, rootPath, folderName=folderName)

    # save steps
    stepsDir = expDir.joinpath('steps')
    steps = experimentProtocol.getSteps()

    for step in steps:
        step.export(stepsDir)

    # save inventory fields
    inventoryFieldsDir = expDir.joinpath('inventory')
    inventoryFields = experimentProtocol.getInventoryFields()

    for inventoryField in inventoryFields:
        inventoryField.export(inventoryFieldsDir)

    # save data fields
    dataDir = expDir.joinpath('data')
    data = experimentProtocol.getDataFields()

    for dat in data:
        dat.export(dataDir)
