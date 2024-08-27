#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import os

import pytest
from labstep.entities.user.model import User

import labstep

from .fixtures import fixtures, newString, testString


class TestUser:

    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def otherWorkspace(self):
        return fixtures.workspace()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\User')

    def test_setWorkspace(self, user, otherWorkspace):
        user.setWorkspace(otherWorkspace.id)
        experiment = user.newExperiment('Test')
        experiments = otherWorkspace.getExperiments()
        assert experiments[0].id == experiment.id

    # getSingle()
    def test_experiments(self, user):
        entity = user.newExperiment(testString)
        result = user.getExperiment(entity.id)
        assert result.name == testString

    def test_getProtocol(self, user):
        entity = user.newProtocol(testString)
        result = user.getProtocol(entity.id)
        assert result.name == testString

    def test_getResource(self, user):
        entity = user.newResource(testString)
        result = user.getResource(entity.id)
        assert result.name == testString

    def test_getResourceLocation(self, user):
        entity = user.newResourceLocation(testString)
        result = user.getResourceLocation(entity.guid)
        assert result.name == testString

    def test_getResourceCategory(self, user):
        entity = user.newResourceCategory(testString)
        result = user.getResourceCategory(entity.id)
        assert result.name == testString

    def test_getOrderRequest(self, user):
        new_resource = user.newResource(testString)
        entity = user.newOrderRequest(resource_id=new_resource.id)
        result = user.getOrderRequest(entity.id)
        assert result.name == testString

    def test_getWorkspace(self, user):
        entity = user.newWorkspace(testString)
        result = user.getWorkspace(entity.id)
        assert result.name == testString

    def test_getFile(self, user):
        entity = user.newFile(os.path.abspath(__file__))
        result = user.getFile(entity.id)
        assert result.id == entity.id

    def test_getPurchaseOrder(self, user):
        entity = user.newPurchaseOrder()
        result = user.getPurchaseOrder(entity.id)
        assert result.id == entity.id

    def test_getExperimentTemplate(self, user):
        entity = user.newExperimentTemplate(testString)
        result = user.getExperimentTemplate(entity.id)
        assert result.name == testString

    def test_getEntityStateWorkflow(self, user):
        entity = user.newEntityStateWorkflow(testString)
        result = user.getEntityStateWorkflow(entity.id)
        assert result.name == testString

    # getMany()
    def test_getExperiments(self, user):
        user.newExperiment(testString)
        result = user.getExperiments(count=10)
        assert result[0].id

    def test_getProtocols(self, user):
        user.newProtocol(testString)
        result = user.getProtocols(count=10)
        assert result[0].id

    def test_getResources(self, user):
        user.newResource(testString)
        result = user.getResources(count=10)
        assert result[0].id

    def test_getResourceItems(self, user):
        resource = user.newResource(testString)
        resource.newItem()
        result = user.getResourceItems(count=10)
        assert result[0].id

    def test_getResourceCategorys(self, user):
        user.newResourceCategory(testString)
        result = user.getResourceCategorys(count=10)
        assert result[0].id

    def test_getResourceLocations(self, user):
        user.newResourceLocation(testString)
        result = user.getResourceLocations(count=10)
        assert result[0].id

    def test_getOrderRequests(self, user):
        new_resource = user.newResource(testString)
        entity = user.newOrderRequest(resource_id=new_resource.id)
        result = user.getOrderRequests(count=10)
        assert result[0].id

    def test_getOrderRequestsWithFilter(self, user: User):
        new_resource = user.newResource(testString)
        entity = user.newOrderRequest(resource_id=new_resource.id)
        result = user.getOrderRequests(status='new', count=10)
        assert result[0].id

    def test_getTags(self, user):
        user.newTag(newString(), type='experiment_workflow')
        result = user.getTags(count=10)
        assert result[0].id

    def test_getWorkspaces(self, user):
        user.newWorkspace(testString)
        result = user.getWorkspaces(count=10)
        assert result[0].id

    def test_getPurchaseOrders(self, user):
        purchase_order_open = user.newPurchaseOrder(status='open')
        purchase_order_pending = user.newPurchaseOrder(status='pending')
        purchase_order_completed = user.newPurchaseOrder(status='completed')

        result_open = user.getPurchaseOrders(status='open')
        result_pending = user.getPurchaseOrders(status='pending')
        result_completed = user.getPurchaseOrders(status='completed')

        assert purchase_order_open.id == result_open[0]['id'] and \
            purchase_order_pending.id == result_pending[0]['id'] and \
            purchase_order_completed.id == result_completed[0]['id']

    def test_getExperimentTemplates(self, user):
        user.newExperimentTemplate(testString)
        result = user.getExperimentTemplates()
        assert result[0].id

    def test_getEntityStateWorkflows(self, user):
        user.newEntityStateWorkflow(testString)
        result = user.getEntityStateWorkflows()
        assert result[0].id

    # newEntity()

    def test_newExperiment(self, user):
        result = user.newExperiment(testString)
        assert result.name == testString

    def test_newProtocol(self, user):
        result = user.newProtocol(testString)
        assert result.name == testString

    def test_newResource(self, user):
        result = user.newResource(testString)
        assert result.name == testString

    def test_newResourceCategory(self, user):
        result = user.newResourceCategory(testString)
        assert result.name == testString

    def test_newResourceLocation(self, user):
        result = user.newResourceLocation('testLocation')
        result.delete()
        assert result.name == 'testLocation'

    def test_newOrderRequest(self, user):
        entity = user.newResource(testString)
        result = user.newOrderRequest(resource_id=entity.id)
        assert result.name == testString

    def test_newTag(self, user):
        name = newString()
        result = user.newTag(name, type='experiment_workflow')
        assert result.name == name

    def test_newWorkspace(self, user):
        result = user.newWorkspace(testString)
        assert result.name == testString

    def test_newFile(self, user):
        result = user.newFile(os.path.abspath(__file__))
        assert result is not None

    def test_acceptShareLink(self, user):
        # FIXME should be a workspace the user isn't already in!
        newWorkspace = fixtures.workspace()
        sharelink = newWorkspace.getSharelink()
        result = user.acceptSharelink(sharelink.token)

    def test_newDeviceCategory(self, user):
        result = user.newDeviceCategory(testString)
        assert result.name == testString

    def test_newAPIKey(self, user):
        from labstep.service.helpers import getTime
        result = user.newAPIKey(testString, expires_at=getTime())
        assert result.name == testString

    def test_newPurchaseOrder(self, user):
        result = user.newPurchaseOrder(testString)
        assert result.name == testString

    def test_newExperimentTemplate(self, user):
        result = user.newExperimentTemplate(testString)
        assert result.name == testString

    def test_newEntityStateWorkflow(self, user):
        result = user.newEntityStateWorkflow(testString)
        assert result.name == testString
