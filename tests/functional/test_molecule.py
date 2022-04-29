#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest
from .fixtures import loadFixtures
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
