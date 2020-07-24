#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fixtures import user, newString


class TestTag:
    def test_edit(self):
        entity = user.newTag(newString(), 'experiment_workflow')
        newName = newString()
        result = entity.edit(newName)
        result.delete()
        assert result.name == newName, \
            'FAILED TO EDIT TAG NAME'

    def test_delete(self):
        entityToDelete = user.newTag(newString(), 'experiment_workflow')
        result = entityToDelete.delete()
        assert result is None, \
            'FAILED TO DELETE TAG'
