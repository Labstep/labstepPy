#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>
import labstep
import os
import pytest
from fixtures import loadFixtures


class TestJupyter:
    def setup_method(self):
        loadFixtures('Python\\\\Jupyter')

    def test_not_in_jupyter(self):
        with pytest.raises(Exception):
            labstep.jupyter.getExperiment()

    # Disabled tests not working on CI
    # def test_in_jupyter(self):
    #     os.environ["LABSTEP_API_KEY"] = "test@labstep.com"
    #     os.environ["LABSTEP_JUPYTER_EXPERIMENT_GUID"] = "abcd"
    #     experimentProtocol = labstep.jupyter.getExperiment()
    #     assert 2 == experimentProtocol.id
    #     assert "abcd" == experimentProtocol.guid

