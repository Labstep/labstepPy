#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>


import labstep
import os
import random
import string
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
from labstep.entities.organization.repository import newOrganization
from labstep.entities.user.repository import newUser, getUser
from labstep.entities.sequence.repository import newSequence
from labstep.generic.entity.repository import editEntity, getEntity
from labstep.entities.user.model import User
from labstep.entities.organization.model import Organization
from labstep.constants.unspecified import UNSPECIFIED
from labstep.service.helpers import configService

load_dotenv(override=True)
LABSTEP_API_URL = os.getenv("LABSTEP_API_URL")
LABSTEP_API_USERNAME = os.getenv("LABSTEP_API_USERNAME")
LABSTEP_API_APIKEY = os.getenv("LABSTEP_API_APIKEY")
LABSTEP_PERMISSIONS_ADMIN = os.getenv("LABSTEP_PERMISSIONS_ADMIN")
LABSTEP_PERMISSIONS_MEMBER_ONE = os.getenv('LABSTEP_PERMISSIONS_MEMBER_ONE')
LABSTEP_PERMISSIONS_MEMBER_TWO = os.getenv('LABSTEP_PERMISSIONS_MEMBER_TWO')
LABSTEP_PERMISSIONS_ADMIN_APIKEY = os.getenv(
    "LABSTEP_PERMISSIONS_ADMIN_APIKEY")
LABSTEP_PERMISSIONS_MEMBER_ONE_APIKEY = os.getenv(
    'LABSTEP_PERMISSIONS_MEMBER_ONE_APIKEY')
LABSTEP_PERMISSIONS_MEMBER_TWO_APIKEY = os.getenv(
    'LABSTEP_PERMISSIONS_MEMBER_TWO_APIKEY')
SYMFONY_CONSOLE_PATH = os.getenv("LABSTEP_SYMFONY_CONSOLE_PATH")

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


