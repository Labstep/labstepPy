#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from labstep.entities.molecule.repository import newMolecule
from .shared import sharedTests

# __tracebackhide__ = True


""" class TestMolecule:
    @pytest.fixture
    def entity(self):
        molecule = newMolecule()
        return molecule()

    def setup_method(self):
        loadFixtures('Python\\\\Molecule')

    def test_delete(self, entity):
        assert sharedTests.delete(entity) """
