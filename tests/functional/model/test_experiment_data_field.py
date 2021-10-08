#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from fixtures import experimentDataField, experimentMaterial, loadFixtures, authUser
from shared import sharedTests


class TestExperimentDataField:

    @pytest.fixture
    def entity(self):
        return experimentDataField()

    @pytest.fixture
    def material(self):
        return experimentMaterial()

    def setup_method(self):
        loadFixtures('Python\\\\Metadata')

    def test_edit(self, entity):
        result = entity.edit(fieldName='Pytest Edited')
        assert result.label == 'Pytest Edited'

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_link_to_material(self):
        user = authUser()
        exp = user.newExperiment('Test')
        data = exp.addDataField('Test')
        material = exp.addMaterial('Test')
        data.linkToMaterial(material)
        linkedMaterials = data.getLinkedMaterials()
        assert linkedMaterials[0].id == material.id