def newString(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def new_email():
    return f'test+{newString()}@labstep.com'


testString = newString()


class Fixtures:

    _defaultUser = None

    def loadFixtures(self, name):
        if 'staging' in LABSTEP_API_URL:
            return

        if 'api.labstep.com' in LABSTEP_API_URL:
            raise Exception(
                'Test suite should not be run on production environment. Check your .env')

        if ('LABSTEP_DEBUG' in os.environ.keys()):
            print(f'\nLoading Fixtures {name}')

        command = f'php {SYMFONY_CONSOLE_PATH} labstep:load-fixtures {name} --force -e prod'

        if ('LABSTEP_DEBUG' in os.environ.keys()):
            print(f'\nCommand: {command}')

        popen = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        retval = popen.wait()
        stdoutValue, stderrValue = popen.communicate()

        if ('LABSTEP_DEBUG' in os.environ.keys()):
            print(f'\nOutput: {stdoutValue}')
            print(f'\nErr: {stderrValue}')

        assert retval == 0
        assert stderrValue is None
        assert 'Database ready' in stdoutValue.decode('utf-8')

        if ('LABSTEP_DEBUG' in os.environ.keys()):
            print('\nFixtures loaded')

    def defaultUser(self):

        if self._defaultUser is None:
            self._defaultUser = labstep.authenticate(
                apikey=LABSTEP_API_APIKEY)

        return self._defaultUser

    def experiment(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newExperiment(newString())

    def protocol(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newProtocol(newString())

    def experimentProtocol(self, user=None):
        user = user if user is not None else self.defaultUser()
        exp = user.newExperiment(newString())
        experiment_protocol = exp.addProtocol(self.protocol())
        return experiment_protocol

    def resource(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newResource(newString())

    def resourceCategory(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newResourceCategory(newString())

    def orderRequest(self, user=None):
        user = user if user is not None else self.defaultUser()
        new_resource = self.resource()
        return user.newOrderRequest(resource_id=new_resource.id)

    def purchaseOrder(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newPurchaseOrder()

    def resourceItem(self, user=None):
        user = user if user is not None else self.defaultUser()
        return self.resource().newItem(name='Pytest Acetone')

    def resourceLocation(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newResourceLocation(newString())

    def workspace(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newWorkspace(newString())

    def protocolCollection(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newCollection(newString(), type="protocol")

    def experimentCollection(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newCollection(newString())

    def device(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newDevice(newString())

    def chemicalReaction(self, user=None):
        user = user if user is not None else self.defaultUser()
        experiment = user.newExperiment('Test')
        experiment_protocol = experiment.addProtocol(self.protocol())
        return experiment_protocol.addChemicalReaction()

    def metadata(self, user=None):
        user = user if user is not None else self.defaultUser()
        resourceWithMetadata = user.newResource(newString())
        return resourceWithMetadata.addMetadata(newString())

    def metadataDate(self, user=None):
        user = user if user is not None else self.defaultUser()
        resourceWithMetadata = user.newResource(newString())
        return resourceWithMetadata.addMetadata(newString(), fieldType='date')

    def experimentDataField(self, user=None):
        user = user if user is not None else self.defaultUser()
        exp = user.newExperiment(newString())
        return exp.addDataField('Test')

    def protocolDataField(self, user=None):
        user = user if user is not None else self.defaultUser()
        p = user.newProtocol(newString())
        return p.addDataField('Test')

    def experimentInventoryField(self, user=None):
        user = user if user is not None else self.defaultUser()
        exp = user.newExperiment(newString())
        return exp.addInventoryField('Test')

    def tag(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newTag('Test Tag', type='experiment_workflow')

    def jupyterNotebook(self, user=None):
        user = user if user is not None else self.defaultUser()
        exp = user.newExperiment(newString())

        jupyterNotebook = newJupyterNotebook(user, 'Test Notebook', extraParams={
            'experiment_id': exp.root_experiment.id})
        return jupyterNotebook

    def jupyterInstance(self, user=None):
        user = user if user is not None else self.defaultUser()
        jupyterInstance = user.getJupyterInstance(
            'd4b88c0b-37e8-4c84-8ce6-49a5661cd646')
        return jupyterInstance

    def sequence(self, user=None):
        user = user if user is not None else self.defaultUser()
        resource = user.newResource(newString())
        metadata = resource.addMetadata(newString())
        return newSequence(user, metadata.id)

    def experiment_jupyterNotebook(self, user=None):
        user = user if user is not None else self.defaultUser()
        exp = user.newExperiment(newString())
        return exp.addJupyterNotebook('Test')

    def protocol_jupyterNotebook(self, user=None):
        user = user if user is not None else self.defaultUser()
        prot = user.newProtocol(newString())
        return prot.addJupyterNotebook('Test')

    def experiment_protocol_conditions(self, user=None):
        user = user if user is not None else self.defaultUser()
        exp = user.newExperiment(newString())
        return exp.addConditions(1)

    def protocol_protocol_conditions(self, user=None):
        user = user if user is not None else self.defaultUser()
        prot = user.newProtocol(newString())
        return prot.addConditions(1)

    def deviceCategory(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newDeviceCategory(newString())

    def new_user(self, token=UNSPECIFIED):
        return newUser(
            first_name='Test',
            last_name='User',
            email=new_email(),
            password='gehwuigGHEUWIG123478!@$%£^@',
            share_link_token=token,
            extraParams={'is_signup_enterprise': True, 'skip_verification_email': True})

    def workspace_role(self, user: User = None):
        user = user if user is not None else self.defaultUser()
        [org, users] = self.organization_with_users(user)

        return org.newWorkspaceRole(name=newString())

    def organization_with_users(self, user: User = None):
        user = user if user is not None else self.defaultUser()
        org = newOrganization(user, newString())
        wspace = user.newWorkspace(newString())
        user.setWorkspace(wspace.id)
        email1 = new_email()
        email2 = new_email()
        org.inviteUsers(emails=[email1, email2], workspace_id=wspace.id)
        invitations = org.getPendingInvitations()
        invite_token = invitations[0].share_link['token']
        another_user = newUser(
            first_name='Team',
            last_name='Labstep',
            email=email1,
            password='gehwuigGHEUWIG123478!@$%£^@',
            share_link_token=invite_token,
            extraParams={'is_signup_enterprise': True, 'skip_verification_email': True})

        invite_token = invitations[1].share_link['token']
        user2 = newUser(
            first_name='Team',
            last_name='Labstep',
            email=email2,
            password='gehwuigGHEUWIG123478!@$%£^@',
            share_link_token=invite_token,
            extraParams={'is_signup_enterprise': True, 'skip_verification_email': True})

        return org, [another_user, user2]

    def collaborator(self, main_user: User):
        [org, users] = self.organization_with_users(main_user)

        experiment = main_user.newExperiment(name='Test')

        return experiment.assign(users[0].id)

    def jupyterSchedule(self, user=None):
        user = user if user is not None else self.defaultUser()
        exp = user.newExperiment(newString())
        jnotebook = exp.addJupyterNotebook('Test')
        return jnotebook.newJupyterSchedule('weekly')

    def api_key(self, user=None):
        user = user if user is not None else self.defaultUser()
        return user.newAPIKey(newString())

    def device_booking(self, user=None):
        user = user if user is not None else self.defaultUser()
        device = user.newDevice(name=newString())
        return device.addDeviceBooking(started_at='2025-12-01 00:00', ended_at='2025-12-02 00:00')

    def permissions_test_users():
        admin = labstep.authenticate('', LABSTEP_PERMISSIONS_ADMIN_APIKEY)
        member_1 = labstep.authenticate(
            LABSTEP_PERMISSIONS_MEMBER_ONE, LABSTEP_PERMISSIONS_MEMBER_ONE_APIKEY)
        member_2 = labstep.authenticate(
            LABSTEP_PERMISSIONS_MEMBER_TWO, LABSTEP_PERMISSIONS_MEMBER_TWO_APIKEY)
        return [admin, member_1, member_2]


fixtures = Fixtures()
