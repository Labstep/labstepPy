#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
import pytest

from labstep.entities.experiment.model import Experiment
from .fixtures import experiment, loadFixtures


class TestExperimentLink:
    @pytest.fixture
    def entity(self):
        experiment1 = experiment()
        experiment2 = experiment()
        return experiment1.addExperimentLink(experiment2.id)

    def setup_method(self):
        loadFixtures('Python\\\\Experiment')

    def test_delete(self, entity):
        entity.delete()
        assert entity.deleted_at is not None

    def test_get_source_experiment(self, entity):
        source = entity.getSourceExperiment()
        assert isinstance(source, Experiment)

    def test_get_target_experiment(self, entity):
        target = entity.getTargetExperiment()
        assert isinstance(target, Experiment)
