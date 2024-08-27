#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import os

import pytest

import labstep

from .fixtures import fixtures


class TestJupyter:
    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Jupyter')

    def test_not_in_jupyter(self):
        with pytest.raises(Exception):
            labstep.jupyter.getParent()

    # Disabled tests not working on CI
    # def test_in_jupyter(self):
    #     os.environ["LABSTEP_API_KEY"] = "test@labstep.com"
    #     os.environ["LABSTEP_JUPYTER_EXPERIMENT_GUID"] = "abcd"
    #     experimentProtocol = labstep.jupyter.getExperiment()
    #     assert 2 == experimentProtocol.id
    #     assert "abcd" == experimentProtocol.guid
