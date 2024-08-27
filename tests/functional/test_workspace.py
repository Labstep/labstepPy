#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

import labstep

from .fixtures import fixtures, testString
from .shared import sharedTests


class TestWorkspace:

    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def entity(self):
        return fixtures.workspace()

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_getSharelink(self, entity):
        assert sharedTests.sharelink(entity)

    # getMany()
    def test_getExperiments(self, entity, user):
        user.setWorkspace(entity.id)
        user.newExperiment(testString)
        result = entity.getExperiments()
        assert result[0].id

    def test_getProtocols(self, entity, user):
        user.setWorkspace(entity.id)
        user.newProtocol(testString)
        result = entity.getProtocols()
        assert result[0].id

    def test_getResources(self, entity, user):
        user.setWorkspace(entity.id)
        user.newResource(testString)
        result = entity.getResources()
        assert result[0].id

    def test_getResourceItems(self, entity, user):
        user.setWorkspace(entity.id)
        user.newResource(testString).newItem()
        result = entity.getResourceItems()
        assert result[0].id

    def test_getResourceCategorys(self, entity, user):
        user.setWorkspace(entity.id)
        user.newResourceCategory(testString)
        result = entity.getResourceCategorys()
        assert result[0].id

    def test_getResourceLocations(self, entity, user):
        user.setWorkspace(entity.id)
        new_RL = user.newResourceLocation(testString)
        result = entity.getResourceLocations()
        assert result[0].id

    def test_getOrderRequests(self, entity, user):
        user.setWorkspace(entity.id)
        new_resource = user.newResource(testString)
        new_resource.newOrderRequest()
        result = entity.getOrderRequests()
        assert result[0].id

    def test_getTags(self, entity, user):
        user.setWorkspace(entity.id)
        new_tag = user.newTag('test_newTag', type='experiment_workflow')
        result = entity.getTags()
        new_tag.delete()
        assert result[0].id

    def test_getFiles(self, entity):
        result = entity.getFiles()
        assert len(result) >= 0

    def test_getMembers(self, entity):
        result = entity.getMembers()
        assert len(result) >= 0

    def test_getCollections(self, entity):
        result = entity.getCollections()
        assert len(result) >= 0

    def test_getDeviceCategorys(self, entity, user):
        user.setWorkspace(entity.id)
        workspace = user.getWorkspace(entity.id)
        device_category = user.newDeviceCategory(testString)
        result = workspace.getDeviceCategorys()
        assert result[0].id == device_category.id

    def test_getJupyterNotebook(self, entity, user):
        user.setWorkspace(entity.id)
        workspace = user.getWorkspace(entity.id)
        new_jupyterNotebook = workspace.addJupyterNotebook(name=testString)
        entity_from_get = workspace.getJupyterNotebook(
            new_jupyterNotebook.guid)
        assert new_jupyterNotebook.guid == entity_from_get.guid

    def test_getJupyterNotebooks(self, entity, user):
        user.setWorkspace(entity.id)
        workspace = user.getWorkspace(entity.id)
        new_jupyterNotebook = workspace.addJupyterNotebook(name=testString)
        entities_from_get = workspace.getJupyterNotebooks()
        assert new_jupyterNotebook.guid == entities_from_get[0].guid

    def test_getCollaboratorRoles(self, entity):
        collaboratorRole = entity.newCollaboratorRole(name=testString, description=testString)
        get_collaborator_roles = entity.getCollaboratorRoles()

        assert get_collaborator_roles[0].id == collaboratorRole.id

    def test_getExperimentTemplates(self, entity):
        experiment_template = entity.newExperimentTemplate(name=testString)
        get_experiment_templates = entity.getExperimentTemplates()

        assert get_experiment_templates[0].id == experiment_template.id

    def test_getEntityStateWorkflow(self, entity):
        entityStateWorkflow = entity.newEntityStateWorkflow(name=testString)
        get_state_workflows = entity.getEntityStateWorkflows()

        assert get_state_workflows[0].id == entityStateWorkflow.id


