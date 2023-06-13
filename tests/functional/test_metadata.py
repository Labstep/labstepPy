#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import json
import pytest
from .fixtures import metadata, authUser, resource, testString, loadFixtures
from .shared import sharedTests


class TestMetadata:

    @pytest.fixture
    def entity(self):
        return metadata()

    def setup_method(self):
        loadFixtures('Python\\\\Metadata')

    def test_edit(self, entity):
        result = entity.edit(fieldName='Pytest Edited')
        assert result.label == 'Pytest Edited'

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test__get_value(self):
        user = authUser()
        new_resource = user.newResource('Sequence')
        result = new_resource.addMetadata(fieldName='seq', fieldType='sequence', extraParams={
            'sequence': {
            'data': json.dumps({"circular":"true", "sequence": 'ATG'}),
            'name': 'start codon'
            }})
        assert result.getValue()['sequence'] == 'ATG'
