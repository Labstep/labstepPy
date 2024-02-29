#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from labstep.entities.experiment.model import Experiment
from .fixtures import fixtures


class TestExperimentLink:
    @pytest.fixture
    def entity(self):
        experiment1 = fixtures.experiment()
        experiment2 = fixtures.experiment()
        return experiment1.addExperimentLink(experiment2.id)

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Experiment')

    def test_delete(self, entity):
        entity.delete()
        assert entity.deleted_at is not None

    def test_get_source_experiment(self, entity):
        source = entity.getSourceExperiment()
        assert isinstance(source, Experiment)

    def test_get_target_experiment(self, entity):
        target = entity.getTargetExperiment()
        assert isinstance(target, Experiment)
