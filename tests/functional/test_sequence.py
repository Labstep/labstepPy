#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from labstep.entities.sequence.model import Sequence
import pytest
from .fixtures import fixtures
from .shared import sharedTests


class TestSequence:

    @pytest.fixture
    def entity(self):
        return fixtures.sequence()

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self, entity):

        newData = '''
        {"circular": true, "sequence": "actagct", "proteinSequence": "", "size": 7, "proteinSize": 0, "features": {}, "warnings": {}, "assemblyPieces": {}, "lineageAnnotations": {}, "parts": {
        }, "cutsites": {}, "orfs": {}, "translations": {}, "primers": {}, "guides": {}, "materiallyAvailable": true, "description": "", "fromFileUpload": false, "stateTrackingId": "l4i9w7wv", "filteredFeatures": {}}
        '''
        edited = entity.edit(data=newData)

        assert edited.data == newData
