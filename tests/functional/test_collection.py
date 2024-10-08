#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures, newString
from .shared import sharedTests


class TestCollection:
    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def entity(self):
        return fixtures.experimentCollection()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Collection')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_getExperiments(self, entity, user):
        experimentToAdd = fixtures.experiment()
        experimentToAdd.addToCollection(entity.id)
        experiments = user.getExperiments(collection_id=entity.id)
        assert experiments[0].id == experimentToAdd.id

    def test_getProtocols(self, user):
        collection = user.newCollection(newString(), 'protocol')
        protocol = user.newProtocol(newString())
        protocol.addToCollection(collection.id)
        protocols = user.getProtocols(collection_id=collection.id)
        assert protocols[0].id == protocol.id

    def test_subCollections(self, entity):
        fromCreate = entity.addSubCollections(
            names=['Folder A', 'Folder B'])

        fromGet = entity.getSubCollections()

        assert fromCreate.get('Folder A').id == fromGet.get('Folder A').id
