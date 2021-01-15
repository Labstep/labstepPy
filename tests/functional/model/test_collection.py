#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from fixtures import user, newString

class TestCollection:
    def test_edit(self):
        entity = user.newCollection(newString(), 'experiment')
        newName = newString()
        result = entity.edit(newName)
        result.delete()
        assert result.name == newName, \
            'FAILED TO EDIT COLLECTION NAME'

    def test_delete(self):
        entityToDelete = user.newCollection(newString(), 'experiment')
        result = entityToDelete.delete()
        assert result.deleted_at is not None, \
            'FAILED TO DELETE COLLECTION'

    def test_getExperiments(self):
        collection = user.newCollection(newString(), 'experiment')
        experiment = user.newExperiment(newString())
        experiment.addToCollection(collection.id)
        experiments = user.getExperiments(collection_id=collection.id)
        assert experiments[0].id == experiment.id

    def test_getProtocols(self):
        collection = user.newCollection(newString(), 'protocol')
        protocol = user.newProtocol(newString())
        protocol.addToCollection(collection.id)
        protocols = user.getProtocols(collection_id=collection.id)
        assert protocols[0].id == protocol.id
