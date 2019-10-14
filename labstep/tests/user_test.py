#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS


testUser = LS.login('demo@labstep.com', 'demopassword')


class TestUser:
    def test_get_experiment(self):
        exp = testUser.getExperiment(23450)
        assert exp['name'] == "API Test Experiment", \
            "INCORRECT EXPERIMENT NAME!"
        assert exp['description'] == "<p>API Test Description</p>", \
            "INCORRECT EXPERIMENT DESCRIPTION!"
