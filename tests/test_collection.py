#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import user, newString


class TestCollection:
    def test_edit(self):
        entity = user.newCollection(newString(), 'experiment_workflow')
        newName = newString()
        result = entity.edit(newName)
        result.delete()
        assert result.name == newName, \
            'FAILED TO EDIT COLLECTION NAME'

    def test_delete(self):
        entityToDelete = user.newCollection(newString(), 'experiment_workflow')
        result = entityToDelete.delete()
        assert result is None, \
            'FAILED TO DELETE COLLECTION'

    def test_getExperiments(self):
        entity = user.newCollection(newString(), 'experiment_workflow')
        experiments = entity.getExperiments()
        assert experiments == []
