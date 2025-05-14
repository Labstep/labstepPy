#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures, proseMirrorState
from .shared import sharedTests


class TestExperimentProtocol:
    @pytest.fixture
    def entity(self):
        return fixtures.experimentProtocol()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\ExperimentProtocol')

    def test_edit(self, entity):
        entity.edit(name='Edit Test', body=proseMirrorState)
        entity.update()
        assert entity.name == 'Edit Test' \
            and entity.getBody() == proseMirrorState

    def test_get_experiment(self, entity):
        experiment = entity.getExperiment()
        assert experiment is not None

    def test_steps(self, entity):
        entity.addSteps(2)
        steps = entity.getSteps()
        result = steps[0].complete()
        assert result.ended_at is not None and len(steps) >= 2

    def test_inventory_fields(self, entity):
        assert sharedTests.inventoryFields(entity)

    def test_timers(self, entity):
        assert sharedTests.timers(entity)

    def test_tables(self, entity):
        assert sharedTests.tables(entity)

    def test_dataFields(self, entity):
        assert sharedTests.dataFields(entity)

    def test_files(self, entity):
        assert sharedTests.files(entity)

    def test_jupyter_notebooks(self, entity):
        assert sharedTests.jupyterNotebooks(entity)

    def test_experiment_protocol_conditions(self, entity):
        assert sharedTests.experimentConditions(entity)
