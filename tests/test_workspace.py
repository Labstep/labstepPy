#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import user, workspace, testString

# Make new entity
entity = workspace()

user.setWorkspace(entity.id)


class TestWorkspace:
    def test_edit(self):
        result = entity.edit('Pytest Edited')
        assert result.name == 'Pytest Edited', \
            'FAILED TO EDIT WORKSPACE'

    def test_delete(self):
        entityToDelete = user.newWorkspace(testString)
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE WORKSPACE'

    # getMany()
    def test_getExperiments(self):
        user.newExperiment(testString)
        result = entity.getExperiments()
        assert result[0].id, \
            'FAILED TO GET EXPERIMENTS'

    def test_getProtocols(self):
        user.newProtocol(testString)
        result = entity.getProtocols()
        assert result[0].id, \
            'FAILED TO GET PROTOCOLS'

    def test_getResources(self):
        user.newResource(testString)
        result = entity.getResources()
        assert result[0].id, \
            'FAILED TO GET RESOURCES'

    def test_getResourceCategorys(self):
        user.newResourceCategory(testString)
        result = entity.getResourceCategorys()
        assert result[0].id, \
            'FAILED TO GET RESOURCE CATEGORYS'

    def test_getResourceLocations(self):
        new_RL = user.newResourceLocation(testString)
        result = entity.getResourceLocations()
        new_RL.delete()
        assert result[0].id, \
            'FAILED TO GET RESOURCE LOCATIONS'

    def test_getOrderRequests(self):
        new_resource = user.newResource(testString)
        new_resource.newOrderRequest()
        result = entity.getOrderRequests()
        assert result[0].id, \
            'FAILED TO GET ORDER REQUESTS'

    def test_getTags(self):
        new_tag = user.newTag('test_newTag', type='experiment_workflow')
        result = entity.getTags()
        new_tag.delete()
        assert result[0].id, \
            'FAILED TO GET TAGS'

    def test_getFiles(self):
        result = entity.getFiles()
        assert len(result) >= 0, \
            'FAILED TO GET FILES'

    def test_getMembers(self):
        result = entity.getMembers()
        assert len(result) >= 0, \
            'FAILED TO GET MEMBERS'

    def test_getSharelink(self):
        sharelink = entity.getSharelink()
        assert sharelink is not None

    def test_getCollections(self):
        result = entity.getCollections()
        assert len(result) >= 0

    def test_autoSharing(self):
        result = entity.setAutosharing(experiment_sharing=False,
                                       protocol_sharing=False,
                                       resource_sharing=False)

        result = entity.setAutosharing(experiment_sharing=True,
                                       protocol_sharing=True,
                                       resource_sharing=True)

        assert result is not None
