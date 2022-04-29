#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>


import labstep
import os
import re
import subprocess
from dotenv import load_dotenv
from labstep.entities.protocol.model import Protocol
from labstep.entities.experiment.model import Experiment
from labstep.entities.device.model import Device
from labstep.entities.resource.model import Resource
from labstep.entities.workspace.model import Workspace
from labstep.entities.resourceLocation.model import ResourceLocation
from labstep.entities.resourceItem.model import ResourceItem
from labstep.entities.orderRequest.model import OrderRequest
from labstep.entities.resourceCategory.model import ResourceCategory
from labstep.entities.experimentProtocol.model import ExperimentProtocol
from labstep.entities.collection.model import Collection
from labstep.entities.metadata.model import Metadata
from labstep.entities.jupyterNotebook.repository import newJupyterNotebook
from labstep.entities.user.repository import newUser


load_dotenv(override=True)
LABSTEP_API_URL = os.getenv("LABSTEP_API_URL")
LABSTEP_API_USERNAME = os.getenv("LABSTEP_API_USERNAME")
LABSTEP_API_APIKEY = os.getenv("LABSTEP_API_APIKEY")
SYMFONY_CONSOLE_PATH = os.getenv("LABSTEP_SYMFONY_CONSOLE_PATH")


def loadFixtures(name):
    if 'api' in LABSTEP_API_URL:
        return
    print(f'\nLoading Fixtures {name}')

    command = f'php {SYMFONY_CONSOLE_PATH} labstep:load-fixtures {name} --force'
    popen = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    retval = popen.wait()
    stdoutValue, stderrValue = popen.communicate()
    assert retval == 0
    assert stderrValue is None
    assert 'Database ready' in stdoutValue.decode('utf-8')
    print('\nFixtures loaded')

    command = f'php {SYMFONY_CONSOLE_PATH} fos:elastica:populate --env=prod'
    popen = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    retval = popen.wait()
    stdoutValue, stderrValue = popen.communicate()
    assert stderrValue is None
    print('\nES populated\n')


def authUser():
    return labstep.authenticate(LABSTEP_API_USERNAME, LABSTEP_API_APIKEY)


tableData = {
    "rowCount": 6,
    "columnCount": 6,
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

proseMirrorState = {
    "type": "doc",
    "content": [
        {
            "type": "paragraph",
            "attrs": {"align": None},
            "content": [
                {
                    "type": "text",
                            "text": "test"
                }
            ]
        },
        {
            "type": "paragraph",
            "attrs": {"align": None}
        }
    ]
}


def proseMirrorStateWithSteps(steps):
    return {
        "type": "doc",
        "content": [
                {
                    "type": "protocol_step",
                    "attrs": {"id": steps[0].id},
                    "content": [{
                            "type": "paragraph",
                            "attrs": {"align": None}
                    }]
                },
            {
                    "type": "protocol_step",
                    "attrs": {"id": steps[1].id},
                    "content": [{
                        "type": "paragraph",
                        "attrs": {"align": None}}
                    ]}
        ]
    }


testString = labstep.service.helpers.getTime()


def collaborator(token):
    uniqueString = re.sub(r'[^\w]', '', labstep.service.helpers.getTime())
    return newUser(
        first_name='Team',
        last_name='Labstep',
        email=f'{uniqueString}@labstep.com',
        password='testpass',
        share_link_token=token)


def newString():
    return labstep.service.helpers.getTime()


def experiment():
    user = authUser()
    return user.newExperiment(testString)


def protocol():
    user = authUser()
    return user.newProtocol(testString)


def experimentProtocol():
    user = authUser()
    exp = user.newExperiment(testString)
    experiment_protocol = exp.addProtocol(protocol())
    return experiment_protocol


def resource():
    user = authUser()
    return user.newResource(testString)


def resourceCategory():
    user = authUser()
    return user.newResourceCategory(testString)


def orderRequest():
    user = authUser()
    new_resource = resource()
    return user.newOrderRequest(resource_id=new_resource.id)


def resourceItem():
    return resource().newItem(name='Pytest Acetone')


def resourceLocation():
    user = authUser()
    return user.newResourceLocation(testString)


def workspace():
    user = authUser()
    return user.newWorkspace(testString)


def protocolCollection():
    user = authUser()
    return user.newCollection(newString(), type="protocol")


def experimentCollection():
    user = authUser()
    return user.newCollection(newString())


def device():
    user = authUser()
    return user.newDevice(newString())


def chemicalReaction():
    user = authUser()
    experiment = user.newExperiment('Test')
    experiment_protocol = experiment.addProtocol(protocol())
    return experiment_protocol.addChemicalReaction()


def metadata():
    user = authUser()
    resourceWithMetadata = user.newResource(testString)
    return resourceWithMetadata.addMetadata(testString)


def experimentDataField():
    user = authUser()
    exp = user.newExperiment(testString)
    return exp.addDataField('Test')


def protocolDataField():
    user = authUser()
    p = user.newProtocol(testString)
    return p.addDataField('Test')


def experimentInventoryField():
    user = authUser()
    exp = user.newExperiment(testString)
    return exp.addInventoryField('Test')


def tag():
    user = authUser()
    return user.newTag('Test Tag', type='experiment_workflow')


def jupyterNotebook():
    user = authUser()
    jupyterNotebook = user.getJupyterNotebook('guid-test')
    #jupyterNotebook = newJupyterNotebook(user, 'Test Notebook')
    return jupyterNotebook


def jupyterInstance():
    user = authUser()
    jupyterInstance = user.getJupyterInstance('guid-test')
    return jupyterInstance
